import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pandas as pd
from config import *

class GoogleSheetsAPI:
    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        self.service = None
        self.authenticate()
    
    def authenticate(self):
        """Xác thực Google Sheets API"""
        creds = None
        
        # Token file lưu access và refresh tokens
        if os.path.exists(GOOGLE_SHEETS_TOKEN_FILE):
            creds = Credentials.from_authorized_user_file(GOOGLE_SHEETS_TOKEN_FILE, self.SCOPES)
        
        # Nếu không có credentials hợp lệ, cho phép user login
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists(GOOGLE_SHEETS_CREDENTIALS_FILE):
                    raise FileNotFoundError(f"Không tìm thấy file {GOOGLE_SHEETS_CREDENTIALS_FILE}. "
                                          f"Vui lòng tải credentials từ Google Cloud Console.")
                
                flow = InstalledAppFlow.from_client_secrets_file(
                    GOOGLE_SHEETS_CREDENTIALS_FILE, self.SCOPES)
                creds = flow.run_local_server(port=0)
            
            # Lưu credentials cho lần chạy tiếp theo
            with open(GOOGLE_SHEETS_TOKEN_FILE, 'w') as token:
                token.write(creds.to_json())
        
        self.service = build('sheets', 'v4', credentials=creds)
    
    def read_sheet_data(self, range_name=None):
        """Đọc dữ liệu từ Google Sheets"""
        try:
            if not range_name:
                range_name = f"{SHEET_NAME}!A:E"  # Đọc từ cột A đến E
            
            sheet = self.service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                      range=range_name).execute()
            values = result.get('values', [])
            
            if not values:
                print('Không tìm thấy dữ liệu trong sheet.')
                return []
            
            return values
            
        except Exception as e:
            print(f"Lỗi khi đọc dữ liệu: {e}")
            return []
    
    def write_to_sheet(self, row, col, value):
        """Ghi dữ liệu vào một ô cụ thể"""
        try:
            range_name = f"{SHEET_NAME}!{col}{row}"
            
            body = {
                'values': [[value]]
            }
            
            result = self.service.spreadsheets().values().update(
                spreadsheetId=SPREADSHEET_ID,
                range=range_name,
                valueInputOption='RAW',
                body=body
            ).execute()
            
            print(f"Đã cập nhật {result.get('updatedCells')} ô.")
            return True
            
        except Exception as e:
            print(f"Lỗi khi ghi dữ liệu: {e}")
            return False
    
    def update_row_data(self, row_index, data_dict):
        """Cập nhật một hàng với dictionary data"""
        try:
            # Tạo list values theo thứ tự cột A-E
            values = []
            for col_name, col_letter in COLUMNS.items():
                if col_name in data_dict:
                    values.append(data_dict[col_name])
                else:
                    values.append('')  # Ô trống nếu không có dữ liệu
            
            range_name = f"{SHEET_NAME}!A{row_index}:E{row_index}"
            
            body = {
                'values': [values]
            }
            
            result = self.service.spreadsheets().values().update(
                spreadsheetId=SPREADSHEET_ID,
                range=range_name,
                valueInputOption='RAW',
                body=body
            ).execute()
            
            print(f"Đã cập nhật hàng {row_index}: {result.get('updatedCells')} ô.")
            return True
            
        except Exception as e:
            print(f"Lỗi khi cập nhật hàng {row_index}: {e}")
            return False
    
    def get_next_available_row(self):
        """Tìm hàng trống tiếp theo để thêm dữ liệu mới"""
        data = self.read_sheet_data()
        if not data:
            return 2  # Hàng 1 là header, bắt đầu từ hàng 2
        return len(data) + 1
    
    def find_email_ready_row(self):
        """Tìm hàng có Email nhưng chưa có MetaMask/Twitter"""
        data = self.read_sheet_data()
        if not data:
            return None
        
        # Bỏ qua header (hàng đầu tiên)
        for i, row in enumerate(data[1:], start=2):
            # Kiểm tra: có email (cột A) nhưng chưa có metamask (cột B) hoặc twitter (cột C)
            if (len(row) > 0 and row[0] != '' and  # Có email
                (len(row) <= 1 or row[1] == '') and  # Chưa có metamask
                (len(row) <= 2 or row[2] == '')):    # Chưa có twitter
                
                return {
                    'row_index': i,
                    'email': row[0],
                    'metamask': row[1] if len(row) > 1 else '',
                    'twitter': row[2] if len(row) > 2 else '',
                    'status_x': row[3] if len(row) > 3 else '',
                    'done': row[4] if len(row) > 4 else ''
                }
        
        return None
    
    def find_empty_row(self):
        """Tìm hàng trống để ghi dữ liệu mới"""
        data = self.read_sheet_data()
        if not data:
            return 2  # Hàng 2 nếu sheet trống
        
        # Bỏ qua header (hàng đầu tiên)
        for i, row in enumerate(data[1:], start=2):
            # Kiểm tra nếu email (cột A) trống
            if len(row) <= 0 or row[0] == '':
                return i
        
        # Nếu không có hàng trống, trả về hàng tiếp theo
        return len(data) + 1
    
    def mark_done(self, row_index):
        """Đánh dấu task hoàn thành"""
        return self.write_to_sheet(row_index, COLUMNS['DONE'], 'TRUE')
    
 