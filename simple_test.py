#!/usr/bin/env python3
"""
Test đơn giản: tìm hàng trống và ghi dữ liệu thử
"""

from google_sheets_api import GoogleSheetsAPI

def find_empty_row_and_write():
    """Tìm hàng trống và ghi dữ liệu test"""
    
    print("🧪 TEST ĐƠN GIẢN - GHI DỮ LIỆU VÀO ONEFOOTBALL CLUB")
    print("="*60)
    
    try:
        # Kết nối API
        print("📡 Đang kết nối...")
        api = GoogleSheetsAPI()
        
        # Đọc dữ liệu hiện tại
        print("📖 Đang đọc sheet 'Onefootball Club'...")
        data = api.read_sheet_data()
        
        if not data:
            print("❌ Không đọc được dữ liệu từ sheet")
            return
        
        print(f"✅ Đọc thành công {len(data)} hàng")
        
        # In ra một vài hàng đầu để xem cấu trúc
        print("\n📊 Dữ liệu hiện tại:")
        for i, row in enumerate(data[:5]):  # Chỉ in 5 hàng đầu
            print(f"Hàng {i+1}: {row}")
        
        # Tìm hàng trống để ghi
        empty_row = None
        for i, row in enumerate(data):
            # Kiểm tra nếu hàng có ít nhất 1 cột trống ở Email (cột B)
            if len(row) <= 1 or (len(row) > 1 and row[1] == ''):
                empty_row = i + 1  # +1 vì Google Sheets bắt đầu từ 1
                break
        
        if not empty_row:
            # Nếu không có hàng trống, tạo hàng mới
            empty_row = len(data) + 1
        
        print(f"\n🎯 Sẽ ghi dữ liệu vào hàng {empty_row}")
        
        # Ghi dữ liệu test
        test_email = "test123@outlook.com"
        test_metamask = "0x1234567890abcdef1234567890abcdef12345678"
        test_twitter = "@testuser123"
        
        print(f"\n📝 Đang ghi dữ liệu test...")
        print(f"   Email: {test_email}")
        print(f"   MetaMask: {test_metamask}")
        print(f"   Twitter: {test_twitter}")
        
        # Ghi từng ô (theo cấu trúc đúng: A=Email, B=Metamask, C=Twitter)
        api.write_to_sheet(empty_row, 'A', test_email)      # Cột A: Email
        api.write_to_sheet(empty_row, 'B', test_metamask)   # Cột B: MetaMask  
        api.write_to_sheet(empty_row, 'C', test_twitter)    # Cột C: Twitter
        
        print(f"\n✅ HOÀN THÀNH! Đã ghi dữ liệu vào hàng {empty_row}")
        print(f"🔗 Kiểm tra tại: https://docs.google.com/spreadsheets/d/1Lqzi-H-npwmFRU07NWBMk0y3-tgaFrXHOKW-21qUpr4/edit")
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")

if __name__ == "__main__":
    find_empty_row_and_write() 