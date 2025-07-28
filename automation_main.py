#!/usr/bin/env python3
"""
Main automation script - Tự động tạo tài khoản và ghi vào Google Sheets
"""

from google_sheets_api import GoogleSheetsAPI
from undetected_chrome_final import SimpleUndetectedChrome
import time

def main():
    """Main automation workflow - Tìm email và tạo Chrome profile"""
    
    print("🤖 CHROME AUTOMATION - ONEFOOTBALL CLUB")
    print("="*45)
    
    try:
        # Kết nối Google Sheets
        print("📡 Đang kết nối Google Sheets...")
        api = GoogleSheetsAPI()
        
        # Tìm hàng có email nhưng chưa có metamask/twitter
        print("🔍 Tìm email cần xử lý...")
        email_row = api.find_email_ready_row()
        
        if not email_row:
            print("ℹ️ Không tìm thấy email nào cần xử lý")
            print("💡 Hãy thêm email vào cột A trong Google Sheets")
            return
        
        email = email_row['email']
        row_index = email_row['row_index']
        
        print(f"📧 Tìm thấy email: {email}")
        print(f"📍 Ở hàng: {row_index}")
        
        # Tạo Undetected Chrome
        print(f"\n🌐 Khởi tạo Undetected Chrome...")
        chrome = SimpleUndetectedChrome()
        
        # Tạo driver
        driver = chrome.create_driver(email)
        
        if driver:
            # Mở Outlook
            success = chrome.open_outlook()
            
            if success:
                print(f"\n✅ Outlook.com đã mở!")
                print(f"📧 Email để đăng ký: {email}")
                
                # Tự động điền email
                fill_success = chrome.auto_fill_email(email)
                
                if fill_success:
                    print(f"\n🎉 ĐÃ TỰ ĐỘNG ĐIỀN EMAIL!")
                    print(f"📝 Username đã nhập: {email.split('@')[0]}")
                    print(f"⏎ Đã ấn Enter")
                    
                    # Tự động điền mật khẩu
                    print(f"\n🔐 Tiếp tục điền mật khẩu...")
                    password_success = chrome.auto_fill_password()
                    
                    if password_success:
                        print(f"\n🎉 ĐÃ TỰ ĐỘNG ĐIỀN MẬT KHẨU!")
                        print(f"🔐 Mật khẩu: Lovelybaby93")
                        print(f"⏎ Đã ấn Enter")
                        
                        # Tìm và click nút Never trước
                        print(f"\n🖱️ Tìm và click nút Never...")
                        never_success = chrome.click_never_button()
                        
                        if never_success:
                            print(f"✅ Đã click nút Never!")
                        else:
                            print(f"⚠️ Không thể tìm/click nút Never")
                        
                        # Tự động chọn tháng sinh bằng ảnh
                        print(f"\n📅 Chọn tháng sinh bằng ảnh...")
                        month_success = chrome.auto_select_birth_month_image()
                        
                        if month_success:
                            print(f"✅ Đã chọn tháng June!")
                            
                            # Chọn ngày sinh
                            print(f"\n📅 Chọn ngày sinh...")
                            day_success = chrome.auto_select_birth_day_image()
                            
                            if day_success:
                                print(f"✅ Đã chọn ngày 8!")
                                
                                # Điền năm sinh
                                print(f"\n📅 Điền năm sinh...")
                                year_success = chrome.auto_fill_birth_year("2000")
                                
                                if year_success:
                                    print(f"✅ Đã điền năm 2000!")
                                    
                                    # Điền First name và Last name
                                    print(f"\n👤 Điền tên...")
                                    name_success = chrome.auto_fill_name("Thinh", "Dinh")
                                    
                                    if name_success:
                                        print(f"\n🎉 ĐÃ HOÀN THÀNH THÔNG TIN CƠ BẢN!")
                                        print(f"📅 Ngày sinh: 8/June/2000")
                                        print(f"👤 Tên: Thinh Dinh")
                                        print(f"⏎ Đã ấn Enter")
                                        
                                        # Tìm kiếm nút Skip for now trong quá trình human verification
                                        print(f"\n🔍 Bắt đầu tìm nút 'Skip for now'...")
                                        skip_success = chrome.wait_and_click_skip_button(10)  # Tìm trong 10 phút
                                        
                                        if skip_success:
                                            print(f"✅ Đã click 'Skip for now'!")
                                        else:
                                            print(f"\n💡 Không tìm thấy nút 'Skip for now' hoặc hết thời gian")
                                        
                                        # Mở X.com signup
                                        print(f"\n🐦 BƯỚC TIẾP THEO: TẠO TÀI KHOẢN X.COM")
                                        time.sleep(5)
                                        print(f"="*45)
                                        
                                        x_success = chrome.open_x_signup(email)
                                        
                                        if x_success:
                                            print(f"✅ Đã điền thông tin cơ bản X.com!")
                                            
                                            # Chọn ngày sinh bằng ảnh
                                            print(f"\n📅 Chọn ngày sinh...")
                                            birthday_success = chrome.select_x_birthday_images(email)
                                            
                                            if birthday_success:
                                                 # X.com signup đã hoàn thành, tiếp tục với MetaMask
                                                 print(f"\n✅ X.com signup hoàn thành!")
                                                 
                                                 # Cài đặt MetaMask extension
                                                 metamask_success = chrome.open_metamask_extension()
                                                 
                                                 if metamask_success:
                                                     print(f"\n🎉 ĐÃ HOÀN THÀNH TẤT CẢ AUTOMATION!")
                                                     print(f"✅ Outlook: contohoangtuan@outlook.com")
                                                     print(f"✅ X.com: {email.split('@')[0]}")
                                                     print(f"✅ MetaMask: Đã cài đặt extension")
                                                     print(f"\n🔄 Tiếp tục setup MetaMask thủ công...")
                                                 else:
                                                     print(f"\n⚠️ Hãy cài MetaMask thủ công:")
                                                     print(f"🦊 Vào Chrome Web Store và cài MetaMask")
                                            else:
                                                print(f"\n⚠️ Hãy chọn ngày sinh thủ công:")
                                                print(f"📅 Tháng: June, Ngày: 10, Năm: 2007")
                                                print(f"⏎ Rồi click Next 2 lần (đợi 10 giây giữa 2 lần)")
                                                print(f"🔐 Rồi điền password: lovelybaby")
                                                print(f"📝 Rồi click Sign up")
                                        else:
                                            print(f"❌ Không thể mở X.com signup")
                                            print(f"💡 Hãy mở thủ công: https://x.com/i/flow/signup")
                                    else:
                                        print(f"\n⚠️ Hãy điền tên thủ công:")
                                        print(f"👤 First name: Thinh, Last name: Dinh")
                                else:
                                    print(f"\n⚠️ Hãy điền thủ công:")
                                    print(f"📅 Năm: 2000, First name: Thinh, Last name: Dinh")
                            else:
                                print(f"\n⚠️ Hãy chọn ngày thủ công: 8")
                                print(f"📅 Và điền: Năm 2000, First name: Thinh, Last name: Dinh")
                        else:
                            print(f"\n⚠️ Hãy chọn ngày sinh thủ công:")
                            print(f"📅 Tháng: June, Ngày: 8, Năm: 2000")
                            print(f"👤 First name: Thinh, Last name: Dinh")
                    else:
                        print(f"\n⚠️ Không thể điền mật khẩu tự động")
                        print(f"🔐 Hãy nhập thủ công: Lovelybaby93")
                        print(f"📅 Ngày sinh: 8/June/2000")
                        print(f"👤 First name: Thinh, Last name: Dinh")
                else:
                    print(f"\n⚠️ Không thể tự động điền, làm thủ công:")
                    print(f"📧 Email cần đăng ký: {email}")
                    print(f"🔐 Mật khẩu: Lovelybaby93")
                
                                # Đã hoàn thành automation X.com trong bước trước
                # User ấn Enter nghĩa là đã hoàn thành X.com rồi
                print(f"\n🦊 BƯỚC TIẾP THEO: CÀI ĐẶT METAMASK")
                print(f"="*45)
                
                # Cài đặt MetaMask extension
                metamask_success = chrome.open_metamask_extension()
                
                if metamask_success:
                    print(f"\n🎉 ĐÃ CÀI ĐẶT METAMASK!")
                    print(f"✅ Outlook: {email}")
                    print(f"✅ X.com: {email.split('@')[0]}")
                    print(f"✅ MetaMask: Đã cài đặt extension")
                    print(f"\n🔄 Tiếp tục setup MetaMask...")
                    
                    # Setup MetaMask
                    setup_success = chrome.setup_metamask()
                    if setup_success:
                        print(f"✅ Đã setup MetaMask!")
                        
                        # Tạo wallet
                        wallet_success = chrome.create_metamask_wallet()
                        if wallet_success:
                            print(f"\n🎉 HOÀN THÀNH TẤT CẢ!")
                            print(f"✅ Outlook: {email}")
                            print(f"✅ X.com: {email.split('@')[0]}")  
                            print(f"✅ MetaMask: Đã tạo wallet và lưu seed phrase")
                        else:
                            print(f"⚠️ Hãy tạo wallet MetaMask thủ công")
                    else:
                        print(f"⚠️ Hãy setup MetaMask thủ công")
                else:
                    print(f"\n⚠️ Hãy cài MetaMask thủ công:")
                    print(f"🦊 Vào Chrome Web Store và cài MetaMask")
                
                # TODO: Thêm logic cập nhật Google Sheets sau khi hoàn thành
                
                # Đợi user trước khi đóng
                chrome.wait_user("Hoàn thành tất cả và nhấn Enter để đóng Chrome...")
                
            # Đóng Chrome
            chrome.close()
        else:
            print("❌ Không thể khởi tạo Chrome")
            
    except Exception as e:
        print(f"❌ LỖI: {e}")

if __name__ == "__main__":
    main() 