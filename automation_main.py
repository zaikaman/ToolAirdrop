#!/usr/bin/env python3
"""
Main automation script - Tự động tạo tài khoản và ghi vào Google Sheets
"""

from google_sheets_api import GoogleSheetsAPI
import time
import random

def create_account_data():
    """Tạo dữ liệu tài khoản mới (hiện tại là mock data)"""
    
    # Tạo random data cho demo
    random_num = random.randint(1000, 9999)
    
    account_data = {
        'EMAIL': f'user{random_num}@outlook.com',
        'METAMASK': f'abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about{random_num}',
        'TWITTER': f'@cryptouser{random_num}',
        'STATUS_X': '',  # Để trống ban đầu
        'DONE': ''       # Để trống ban đầu
    }
    
    print(f"📧 Email: {account_data['EMAIL']}")
    print(f"🦊 MetaMask: {account_data['METAMASK'][:50]}...")
    print(f"🐦 Twitter: {account_data['TWITTER']}")
    
    return account_data

def main():
    """Main automation workflow"""
    
    print("🤖 AUTOMATION TOOL - ONEFOOTBALL CLUB")
    print("="*50)
    
    try:
        # Kết nối Google Sheets
        print("📡 Đang kết nối Google Sheets...")
        api = GoogleSheetsAPI()
        
        # Tìm hàng trống
        print("🔍 Tìm hàng trống...")
        empty_row = api.find_empty_row()
        print(f"📍 Sẽ ghi vào hàng {empty_row}")
        
        # Tạo dữ liệu tài khoản
        print(f"\n🚀 Tạo tài khoản mới...")
        account_data = create_account_data()
        
        # Ghi vào Google Sheets
        print(f"\n💾 Ghi dữ liệu vào Google Sheets...")
        success = api.update_row_data(empty_row, account_data)
        
        if success:
            print(f"\n✅ THÀNH CÔNG! Đã tạo tài khoản ở hàng {empty_row}")
            print(f"🔗 Kiểm tra: https://docs.google.com/spreadsheets/d/1Lqzi-H-npwmFRU07NWBMk0y3-tgaFrXHOKW-21qUpr4/edit")
        else:
            print(f"\n❌ LỖI khi ghi dữ liệu!")
            
    except Exception as e:
        print(f"❌ LỖI: {e}")

if __name__ == "__main__":
    main() 