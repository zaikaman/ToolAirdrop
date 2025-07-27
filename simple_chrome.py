#!/usr/bin/env python3
"""
Simple Chrome automation bằng subprocess - không cần Selenium
"""

import os
import subprocess
import time
from config import CHROME_PROFILES_DIR

class SimpleChromeAutomation:
    def __init__(self):
        self.profiles_dir = CHROME_PROFILES_DIR
        self.ensure_profiles_dir()
        self.chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            r"C:\Users\{}\AppData\Local\Google\Chrome\Application\chrome.exe".format(os.getenv('USERNAME')),
        ]
    
    def ensure_profiles_dir(self):
        """Đảm bảo thư mục profiles tồn tại"""
        if not os.path.exists(self.profiles_dir):
            os.makedirs(self.profiles_dir)
            print(f"📁 Đã tạo thư mục: {self.profiles_dir}")
    
    def find_chrome_executable(self):
        """Tìm Chrome executable"""
        for path in self.chrome_paths:
            if os.path.exists(path):
                return path
        return None
    
    def create_profile_name(self, email):
        """Tạo tên profile từ email"""
        profile_name = email.split('@')[0]
        invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*', '.']
        for char in invalid_chars:
            profile_name = profile_name.replace(char, '_')
        return f"profile_{profile_name}"
    
    def get_profile_path(self, email):
        """Lấy đường dẫn profile từ email"""
        profile_name = self.create_profile_name(email)
        return os.path.join(self.profiles_dir, profile_name)
    
    def open_chrome_with_profile(self, email, url="https://outlook.live.com/owa/"):
        """Mở Chrome với profile và URL"""
        
        chrome_exe = self.find_chrome_executable()
        if not chrome_exe:
            print("❌ Không tìm thấy Chrome executable")
            return False
        
        profile_path = self.get_profile_path(email)
        profile_name = self.create_profile_name(email)
        
        print(f"🌐 Mở Chrome với profile: {profile_name}")
        print(f"📁 Profile path: {profile_path}")
        print(f"🔗 URL: {url}")
        
        # Command để mở Chrome
        cmd = [
            chrome_exe,
            f"--user-data-dir={profile_path}",
            "--new-window",
            "--no-first-run",
            "--no-default-browser-check",
            url
        ]
        
        try:
            # Mở Chrome
            subprocess.Popen(cmd, shell=False)
            
            print(f"✅ Chrome đã mở thành công!")
            print(f"👤 Bạn có thể đăng ký tài khoản với email: {email}")
            
            return True
            
        except Exception as e:
            print(f"❌ Lỗi mở Chrome: {e}")
            return False
    
    def wait_for_user_input(self, message="Nhấn Enter sau khi hoàn thành..."):
        """Đợi user input"""
        input(f"\n⏸️ {message}")

def test_simple_chrome():
    """Test Simple Chrome"""
    
    print("🧪 TEST SIMPLE CHROME")
    print("="*30)
    
    test_email = "test123@outlook.com"
    
    chrome = SimpleChromeAutomation()
    
    # Mở Chrome
    success = chrome.open_chrome_with_profile(test_email)
    
    if success:
        chrome.wait_for_user_input("Hoàn thành đăng ký và nhấn Enter...")
        print("✅ Test hoàn thành!")
    else:
        print("❌ Test thất bại!")

if __name__ == "__main__":
    test_simple_chrome() 