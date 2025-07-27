#!/usr/bin/env python3
"""
Chrome automation module - Tạo profile và tự động hóa Chrome
"""

import os
import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import CHROME_PROFILES_DIR

class ChromeAutomation:
    def __init__(self):
        self.profiles_dir = CHROME_PROFILES_DIR
        self.ensure_profiles_dir()
    
    def ensure_profiles_dir(self):
        """Đảm bảo thư mục profiles tồn tại"""
        if not os.path.exists(self.profiles_dir):
            os.makedirs(self.profiles_dir)
            print(f"📁 Đã tạo thư mục: {self.profiles_dir}")
    
    def create_profile_name(self, email):
        """Tạo tên profile từ email"""
        # Lấy phần trước @ và làm sạch ký tự đặc biệt
        profile_name = email.split('@')[0]
        # Thay thế ký tự không hợp lệ
        invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', '.']
        for char in invalid_chars:
            profile_name = profile_name.replace(char, '_')
        
        return f"profile_{profile_name}"
    
    def get_profile_path(self, email):
        """Lấy đường dẫn profile từ email"""
        profile_name = self.create_profile_name(email)
        return os.path.join(self.profiles_dir, profile_name)
    
    def create_chrome_driver(self, email):
        """Tạo Chrome driver với profile riêng"""
        
        profile_path = self.get_profile_path(email)
        profile_name = self.create_profile_name(email)
        
        print(f"🌐 Tạo Chrome profile: {profile_name}")
        print(f"📁 Đường dẫn: {profile_path}")
        
        # Cấu hình Chrome options
        chrome_options = Options()
        chrome_options.add_argument(f"--user-data-dir={profile_path}")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument("--disable-extensions-file-access-check")
        chrome_options.add_argument("--disable-extensions-http-throttling")
        
        # Tắt các thông báo
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        # Tạo driver với multiple fallbacks
        try:
            # Method 1: ChromeDriverManager với cache clear
            print("🔄 Thử ChromeDriverManager...")
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            
        except Exception as e1:
            print(f"⚠️ ChromeDriverManager failed: {e1}")
            try:
                # Method 2: Undetected Chrome (fallback)
                print("🔄 Thử undetected-chromedriver...")
                import undetected_chromedriver as uc
                
                # Convert selenium options to uc options
                uc_options = uc.ChromeOptions()
                for arg in chrome_options.arguments:
                    uc_options.add_argument(arg)
                
                driver = uc.Chrome(options=uc_options, version_main=None)
                
            except Exception as e2:
                print(f"⚠️ Undetected Chrome failed: {e2}")
                try:
                    # Method 3: System Chrome (last resort)
                    print("🔄 Thử system Chrome...")
                    driver = webdriver.Chrome(options=chrome_options)
                    
                except Exception as e3:
                    print(f"❌ Tất cả methods đều fail:")
                    print(f"   - ChromeDriverManager: {e1}")
                    print(f"   - Undetected Chrome: {e2}")
                    print(f"   - System Chrome: {e3}")
                    return None
        
        try:
            # Ẩn thông báo automation
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            print(f"✅ Chrome profile đã sẵn sàng!")
            return driver
            
        except Exception as e:
            print(f"❌ Lỗi setup driver: {e}")
            if driver:
                driver.quit()
            return None
    
    def open_outlook(self, driver):
        """Mở trang đăng ký Outlook"""
        try:
            print("📧 Đang mở Outlook...")
            driver.get("https://outlook.live.com/owa/")
            
            # Đợi trang load
            time.sleep(3)
            
            print("✅ Đã mở Outlook.com")
            print("👤 Bạn có thể đăng ký tài khoản thủ công")
            
            return True
            
        except Exception as e:
            print(f"❌ Lỗi mở Outlook: {e}")
            return False
    
    def wait_for_user_action(self, message="Nhấn Enter để tiếp tục..."):
        """Đợi người dùng thực hiện action"""
        input(f"\n⏸️ {message}")
    
    def close_driver(self, driver):
        """Đóng Chrome driver"""
        try:
            if driver:
                driver.quit()
                print("🔒 Đã đóng Chrome")
        except Exception as e:
            print(f"⚠️ Lỗi đóng Chrome: {e}")

def test_chrome_automation():
    """Test Chrome automation"""
    
    print("🧪 TEST CHROME AUTOMATION")
    print("="*30)
    
    test_email = "test123@outlook.com"
    
    chrome = ChromeAutomation()
    
    # Tạo driver
    driver = chrome.create_chrome_driver(test_email)
    
    if driver:
        # Mở Outlook
        chrome.open_outlook(driver)
        
        # Đợi user
        chrome.wait_for_user_action("Thực hiện đăng ký và nhấn Enter...")
        
        # Đóng
        chrome.close_driver(driver)
    
    print("✅ Test hoàn thành!")

if __name__ == "__main__":
    test_chrome_automation() 