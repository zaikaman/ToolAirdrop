#!/usr/bin/env python3
"""
Gemini AI API module để tạo tên email ngẫu nhiên
"""

import google.generativeai as genai
from config import GEMINI_API_KEY

class GeminiEmailGenerator:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY không được cấu hình trong .env")
        
        # Cấu hình Gemini API
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
    
    def generate_unique_email(self):
        """Tạo tên email outlook ngẫu nhiên và độc đáo"""
        
        prompt = """think of a random but incredibly unique name for an outlook account, for example abcxyz@outlook.com, only response the name, must be all lowcaps, must have @outlook.com"""
        
        try:
            print("🤖 Đang hỏi Gemini AI...")
            response = self.model.generate_content(prompt)
            
            email = response.text.strip()
            
            # Đảm bảo email có @outlook.com
            if '@outlook.com' not in email:
                # Nếu AI không trả về đúng format, tạo fallback
                import random
                fallback_email = f"unique{random.randint(10000, 99999)}@outlook.com"
                print(f"⚠️ AI response không đúng format, dùng fallback: {fallback_email}")
                return fallback_email
            
            print(f"✨ Gemini AI đề xuất: {email}")
            return email
            
        except Exception as e:
            print(f"❌ Lỗi khi gọi Gemini API: {e}")
            
            # Fallback nếu API lỗi
            import random
            fallback_email = f"backup{random.randint(10000, 99999)}@outlook.com"
            print(f"🔄 Sử dụng email backup: {fallback_email}")
            return fallback_email
    
    def test_api(self):
        """Test Gemini API"""
        try:
            print("🧪 Testing Gemini API...")
            email = self.generate_unique_email()
            print(f"✅ Test thành công: {email}")
            return True
        except Exception as e:
            print(f"❌ Test thất bại: {e}")
            return False

if __name__ == "__main__":
    # Test API
    generator = GeminiEmailGenerator()
    generator.test_api() 