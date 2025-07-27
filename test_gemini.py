#!/usr/bin/env python3
"""
Test script cho Gemini API
"""

from gemini_api import GeminiEmailGenerator
from config import GEMINI_API_KEY

def test_gemini():
    print("🧪 TEST GEMINI AI - TẠO EMAIL OUTLOOK")
    print("="*50)
    
    # Kiểm tra API key
    if not GEMINI_API_KEY or GEMINI_API_KEY == 'your_gemini_api_key_here':
        print("❌ GEMINI_API_KEY chưa được cấu hình")
        print("📋 Cách lấy API key:")
        print("1. Truy cập: https://makersuite.google.com/app/apikey")
        print("2. Tạo API key mới")
        print("3. Copy key và thay thế trong file .env")
        print("   GEMINI_API_KEY=your_actual_api_key")
        return False
    
    print(f"🔑 API Key: {GEMINI_API_KEY[:10]}...{GEMINI_API_KEY[-5:]}")
    
    try:
        # Test API
        generator = GeminiEmailGenerator()
        
        print(f"\n🚀 Test tạo 3 email ngẫu nhiên:")
        for i in range(3):
            print(f"\nLần {i+1}:")
            email = generator.generate_unique_email()
            print(f"✅ Kết quả: {email}")
        
        return True
        
    except Exception as e:
        print(f"❌ Lỗi: {e}")
        return False

if __name__ == "__main__":
    test_gemini() 