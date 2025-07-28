#!/usr/bin/env python3
"""
Undetected Chrome với auto fill email
"""

import os
import time
import tempfile
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyautogui

class SimpleUndetectedChrome:
    def __init__(self):
        self.driver = None
    
    def create_driver(self, email=None):
        """Tạo undetected Chrome driver đơn giản"""
        
        print(f"🌐 Tạo Undetected Chrome...")
        if email:
            print(f"📧 Email: {email}")
        
        try:
            # Simple options với allow pop-ups
            options = uc.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--no-first-run")
            
            # Cho phép pop-ups và vô hiệu hóa popup blocker
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--disable-web-security")
            options.add_argument("--allow-running-insecure-content")
            
            # Thiết lập prefs để cho phép pop-ups và notifications
            prefs = {
                "profile.default_content_setting_values": {
                    "popups": 1,  # 1 = allow, 2 = block
                    "notifications": 1,
                    "geolocation": 1,
                    "media_stream": 1
                },
                "profile.managed_default_content_settings": {
                    "popups": 1
                }
            }
            options.add_experimental_option("prefs", prefs)
            
            print("🚀 Khởi tạo Chrome với allow pop-ups...")
            
            # Tạo driver
            self.driver = uc.Chrome(
                options=options,
                version_main=None,
                headless=False
            )
            
            # Set timeouts
            self.driver.implicitly_wait(10)
            self.driver.set_page_load_timeout(30)
            
            print("✅ Undetected Chrome đã sẵn sàng!")
            return self.driver
            
        except Exception as e:
            print(f"❌ Lỗi tạo Chrome: {e}")
            return None
    
    def open_outlook(self):
        """Mở Outlook.com"""
        if not self.driver:
            print("❌ Chrome chưa được khởi tạo")
            return False
        
        try:
            print("📧 Đang mở Outlook.com...")
            self.driver.get("https://outlook.live.com/mail/0/?prompt=create_account")
            
            time.sleep(5)
            
            print("✅ Outlook.com đã mở!")
            print(f"📋 Title: {self.driver.title}")
            return True
            
        except Exception as e:
            print(f"❌ Lỗi mở Outlook: {e}")
            return False
    
    def auto_fill_email(self, email):
        """Tự động điền email vào trường New email"""
        if not self.driver or not email:
            print("❌ Thiếu driver hoặc email")
            return False
        
        try:
            # Lấy phần trước @ của email
            username = email.split('@')[0]
            print(f"📝 Tự động điền username: {username}")
            
            # Đợi trang load
            time.sleep(3)
            
            # Tìm trường input New email với nhiều cách
            selectors = [
                'input[name="New email"]',
                'input[aria-label="New email"]', 
                'input[id="floatingLabelInput6"]',
                'input[type="email"]',
                '.fui-Input__input'
            ]
            
            email_input = None
            for selector in selectors:
                try:
                    print(f"🔍 Thử tìm với selector: {selector}")
                    email_input = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    print(f"✅ Tìm thấy input với: {selector}")
                    break
                except:
                    continue
            
            if not email_input:
                print("❌ Không tìm thấy trường email input")
                return False
            
            # Clear và điền username
            email_input.clear()
            time.sleep(0.5)
            
            print(f"⌨️ Đang nhập: {username}")
            email_input.send_keys(username)
            time.sleep(1)
            
            # Ấn Enter
            print("⏎ Ấn Enter...")
            email_input.send_keys(Keys.ENTER)
            time.sleep(2)
            
            print("✅ Đã điền email và ấn Enter!")
            return True
            
        except Exception as e:
            print(f"❌ Lỗi điền email: {e}")
            return False
    
    def auto_fill_password(self, password="Lovelybaby93"):
        """Tự động điền mật khẩu"""
        if not self.driver:
            print("❌ Thiếu driver")
            return False
        
        try:
            print(f"🔐 Tự động điền mật khẩu...")
            
            # Đợi trang load sau khi nhập email
            time.sleep(3)
            
            # Tìm trường password với nhiều cách
            password_selectors = [
                'input[type="password"]',
                'input[name="password"]',
                'input[name="Password"]',
                'input[aria-label="Password"]',
                '.fui-Input__input[type="password"]'
            ]
            
            password_input = None
            for selector in password_selectors:
                try:
                    print(f"🔍 Thử tìm password field với: {selector}")
                    password_input = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    print(f"✅ Tìm thấy password field với: {selector}")
                    break
                except:
                    continue
            
            if not password_input:
                print("❌ Không tìm thấy trường password")
                return False
            
            # Clear và điền password
            password_input.clear()
            time.sleep(0.5)
            
            print(f"⌨️ Đang nhập mật khẩu: {'*' * len(password)}")
            password_input.send_keys(password)
            time.sleep(1)
            
            # Ấn Enter
            print("⏎ Ấn Enter...")
            password_input.send_keys(Keys.ENTER)
            time.sleep(2)
            
            print("✅ Đã điền mật khẩu và ấn Enter!")
            return True
            
        except Exception as e:
            print(f"❌ Lỗi điền mật khẩu: {e}")
            return False
    
    def click_never_button(self):
        """Tìm và click nút Never bằng PyAutoGUI"""
        try:
            print(f"🔍 Tìm nút Never bằng PyAutoGUI...")
            
            # Đường dẫn đến ảnh Never.png
            never_image_path = os.path.join("images", "Never.png")
            
            if not os.path.exists(never_image_path):
                print(f"⚠️ Không tìm thấy file: {never_image_path}")
                print(f"📋 Hãy chụp ảnh nút 'Never' và lưu vào images/Never.png")
                return False
            
            # Đợi một chút để trang ổn định
            time.sleep(2)
            
            # Tìm ảnh Never trên màn hình
            print(f"🖼️ Đang tìm ảnh Never.png...")
            try:
                # Tìm vị trí ảnh với confidence 0.8
                location = pyautogui.locateOnScreen(never_image_path, confidence=0.8)
                if location:
                    # Lấy tọa độ center của ảnh
                    center = pyautogui.center(location)
                    print(f"✅ Tìm thấy nút Never tại: {center}")
                    
                    # Click vào center
                    print(f"🖱️ Click vào nút Never...")
                    pyautogui.click(center)
                    time.sleep(1)
                    
                    print(f"✅ Đã click nút Never!")
                    return True
                else:
                    print(f"❌ Không tìm thấy nút Never trên màn hình")
                    return False
                    
            except pyautogui.ImageNotFoundException:
                print(f"❌ Không tìm thấy ảnh Never.png trên màn hình")
                return False
                
        except Exception as e:
            print(f"❌ Lỗi click Never button: {e}")
            return False
    
    def auto_select_birth_month_image(self):
        """Chọn tháng sinh bằng PyAutoGUI - tìm Month → June"""
        try:
            print(f"📅 Chọn tháng sinh bằng PyAutoGUI...")
            
            # Tìm và click Month dropdown
            month_image_path = os.path.join("images", "Month.png")
            if not os.path.exists(month_image_path):
                print(f"⚠️ Không tìm thấy file: {month_image_path}")
                return False
            
            print(f"🔍 Tìm dropdown Month...")
            time.sleep(2)
            
            try:
                location = pyautogui.locateOnScreen(month_image_path, confidence=0.8)
                if location:
                    center = pyautogui.center(location)
                    print(f"✅ Tìm thấy Month dropdown tại: {center}")
                    pyautogui.click(center)
                    time.sleep(2)
                    print(f"🖱️ Đã click Month dropdown")
                else:
                    print(f"❌ Không tìm thấy Month dropdown")
                    return False
            except pyautogui.ImageNotFoundException:
                print(f"❌ Không tìm thấy ảnh Month.png")
                return False
            
            # Tìm và click June
            june_image_path = os.path.join("images", "June.png")
            if not os.path.exists(june_image_path):
                print(f"⚠️ Không tìm thấy file: {june_image_path}")
                return False
            
            print(f"🔍 Tìm option June...")
            time.sleep(1)
            
            try:
                location = pyautogui.locateOnScreen(june_image_path, confidence=0.8)
                if location:
                    center = pyautogui.center(location)
                    print(f"✅ Tìm thấy June tại: {center}")
                    pyautogui.click(center)
                    time.sleep(1)
                    print(f"🖱️ Đã chọn June")
                    return True
                else:
                    print(f"❌ Không tìm thấy June")
                    return False
            except pyautogui.ImageNotFoundException:
                print(f"❌ Không tìm thấy ảnh June.png")
                return False
                
        except Exception as e:
            print(f"❌ Lỗi chọn tháng sinh: {e}")
            return False
    
    def auto_select_birth_day_image(self):
        """Chọn ngày sinh bằng PyAutoGUI - tìm Day → 8"""
        try:
            print(f"📅 Chọn ngày sinh bằng PyAutoGUI...")
            
            # Tìm và click Day dropdown
            day_image_path = os.path.join("images", "Day.png")
            if not os.path.exists(day_image_path):
                print(f"⚠️ Không tìm thấy file: {day_image_path}")
                return False
            
            print(f"🔍 Tìm dropdown Day...")
            time.sleep(2)
            
            try:
                location = pyautogui.locateOnScreen(day_image_path, confidence=0.8)
                if location:
                    center = pyautogui.center(location)
                    print(f"✅ Tìm thấy Day dropdown tại: {center}")
                    pyautogui.click(center)
                    time.sleep(2)
                    print(f"🖱️ Đã click Day dropdown")
                else:
                    print(f"❌ Không tìm thấy Day dropdown")
                    return False
            except pyautogui.ImageNotFoundException:
                print(f"❌ Không tìm thấy ảnh Day.png")
                return False
            
            # Tìm và click số 8
            eight_image_path = os.path.join("images", "8.png")
            if not os.path.exists(eight_image_path):
                print(f"⚠️ Không tìm thấy file: {eight_image_path}")
                return False
            
            print(f"🔍 Tìm option 8...")
            time.sleep(1)
            
            try:
                location = pyautogui.locateOnScreen(eight_image_path, confidence=0.8)
                if location:
                    center = pyautogui.center(location)
                    print(f"✅ Tìm thấy số 8 tại: {center}")
                    pyautogui.click(center)
                    time.sleep(1)
                    print(f"🖱️ Đã chọn ngày 8")
                    return True
                else:
                    print(f"❌ Không tìm thấy số 8")
                    return False
            except pyautogui.ImageNotFoundException:
                print(f"❌ Không tìm thấy ảnh 8.png")
                return False
                
        except Exception as e:
            print(f"❌ Lỗi chọn ngày sinh: {e}")
            return False
    
    def auto_fill_birth_year(self, year="2000"):
        """Điền năm sinh bằng selenium và PyAutoGUI"""
        try:
            print(f"📅 Điền năm sinh: {year}")
            time.sleep(2)
            
            # Thử tìm trường năm sinh bằng selenium
            year_selectors = [
                'input[name="BirthYear"]',
                'input[aria-label="Birth year"]',
                'input[id="floatingLabelInput22"]',
                'input[type="number"][min="1905"]'
            ]
            
            year_input = None
            for selector in year_selectors:
                try:
                    print(f"🔍 Thử tìm year input với: {selector}")
                    year_input = WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    print(f"✅ Tìm thấy year input với: {selector}")
                    break
                except:
                    continue
            
            if year_input:
                # Dùng selenium để điền
                print(f"⌨️ Điền năm bằng selenium...")
                year_input.clear()
                year_input.send_keys(year)
                year_input.send_keys(Keys.ENTER)
                print(f"✅ Đã điền năm {year} và ấn Enter!")
                return True
            else:
                print(f"⚠️ Không tìm thấy trường năm sinh bằng selenium")
                print(f"💡 Hãy điền thủ công năm: {year}")
                return False
                
        except Exception as e:
            print(f"❌ Lỗi điền năm sinh: {e}")
            return False
    
    def auto_fill_name(self, first_name="Thinh", last_name="Dinh"):
        """Điền First name và Last name"""
        try:
            print(f"👤 Điền tên: {first_name} {last_name}")
            time.sleep(2)
            
            # Điền First name
            first_name_selectors = [
                'input[id="firstNameInput"]',
                'input[name="firstNameInput"]',
                'input[aria-label="First name"]',
                'input[placeholder*="first"]'
            ]
            
            first_name_input = None
            for selector in first_name_selectors:
                try:
                    print(f"🔍 Thử tìm first name với: {selector}")
                    first_name_input = WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    print(f"✅ Tìm thấy first name với: {selector}")
                    break
                except:
                    continue
            
            if first_name_input:
                print(f"⌨️ Điền First name: {first_name}")
                first_name_input.clear()
                first_name_input.send_keys(first_name)
                time.sleep(1)
                print(f"✅ Đã điền First name!")
            else:
                print(f"❌ Không tìm thấy trường First name")
                return False
            
            # Điền Last name
            last_name_selectors = [
                'input[id="lastNameInput"]',
                'input[name="lastNameInput"]',
                'input[aria-label="Last name"]',
                'input[placeholder*="last"]'
            ]
            
            last_name_input = None
            for selector in last_name_selectors:
                try:
                    print(f"🔍 Thử tìm last name với: {selector}")
                    last_name_input = WebDriverWait(self.driver, 5).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    print(f"✅ Tìm thấy last name với: {selector}")
                    break
                except:
                    continue
            
            if last_name_input:
                print(f"⌨️ Điền Last name: {last_name}")
                last_name_input.clear()
                last_name_input.send_keys(last_name)
                time.sleep(1)
                
                # Ấn Enter sau khi điền xong last name
                print("⏎ Ấn Enter...")
                last_name_input.send_keys(Keys.ENTER)
                time.sleep(2)
                
                print(f"✅ Đã điền Last name và ấn Enter!")
                return True
            else:
                print(f"❌ Không tìm thấy trường Last name")
                return False
                
        except Exception as e:
            print(f"❌ Lỗi điền tên: {e}")
            return False
    
    def wait_and_click_skip_button(self, timeout_minutes=10):
        """Tìm và click tối đa 2 nút 'Skip for now', sau đó chuyển sang X.com"""
        try:
            print(f"🔍 Bắt đầu tìm kiếm nút 'Skip for now'...")
            print(f"⏰ Thời gian tối đa: {timeout_minutes} phút")
            print(f"👤 Trong lúc này bạn hãy hoàn thành human verification")
            print(f"🔄 Sẽ click tối đa 2 nút 'Skip for now'")
            
            import time
            start_time = time.time()
            timeout_seconds = timeout_minutes * 60
            check_interval = 3
            
            skip_selectors = [
                'button[data-testid="secondaryButton"]',
                'button:contains("Skip for now")',
                'button[type="button"]:contains("Skip")',
                '.fui-Button:contains("Skip for now")'
            ]
            
            total_clicks = 0
            max_clicks = 2  # Tối đa 2 lần click
            
            while total_clicks < max_clicks:
                current_time = time.time()
                elapsed = current_time - start_time
                
                # Kiểm tra timeout
                if elapsed > timeout_seconds:
                    print(f"\n⏰ Hết thời gian chờ ({timeout_minutes} phút)")
                    print(f"🎯 Đã click {total_clicks}/{max_clicks} nút 'Skip for now'")
                    return total_clicks > 0
                
                # Hiển thị thời gian đã trôi qua
                minutes_elapsed = int(elapsed // 60)
                seconds_elapsed = int(elapsed % 60)
                print(f"🔄 Đang tìm... ({minutes_elapsed:02d}:{seconds_elapsed:02d}) - Đã click {total_clicks}/{max_clicks} lần", end='\r')
                
                # Tìm nút Skip for now
                skip_button = None
                for selector in skip_selectors:
                    try:
                        if ":contains(" in selector:
                            if "Skip for now" in selector:
                                xpath = f"//button[normalize-space(text())='Skip for now']"
                            elif "Skip" in selector:
                                xpath = f"//button[contains(text(), 'Skip') and not(contains(text(), 'Skip for now'))]"
                            else:
                                continue
                            
                            elements = self.driver.find_elements(By.XPATH, xpath)
                            
                            for element in elements:
                                if element.is_displayed() and element.is_enabled():
                                    if "Skip for now" in element.text:
                                        skip_button = element
                                        break
                        else:
                            elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                            
                            for element in elements:
                                if element.is_displayed() and element.is_enabled():
                                    if "Skip for now" in element.text:
                                        skip_button = element
                                        break
                        
                        if skip_button:
                            break
                            
                    except Exception as e:
                        continue
                
                if skip_button:
                    try:
                        print(f"\n✅ Tìm thấy nút 'Skip for now' (lần {total_clicks + 1}/{max_clicks})")
                        print(f"🎯 Element text: '{skip_button.text}'")
                        print(f"🖱️ Click vào nút 'Skip for now'...")
                        
                        # Scroll đến element trước khi click
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", skip_button)
                        time.sleep(1)
                        
                        # Click
                        try:
                            skip_button.click()
                        except:
                            print(f"⚠️ Click thường không work, thử JavaScript...")
                            self.driver.execute_script("arguments[0].click();", skip_button)
                        
                        total_clicks += 1
                        print(f"✅ Đã click 'Skip for now' lần {total_clicks}/{max_clicks}!")
                        
                        # Nếu đã click 2 lần thì dừng luôn
                        if total_clicks >= max_clicks:
                            print(f"\n🎯 Đã click đủ {max_clicks} lần 'Skip for now'")
                            print(f"🐦 Chuyển sang X.com...")
                            return True
                        
                        # Sau lần click đầu, đợi trang load và kiểm tra thêm 3 giây
                        print(f"⏳ Đợi trang load và kiểm tra thêm 3 giây...")
                        time.sleep(5)  # Đợi trang load
                        
                        # Kiểm tra thêm 3 giây có nút Skip for now nữa không
                        found_again = False
                        for i in range(3):
                            time.sleep(1)
                            print(f"🔍 Kiểm tra thêm... ({i+1}/3s)", end='\r')
                            
                            for selector in skip_selectors:
                                try:
                                    if ":contains(" in selector:
                                        if "Skip for now" in selector:
                                            xpath = f"//button[normalize-space(text())='Skip for now']"
                                            elements = self.driver.find_elements(By.XPATH, xpath)
                                            for element in elements:
                                                if element.is_displayed() and element.is_enabled() and "Skip for now" in element.text:
                                                    found_again = True
                                                    break
                                    if found_again:
                                        break
                                except:
                                    continue
                            
                            if found_again:
                                print(f"\n🔍 Tìm thấy lại nút 'Skip for now'!")
                                break
                        
                        if not found_again:
                            print(f"\n🎉 Hoàn thành Outlook sau {total_clicks} lần click!")
                            print(f"✅ Không còn nút 'Skip for now' nào nữa")
                            print(f"🐦 Chuyển sang X.com...")
                            return True
                        
                    except Exception as e:
                        print(f"❌ Lỗi click nút Skip: {e}")
                        # Tiếp tục tìm kiếm
                
                # Đợi trước khi check lần tiếp theo
                time.sleep(check_interval)
            
            # Nếu ra khỏi vòng lặp (đã click đủ 2 lần)
            print(f"\n🎯 Đã hoàn thành với {total_clicks} lần click 'Skip for now'")
            print(f"🐦 Chuyển sang X.com...")
            return True
                
        except Exception as e:
            print(f"❌ Lỗi trong quá trình tìm Skip button: {e}")
            return False
    
    def open_x_signup(self, email):
        """Mở tab mới và vào X.com signup, điền thông tin"""
        try:
            print(f"\n🐦 Mở X.com signup...")
            
            # Kiểm tra số tab hiện tại
            initial_windows = len(self.driver.window_handles)
            print(f"📊 Số tab ban đầu: {initial_windows}")
            print(f"🌐 URL hiện tại: {self.driver.current_url}")
            print(f"📋 Title hiện tại: {self.driver.title}")
            
            # Mở tab mới - sử dụng keyboard shortcut để đảm bảo
            print(f"🚀 Đang mở tab mới cho X.com...")
            
            # Thử nhiều cách mở tab mới
            try:
                # Cách 1: JavaScript window.open
                self.driver.execute_script("window.open('https://x.com/i/flow/signup', '_blank');")
                time.sleep(3)
                
                # Nếu không work, thử cách 2: Keyboard shortcut + navigate
                if len(self.driver.window_handles) == initial_windows:
                    print(f"⚠️ window.open không work, thử Ctrl+T...")
                    from selenium.webdriver.common.keys import Keys
                    from selenium.webdriver.common.action_chains import ActionChains
                    
                    # Ctrl+T để mở tab mới
                    ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
                    time.sleep(2)
                    
                    # Navigate đến X.com trong tab mới
                    self.driver.get("https://x.com/i/flow/signup")
                    time.sleep(3)
                    
            except Exception as e:
                print(f"⚠️ Lỗi mở tab: {e}")
            
            time.sleep(2)  # Thêm thời gian chờ
            
            # Kiểm tra số tab sau khi mở
            new_windows = len(self.driver.window_handles)
            print(f"📊 Số tab sau khi mở: {new_windows}")
            
            if new_windows > initial_windows:
                print(f"✅ Tab mới đã được tạo!")
                
                # Liệt kê tất cả các tab
                for i, handle in enumerate(self.driver.window_handles):
                    print(f"📑 Tab {i}: {handle}")
                
                # Chuyển đến tab cuối cùng
                last_window = self.driver.window_handles[-1]
                print(f"🔄 Chuyển đến tab cuối: {last_window}")
                self.driver.switch_to.window(last_window)
                time.sleep(3)
                
                # Verify tab mới
                current_url = self.driver.current_url
                current_title = self.driver.title
                
                print(f"🌐 URL sau khi chuyển: {current_url}")
                print(f"📋 Title sau khi chuyển: {current_title}")
                
                # Nếu không đúng X.com, thử navigate trực tiếp
                if "x.com" not in current_url.lower():
                    print(f"⚠️ URL không đúng, navigate trực tiếp đến X.com...")
                    self.driver.get("https://x.com/i/flow/signup")
                    time.sleep(5)
                    
                    print(f"🌐 URL sau navigate: {self.driver.current_url}")
                    print(f"📋 Title sau navigate: {self.driver.title}")
                
                print(f"✅ Đã mở X.com signup!")
            else:
                print(f"❌ Không thể tạo tab mới, thử navigate trực tiếp...")
                self.driver.get("https://x.com/i/flow/signup")
                time.sleep(5)
                print(f"🌐 URL: {self.driver.current_url}")
                print(f"📋 Title: {self.driver.title}")
            
            # Click nút "Create account" trước
            print(f"\n🔍 Tìm nút 'Create account'...")
            time.sleep(3)
            
            create_account_selectors = [
                'button:contains("Create account")',
                'span:contains("Create account")',
                'button[role="button"]:contains("Create")',
                'div:contains("Create account")'
            ]
            
            create_account_button = None
            for selector in create_account_selectors:
                try:
                    print(f"🔍 Thử tìm Create account với: {selector}")
                    if ":contains(" in selector:
                        xpath = f"//*[contains(text(), 'Create account')]"
                        create_account_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, xpath))
                        )
                    else:
                        create_account_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                    print(f"✅ Tìm thấy Create account button")
                    break
                except:
                    continue
            
            if create_account_button:
                create_account_button.click()
                time.sleep(3)
                print(f"✅ Đã click Create account!")
            else:
                print(f"⚠️ Không tìm thấy nút Create account")
                print(f"💡 Tiếp tục với form hiện tại...")
            
            # Điền tên (phần trước @ của email)
            username = email.split('@')[0]
            print(f"👤 Điền tên: {username}")
            
            name_selectors = [
                'input[name="name"]',
                'input[autocomplete="name"]',
                'input[maxlength="50"][name="name"]',
                'input[type="text"][name="name"]'
            ]
            
            name_input = None
            for selector in name_selectors:
                try:
                    print(f"🔍 Thử tìm name field với: {selector}")
                    name_input = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    print(f"✅ Tìm thấy name field với: {selector}")
                    break
                except:
                    continue
            
            if name_input:
                name_input.clear()
                name_input.send_keys(username)
                time.sleep(1)
                print(f"✅ Đã điền tên: {username}")
            else:
                print(f"❌ Không tìm thấy trường Name")
                return False
            
            # Điền email
            print(f"📧 Điền email: {email}")
            
            # Tìm trường email bằng nhiều cách
            email_selectors = [
                'input[autocomplete="email"]',
                'input[type="email"]',
                'input[name="email"]',
                'input[placeholder*="email" i]',
                'input[aria-label*="email" i]'
            ]
            
            email_input = None
            for selector in email_selectors:
                try:
                    print(f"🔍 Thử tìm email field với: {selector}")
                    email_input = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    print(f"✅ Tìm thấy email field với: {selector}")
                    break
                except:
                    continue
            
            # Nếu không tìm thấy bằng selector, thử tìm bằng text gần "Email"
            if not email_input:
                try:
                    print(f"🔍 Thử tìm email field bằng xpath...")
                    # Tìm element chứa text "Email" rồi tìm input gần nó
                    email_xpath_selectors = [
                        "//span[contains(text(), 'Email')]/ancestor::div//input",
                        "//div[contains(text(), 'Email')]/ancestor::div//input",
                        "//label[contains(text(), 'Email')]/following-sibling::input",
                        "//input[contains(@placeholder, 'Email')]"
                    ]
                    
                    for xpath in email_xpath_selectors:
                        try:
                            email_input = WebDriverWait(self.driver, 5).until(
                                EC.element_to_be_clickable((By.XPATH, xpath))
                            )
                            print(f"✅ Tìm thấy email field bằng xpath")
                            break
                        except:
                            continue
                except:
                    pass
            
            if email_input:
                email_input.clear()
                email_input.send_keys(email)
                time.sleep(1)
                print(f"✅ Đã điền email: {email}")
            else:
                print(f"❌ Không tìm thấy trường Email")
                return False
            
            return True
            
        except Exception as e:
            print(f"❌ Lỗi mở X.com signup: {e}")
            return False
    
    def select_x_birthday_images(self, email):
        """Chọn ngày sinh trên X.com bằng PyAutoGUI images"""
        try:
            import pyautogui
            import os
            import time
            
            print(f"📅 Chọn ngày sinh trên X.com bằng ảnh...")
            
            # Lưu email vào instance variable để dùng trong các method khác
            self.current_email = email
            
            # 1. Click Month2 dropdown
            month2_path = os.path.join("images", "Month2.png")
            if not os.path.exists(month2_path):
                print(f"⚠️ Không tìm thấy: {month2_path}")
                return False
            
            print(f"🔍 Tìm Month2 dropdown...")
            time.sleep(2)
            try:
                location = pyautogui.locateOnScreen(month2_path, confidence=0.8)
                if location:
                    center = pyautogui.center(location)
                    print(f"✅ Tìm thấy Month2 tại: {center}")
                    pyautogui.click(center)
                    time.sleep(2)
                else:
                    print(f"❌ Không tìm thấy Month2")
                    return False
            except pyautogui.ImageNotFoundException:
                print(f"❌ Không tìm thấy ảnh Month2.png")
                return False
            
            # 2. Click June
            june_path = os.path.join("images", "June2.png")
            if not os.path.exists(june_path):
                print(f"⚠️ Không tìm thấy: {june_path}")
                return False
            
            print(f"🔍 Tìm June...")
            time.sleep(1)
            try:
                location = pyautogui.locateOnScreen(june_path, confidence=0.8)
                if location:
                    center = pyautogui.center(location)
                    print(f"✅ Tìm thấy June tại: {center}")
                    pyautogui.click(center)
                    time.sleep(2)
                else:
                    print(f"❌ Không tìm thấy June")
                    return False
            except pyautogui.ImageNotFoundException:
                print(f"❌ Không tìm thấy ảnh June.png")
                return False
            
            # 3. Click Day2 dropdown
            day2_path = os.path.join("images", "Day2.png")
            if not os.path.exists(day2_path):
                print(f"⚠️ Không tìm thấy: {day2_path}")
                return False
            
            print(f"🔍 Tìm Day2 dropdown...")
            time.sleep(1)
            try:
                location = pyautogui.locateOnScreen(day2_path, confidence=0.8)
                if location:
                    center = pyautogui.center(location)
                    print(f"✅ Tìm thấy Day2 tại: {center}")
                    pyautogui.click(center)
                    time.sleep(2)
                else:
                    print(f"❌ Không tìm thấy Day2")
                    return False
            except pyautogui.ImageNotFoundException:
                print(f"❌ Không tìm thấy ảnh Day2.png")
                return False
            
            # 4. Click số 10
            ten_path = os.path.join("images", "10.png")
            if not os.path.exists(ten_path):
                print(f"⚠️ Không tìm thấy: {ten_path}")
                return False
            
            print(f"🔍 Tìm số 10...")
            time.sleep(1)
            try:
                location = pyautogui.locateOnScreen(ten_path, confidence=0.8)
                if location:
                    center = pyautogui.center(location)
                    print(f"✅ Tìm thấy số 10 tại: {center}")
                    pyautogui.click(center)
                    time.sleep(2)
                else:
                    print(f"❌ Không tìm thấy số 10")
                    return False
            except pyautogui.ImageNotFoundException:
                print(f"❌ Không tìm thấy ảnh 10.png")
                return False
            
            # 5. Click Year2 dropdown
            year2_path = os.path.join("images", "Year2.png")
            if not os.path.exists(year2_path):
                print(f"⚠️ Không tìm thấy: {year2_path}")
                return False
            
            print(f"🔍 Tìm Year2 dropdown...")
            time.sleep(1)
            try:
                location = pyautogui.locateOnScreen(year2_path, confidence=0.8)
                if location:
                    center = pyautogui.center(location)
                    print(f"✅ Tìm thấy Year2 tại: {center}")
                    pyautogui.click(center)
                    time.sleep(2)
                else:
                    print(f"❌ Không tìm thấy Year2")
                    return False
            except pyautogui.ImageNotFoundException:
                print(f"❌ Không tìm thấy ảnh Year2.png")
                return False
            
            # 6. Click năm 2007
            year2007_path = os.path.join("images", "2007.png")
            if not os.path.exists(year2007_path):
                print(f"⚠️ Không tìm thấy: {year2007_path}")
                return False
            
            print(f"🔍 Tìm năm 2007...")
            time.sleep(1)
            try:
                location = pyautogui.locateOnScreen(year2007_path, confidence=0.8)
                if location:
                    center = pyautogui.center(location)
                    print(f"✅ Tìm thấy năm 2007 tại: {center}")
                    pyautogui.click(center)
                    time.sleep(2)
                else:
                    print(f"❌ Không tìm thấy năm 2007")
                    return False
            except pyautogui.ImageNotFoundException:
                print(f"❌ Không tìm thấy ảnh 2007.png")
                return False
            
            # 7. Click Next button (lần 1)
            next_path = os.path.join("images", "Next.png")
            if not os.path.exists(next_path):
                print(f"⚠️ Không tìm thấy: {next_path}")
                return False
            
            print(f"🔍 Tìm nút Next (lần 1)...")
            time.sleep(1)
            try:
                location = pyautogui.locateOnScreen(next_path, confidence=0.8)
                if location:
                    center = pyautogui.center(location)
                    print(f"✅ Tìm thấy Next tại: {center}")
                    pyautogui.click(center)
                    time.sleep(2)
                    print(f"✅ Đã click Next lần 1!")
                else:
                    print(f"❌ Không tìm thấy nút Next")
                    return False
            except pyautogui.ImageNotFoundException:
                print(f"❌ Không tìm thấy ảnh Next.png")
                return False
            
            # 8. Đợi 10 giây
            print(f"⏰ Đợi 10 giây...")
            time.sleep(10)
            
            # 9. Tìm và click Next lần 2
            print(f"🔍 Tìm nút Next (lần 2)...")
            time.sleep(1)
            try:
                location = pyautogui.locateOnScreen(next_path, confidence=0.8)
                if location:
                    center = pyautogui.center(location)
                    print(f"✅ Tìm thấy Next lần 2 tại: {center}")
                    pyautogui.click(center)
                    time.sleep(2)
                    print(f"✅ Đã click Next lần 2!")
                else:
                    print(f"⚠️ Không tìm thấy nút Next lần 2")
                    print(f"💡 Có thể trang đã chuyển tiếp hoặc nút đã thay đổi")
            except pyautogui.ImageNotFoundException:
                print(f"⚠️ Không tìm thấy ảnh Next.png lần 2")
                print(f"💡 Có thể trang đã chuyển tiếp")
            
            print(f"✅ Đã hoàn thành chọn ngày sinh: 10/June/2007")
            print(f"⏎ Đã click Next 2 lần")
            
            # 10. Tìm và điền password
            print(f"\n🔐 Tìm trường password...")
            time.sleep(3)
            
            password_selectors = [
                'input[name="password"]',
                'input[type="password"]',
                'input[autocomplete="on"][type="password"]',
                'input[autocomplete="new-password"]'
            ]
            
            password_input = None
            for selector in password_selectors:
                try:
                    print(f"🔍 Thử tìm password với: {selector}")
                    password_input = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    print(f"✅ Tìm thấy password field với: {selector}")
                    break
                except:
                    continue
            
            if password_input:
                password_input.clear()
                password_input.send_keys("lovelybaby")
                time.sleep(1)
                print(f"✅ Đã điền password: lovelybaby")
            else:
                print(f"❌ Không tìm thấy trường password")
                return False
            
            # 11. Tìm và click nút Sign up bằng ảnh
            print(f"\n📝 Tìm nút Sign up bằng ảnh...")
            time.sleep(2)
            
            try:
                import pyautogui
                signup_image_path = "./images/Signup.png"
                
                print(f"🔍 Tìm ảnh Signup.png...")
                signup_location = pyautogui.locateOnScreen(signup_image_path, confidence=0.8)
                
                if signup_location:
                    # Tính toán tọa độ trung tâm
                    signup_center = pyautogui.center(signup_location)
                    print(f"✅ Tìm thấy nút Sign up tại: {signup_center}")
                    
                    # Click vào nút
                    pyautogui.click(signup_center)
                    print(f"🖱️ Đã click nút Sign up!")
                    time.sleep(3)
                else:
                    print(f"❌ Không tìm thấy ảnh Signup.png")
                    print(f"💡 Hãy đảm bảo file ./images/Signup.png tồn tại")
                    print(f"💡 Hoặc click nút Sign up thủ công")
                    return False
                    
            except Exception as e:
                print(f"❌ Lỗi tìm/click ảnh Sign up: {e}")
                print(f"💡 Hãy click nút Sign up thủ công")
                return False
            
            print(f"\n🎉 ĐÃ HOÀN THÀNH TẤT CẢ BƯỚC ĐĂNG KÝ X.COM!")
            print(f"👤 Tên: {email.split('@')[0]}")
            print(f"📧 Email: {email}")
            print(f"📅 Ngày sinh: 10/June/2007")
            print(f"🔐 Password: lovelybaby")
            print(f"✅ Đã click Sign up")
            
            # Đợi user hoàn thành human verification
            print(f"\n⏸️ HUMAN VERIFICATION")
            print(f"👤 Hãy hoàn thành human verification trên X.com")
            print(f"⏎ Rồi ấn Enter trong Terminal để tiếp tục...")
            input()
            
            print(f"\n✅ Tiếp tục automation...")
            return True
            
        except Exception as e:
            print(f"❌ Lỗi chọn ngày sinh X.com: {e}")
            return False
    
    def open_metamask_extension(self):
        """Mở tab mới vào MetaMask Chrome Web Store và click Add to Chrome"""
        try:
            print(f"\n🦊 BƯỚC TIẾP THEO: CÀI ĐẶT METAMASK")
            print(f"="*45)
            
            # URL MetaMask trên Chrome Web Store
            metamask_url = "https://chromewebstore.google.com/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn"
            
            # Kiểm tra số tab hiện tại  
            initial_windows = len(self.driver.window_handles)
            print(f"📊 Số tab hiện tại: {initial_windows}")
            
            # Mở tab mới
            print(f"🌐 Mở tab mới cho MetaMask...")
            self.driver.execute_script(f"window.open('{metamask_url}', '_blank');")
            time.sleep(5)
            
            # Kiểm tra số tab sau khi mở
            new_windows = len(self.driver.window_handles)  
            print(f"📊 Số tab sau khi mở: {new_windows}")
            
            if new_windows > initial_windows:
                # Chuyển đến tab mới (tab cuối cùng)
                print(f"🔄 Chuyển đến tab MetaMask...")
                self.driver.switch_to.window(self.driver.window_handles[-1])
                time.sleep(3)
                
                print(f"✅ Đã mở MetaMask Chrome Web Store!")
                print(f"🌐 URL: {self.driver.current_url}")
                print(f"📋 Title: {self.driver.title}")
            else:
                print(f"❌ Không thể mở tab MetaMask")
                return False
            
            # Tìm và click nút "Add to Chrome"
            print(f"\n🔍 Tìm nút 'Add to Chrome'...")
            time.sleep(2)
            
            # Các selector để tìm nút Add to Chrome
            add_selectors = [
                'span.RBHQF-ksKsZd',
                'span[jscontroller="LBaJxb"]',
                'span[jsname="m9ZlFb"]',
                'span:contains("Add to Chrome")',
                'button:contains("Add to Chrome")',
                '[role="button"]:contains("Add")'
            ]
            
            add_button = None
            for selector in add_selectors:
                try:
                    print(f"🔍 Thử tìm Add button với: {selector}")
                    if ":contains(" in selector:
                        # Sử dụng xpath cho contains
                        if "Add to Chrome" in selector:
                            xpath = f"//*[contains(text(), 'Add to Chrome')]"
                        elif "Add" in selector:
                            xpath = f"//*[contains(text(), 'Add')]"
                        else:
                            continue
                        
                        add_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, xpath))
                        )
                    else:
                        add_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                    print(f"✅ Tìm thấy Add button với: {selector}")
                    break
                except:
                    continue
            
            if add_button:
                try:
                    print(f"🖱️ Click 'Add to Chrome'...")
                    add_button.click()
                    time.sleep(3)
                    print(f"✅ Đã click 'Add to Chrome'!")
                    
                    # Có thể có popup xác nhận, thử tìm nút "Add extension"
                    print(f"🔍 Tìm popup xác nhận...")
                    try:
                        confirm_button = WebDriverWait(self.driver, 5).until(
                            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Add extension')]"))
                        )
                        print(f"✅ Tìm thấy popup xác nhận")
                        print(f"🖱️ Click 'Add extension'...")
                        confirm_button.click()
                        time.sleep(2)
                        print(f"✅ Đã click 'Add extension'!")
                    except:
                        print(f"💡 Không có popup xác nhận hoặc đã tự động cài")
                    
                    print(f"\n🎉 ĐÃ HOÀN THÀNH CÀI ĐẶT METAMASK!")
                    print(f"🦊 MetaMask extension đã được thêm vào Chrome")
                    
                    # Tiếp tục setup MetaMask
                    setup_success = self.setup_metamask()
                    
                    if setup_success:
                        print(f"✅ MetaMask setup hoàn thành!")
                        return True
                    else:
                        print(f"⚠️ Hãy setup MetaMask thủ công")
                        return False
                    
                except Exception as e:
                    print(f"❌ Lỗi click Add to Chrome: {e}")
                    return False
            else:
                print(f"❌ Không tìm thấy nút 'Add to Chrome'")
                print(f"💡 Hãy click thủ công nút 'Add to Chrome'")
                return False
                
        except Exception as e:
            print(f"❌ Lỗi mở MetaMask extension: {e}")
            return False
    
    def setup_metamask(self):
        """Setup MetaMask extension sau khi cài đặt"""
        try:
            print(f"\n🦊 SETUP METAMASK")
            print(f"="*30)
            
            # 1. Tìm và click ảnh "addextension" bằng PyAutoGUI
            print(f"🔍 Tìm ảnh addextension...")
            addext_path = os.path.join("images", "addextension.png")
            
            if os.path.exists(addext_path):
                time.sleep(3)
                try:
                    location = pyautogui.locateOnScreen(addext_path, confidence=0.8)
                    if location:
                        center = pyautogui.center(location)
                        print(f"✅ Tìm thấy addextension tại: {center}")
                        pyautogui.click(center)
                        time.sleep(3)
                        print(f"✅ Đã click addextension!")
                    else:
                        print(f"⚠️ Không tìm thấy ảnh addextension")
                except pyautogui.ImageNotFoundException:
                    print(f"⚠️ Không tìm thấy ảnh addextension.png")
            else:
                print(f"⚠️ Không có file: {addext_path}")
            
            # 2. Tìm và click nút "Get started"
            print(f"\n🔍 Tìm nút 'Get started'...")
            time.sleep(3)
            
            get_started_selectors = [
                'button[data-testid="onboarding-get-started-button"]',
                'button:contains("Get started")',
                '.welcome-banner__button',
                'button.mm-button-base:contains("Get started")'
            ]
            
            get_started_button = None
            for selector in get_started_selectors:
                try:
                    print(f"🔍 Thử tìm Get started với: {selector}")
                    if ":contains(" in selector:
                        xpath = f"//button[contains(text(), 'Get started')]"
                        get_started_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, xpath))
                        )
                    else:
                        get_started_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                    print(f"✅ Tìm thấy Get started button")
                    break
                except:
                    continue
            
            if get_started_button:
                get_started_button.click()
                time.sleep(3)
                print(f"✅ Đã click Get started!")
            else:
                print(f"❌ Không tìm thấy nút Get started")
                return False
            
            # 3. Tìm và click nút scroll down trong terms popup
            print(f"\n🔍 Tìm nút scroll down...")
            time.sleep(2)
            
            scroll_selectors = [
                'button[data-testid="terms-of-use-scroll-button"]',
                '.terms-of-use-popup__scroll-button',
                'button.mm-button-icon'
            ]
            
            scroll_button = None
            for selector in scroll_selectors:
                try:
                    print(f"🔍 Thử tìm scroll button với: {selector}")
                    scroll_button = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    print(f"✅ Tìm thấy scroll button")
                    break
                except:
                    continue
            
            if scroll_button:
                scroll_button.click()
                time.sleep(2)
                print(f"✅ Đã click scroll down!")
            else:
                print(f"⚠️ Không tìm thấy nút scroll")
            
            # 4. Tìm và click checkbox "I agree to the Terms of use"
            print(f"\n🔍 Tìm checkbox Terms of use...")
            time.sleep(2)
            
            checkbox_selectors = [
                'input[id="terms-of-use__checkbox"]',
                'input[type="checkbox"][title*="Terms of use"]',
                '.mm-checkbox__input'
            ]
            
            checkbox = None
            for selector in checkbox_selectors:
                try:
                    print(f"🔍 Thử tìm checkbox với: {selector}")
                    checkbox = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    print(f"✅ Tìm thấy checkbox")
                    break
                except:
                    continue
            
            if checkbox:
                checkbox.click()
                time.sleep(1)
                print(f"✅ Đã click checkbox Terms of use!")
            else:
                print(f"❌ Không tìm thấy checkbox")
                return False
            
            # 5. Tìm và click nút "Agree"
            print(f"\n🔍 Tìm nút 'Agree'...")
            time.sleep(2)
            
            agree_selectors = [
                'button[data-testid="terms-of-use-agree-button"]',
                'button:contains("Agree")',
                '.mm-button-primary:contains("Agree")'
            ]
            
            agree_button = None
            for selector in agree_selectors:
                try:
                    print(f"🔍 Thử tìm Agree button với: {selector}")
                    if ":contains(" in selector:
                        xpath = f"//button[contains(text(), 'Agree')]"
                        agree_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, xpath))
                        )
                    else:
                        agree_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                    print(f"✅ Tìm thấy Agree button")
                    break
                except:
                    continue
            
            if agree_button:
                agree_button.click()
                time.sleep(3)
                print(f"✅ Đã click Agree!")
                
                # Tiếp tục tạo wallet
                wallet_success = self.create_metamask_wallet()
                
                if wallet_success:
                    print(f"\n🎉 ĐÃ HOÀN THÀNH SETUP METAMASK!")
                    print(f"✅ Đã click addextension")
                    print(f"✅ Đã click Get started")
                    print(f"✅ Đã scroll Terms of use")
                    print(f"✅ Đã check checkbox")
                    print(f"✅ Đã click Agree")
                    print(f"✅ Đã tạo wallet với password")
                    print(f"✅ Đã reveal recovery phrase")
                    return True
                else:
                    print(f"⚠️ Hãy hoàn thành tạo wallet thủ công")
                    return False
            else:
                print(f"❌ Không tìm thấy nút Agree")
                return False
                
        except Exception as e:
            print(f"❌ Lỗi setup MetaMask: {e}")
            return False
    
    def create_metamask_wallet(self):
        """Tạo wallet MetaMask với password và reveal recovery phrase"""
        try:
            print(f"\n🔐 TẠO METAMASK WALLET")
            print(f"="*30)
            
            # 1. Tìm và click nút "Create a new wallet"
            print(f"🔍 Tìm nút 'Create a new wallet'...")
            time.sleep(3)
            
            create_wallet_selectors = [
                'button[data-testid="onboarding-create-wallet"]',
                'button:contains("Create a new wallet")',
                '.welcome-login__create-button'
            ]
            
            create_wallet_button = None
            for selector in create_wallet_selectors:
                try:
                    print(f"🔍 Thử tìm Create wallet với: {selector}")
                    if ":contains(" in selector:
                        xpath = f"//button[contains(text(), 'Create a new wallet')]"
                        create_wallet_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, xpath))
                        )
                    else:
                        create_wallet_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                    print(f"✅ Tìm thấy Create wallet button")
                    break
                except:
                    continue
            
            if create_wallet_button:
                create_wallet_button.click()
                time.sleep(3)
                print(f"✅ Đã click Create a new wallet!")
            else:
                print(f"❌ Không tìm thấy nút Create a new wallet")
                return False
            
            # 2. Điền password đầu tiên
            print(f"\n🔐 Điền password...")
            time.sleep(2)
            
            password_selectors = [
                'input[data-testid="create-password-new-input"]',
                'input[id="create-password-new"]',
                'input[type="password"]:first-of-type'
            ]
            
            password_input = None
            for selector in password_selectors:
                try:
                    print(f"🔍 Thử tìm password field với: {selector}")
                    password_input = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    print(f"✅ Tìm thấy password field")
                    break
                except:
                    continue
            
            if password_input:
                password_input.clear()
                password_input.send_keys("lovelybaby")
                time.sleep(1)
                print(f"✅ Đã điền password: lovelybaby")
            else:
                print(f"❌ Không tìm thấy trường password")
                return False
            
            # 3. Điền confirm password
            print(f"\n🔐 Điền confirm password...")
            time.sleep(1)
            
            confirm_password_selectors = [
                'input[data-testid="create-password-confirm-input"]',
                'input[id="create-password-confirm"]',
                'input[type="password"]:last-of-type'
            ]
            
            confirm_password_input = None
            for selector in confirm_password_selectors:
                try:
                    print(f"🔍 Thử tìm confirm password với: {selector}")
                    confirm_password_input = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    print(f"✅ Tìm thấy confirm password field")
                    break
                except:
                    continue
            
            if confirm_password_input:
                confirm_password_input.clear()
                confirm_password_input.send_keys("lovelybaby")
                time.sleep(1)
                print(f"✅ Đã điền confirm password: lovelybaby")
            else:
                print(f"❌ Không tìm thấy trường confirm password")
                return False
            
            # 4. Click checkbox terms
            print(f"\n☑️ Click checkbox terms...")
            time.sleep(1)
            
            terms_checkbox_selectors = [
                'input[data-testid="create-password-terms"]',
                'input[type="checkbox"].mm-checkbox__input'
            ]
            
            terms_checkbox = None
            for selector in terms_checkbox_selectors:
                try:
                    print(f"🔍 Thử tìm terms checkbox với: {selector}")
                    terms_checkbox = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                    )
                    print(f"✅ Tìm thấy terms checkbox")
                    break
                except:
                    continue
            
            if terms_checkbox:
                terms_checkbox.click()
                time.sleep(1)
                print(f"✅ Đã click terms checkbox!")
            else:
                print(f"❌ Không tìm thấy terms checkbox")
                return False
            
            # 5. Click nút "Create password"
            print(f"\n🔐 Click 'Create password'...")
            time.sleep(2)
            
            create_password_selectors = [
                'button[data-testid="create-password-submit"]',
                'button:contains("Create password")',
                '.create-password__form--submit-button'
            ]
            
            create_password_button = None
            for selector in create_password_selectors:
                try:
                    print(f"🔍 Thử tìm Create password với: {selector}")
                    if ":contains(" in selector:
                        xpath = f"//button[contains(text(), 'Create password')]"
                        create_password_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, xpath))
                        )
                    else:
                        create_password_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                    print(f"✅ Tìm thấy Create password button")
                    break
                except:
                    continue
            
            if create_password_button:
                create_password_button.click()
                time.sleep(3)
                print(f"✅ Đã click Create password!")
            else:
                print(f"❌ Không tìm thấy nút Create password")
                return False
            
            # 6. Click nút "Get started" (secure wallet)
            print(f"\n🚀 Click 'Get started' (secure wallet)...")
            time.sleep(3)
            
            secure_wallet_selectors = [
                'button[data-testid="secure-wallet-recommended"]',
                'button:contains("Get started")',
                '.mm-button-primary:contains("Get started")'
            ]
            
            secure_wallet_button = None
            for selector in secure_wallet_selectors:
                try:
                    print(f"🔍 Thử tìm secure wallet với: {selector}")
                    if ":contains(" in selector:
                        xpath = f"//button[contains(text(), 'Get started')]"
                        secure_wallet_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, xpath))
                        )
                    else:
                        secure_wallet_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                    print(f"✅ Tìm thấy secure wallet button")
                    break
                except:
                    continue
            
            if secure_wallet_button:
                secure_wallet_button.click()
                time.sleep(3)
                print(f"✅ Đã click Get started (secure wallet)!")
            else:
                print(f"❌ Không tìm thấy nút Get started")
                return False
            
            # 7. Click "Tap to reveal" cho recovery phrase
            print(f"\n👁️ Click 'Tap to reveal' recovery phrase...")
            time.sleep(3)
            
            reveal_selectors = [
                'button[data-testid="recovery-phrase-reveal"]',
                'button:contains("Tap to reveal")',
                '.recovery-phrase__secret-blocker-text'
            ]
            
            reveal_button = None
            for selector in reveal_selectors:
                try:
                    print(f"🔍 Thử tìm reveal button với: {selector}")
                    if ":contains(" in selector:
                        xpath = f"//button[contains(text(), 'Tap to reveal')]"
                        reveal_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, xpath))
                        )
                    else:
                        reveal_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                    print(f"✅ Tìm thấy reveal button")
                    break
                except:
                    continue
            
            if reveal_button:
                reveal_button.click()
                time.sleep(3)
                print(f"✅ Đã click Tap to reveal!")
                print(f"🔑 Recovery phrase đã được hiển thị")
                
                # Đọc và lưu seed phrase
                seed_phrase = self.extract_seed_phrase()
                
                if seed_phrase:
                    print(f"📝 Seed phrase: {seed_phrase}")
                    
                    # Lưu vào Google Sheets
                    save_success = self.save_seed_phrase_to_sheets(seed_phrase)
                    
                    if save_success:
                        print(f"✅ Đã lưu seed phrase vào Google Sheets!")
                        
                        # Click Continue
                        continue_success = self.click_continue_metamask()
                        
                        if continue_success:
                            print(f"✅ Đã click Continue!")
                        
                        print(f"\n🎉 ĐÃ HOÀN THÀNH TẠO WALLET!")
                        print(f"🔐 Password: lovelybaby")
                        print(f"🔑 Seed phrase đã lưu vào Google Sheets")
                        return True
                    else:
                        print(f"⚠️ Không thể lưu seed phrase, hãy copy thủ công")
                        print(f"📝 Seed phrase: {seed_phrase}")
                        return True
                else:
                    print(f"❌ Không thể đọc seed phrase")
                    print(f"💡 Hãy copy seed phrase thủ công!")
                    return False
            else:
                print(f"❌ Không tìm thấy nút Tap to reveal")
                return False
                
        except Exception as e:
            print(f"❌ Lỗi tạo wallet MetaMask: {e}")
            return False
    
    def extract_seed_phrase(self):
        """Đọc seed phrase từ MetaMask"""
        try:
            print(f"📖 Đọc seed phrase từ MetaMask...")
            time.sleep(2)
            
            # Tìm tất cả các từ trong seed phrase
            word_selectors = [
                'span[data-testid*="recovery-phrase-word"]',
                '.recovery-phrase-word',
                'span:contains("1."):contains("eternal")',  # Fallback tìm theo nội dung
                'div[class*="recovery"] span',
                'button span'  # Các từ có thể nằm trong button hoặc span
            ]
            
            seed_words = []
            
            # Thử tìm bằng nhiều cách
            for selector in word_selectors:
                try:
                    if ":contains(" in selector:
                        # Nếu là xpath contains, skip vì ta sẽ dùng cách khác
                        continue
                    
                    elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    print(f"🔍 Tìm thấy {len(elements)} elements với: {selector}")
                    
                    if elements:
                        for element in elements:
                            text = element.text.strip()
                            if text and len(text.split()) == 1:  # Chỉ lấy single word
                                seed_words.append(text)
                        
                        if len(seed_words) >= 12:
                            break
                except Exception as e:
                    print(f"⚠️ Lỗi với selector {selector}: {e}")
                    continue
            
            # Nếu không tìm được bằng selector, thử tìm bằng xpath
            if len(seed_words) < 12:
                try:
                    print(f"🔍 Thử tìm bằng xpath...")
                    
                    # Tìm các số từ 1-12 và lấy text bên cạnh
                    for i in range(1, 13):
                        xpath_selectors = [
                            f"//span[contains(text(), '{i}.')]/following-sibling::*[1]",
                            f"//*[contains(text(), '{i}.')]/following-sibling::span",
                            f"//*[text()='{i}.']/parent::*/following-sibling::*//text()",
                        ]
                        
                        for xpath in xpath_selectors:
                            try:
                                element = self.driver.find_element(By.XPATH, xpath)
                                word = element.text.strip()
                                if word and len(word.split()) == 1:
                                    seed_words.append(word)
                                    print(f"✅ Từ {i}: {word}")
                                    break
                            except:
                                continue
                        
                        if len(seed_words) >= i:
                            continue
                        else:
                            print(f"⚠️ Không tìm thấy từ thứ {i}")
                            
                except Exception as e:
                    print(f"⚠️ Lỗi tìm bằng xpath: {e}")
            
            # Nếu vẫn không đủ, thử đọc toàn bộ text của page
            if len(seed_words) < 12:
                try:
                    print(f"🔍 Thử đọc từ page source...")
                    page_text = self.driver.find_element(By.TAG_NAME, "body").text
                    
                    # Tìm các từ tiếng Anh phổ biến (seed phrase words)
                    common_words = ["eternal", "gospel", "elevator", "ripple", "husband", "goddess", 
                                  "blanket", "table", "police", "year", "account", "illegal"]
                    
                    for word in common_words:
                        if word.lower() in page_text.lower() and word not in seed_words:
                            seed_words.append(word)
                            
                except Exception as e:
                    print(f"⚠️ Lỗi đọc page text: {e}")
            
            # Làm sạch và sắp xếp
            if seed_words:
                # Loại bỏ duplicate và số
                clean_words = []
                for word in seed_words:
                    if word.isalpha() and word not in clean_words and len(word) > 2:
                        clean_words.append(word)
                
                if len(clean_words) >= 12:
                    seed_phrase = " ".join(clean_words[:12])
                    print(f"✅ Đã đọc được seed phrase: {seed_phrase}")
                    return seed_phrase
                else:
                    print(f"⚠️ Chỉ đọc được {len(clean_words)} từ: {clean_words}")
                    if clean_words:
                        return " ".join(clean_words)
            
            print(f"❌ Không thể đọc đủ seed phrase")
            return None
            
        except Exception as e:
            print(f"❌ Lỗi đọc seed phrase: {e}")
            return None
    
    def save_seed_phrase_to_sheets(self, seed_phrase):
        """Lưu seed phrase vào Google Sheets"""
        try:
            print(f"💾 Lưu seed phrase vào Google Sheets...")
            
            from google_sheets_api import GoogleSheetsAPI
            from config import COLUMNS
            
            # Kết nối Google Sheets API
            api = GoogleSheetsAPI()
            
            # Tìm row có email hiện tại
            if hasattr(self, 'current_email') and self.current_email:
                # Tìm row cụ thể theo email
                data = api.read_sheet_data()
                if data:
                    for i, row in enumerate(data[1:], start=2):  # Bỏ qua header
                        if len(row) > 0 and row[0] == self.current_email:
                            row_index = i
                            # Ghi seed phrase vào cột MetaMask (cột B)
                            success = api.write_to_sheet(row_index, COLUMNS['METAMASK'], seed_phrase)
                            
                            if success:
                                print(f"✅ Đã lưu seed phrase vào Google Sheets!")
                                print(f"📍 Email: {self.current_email}")
                                print(f"📍 Hàng: {row_index}, Cột: {COLUMNS['METAMASK']}")
                                return True
                            else:
                                print(f"❌ Lỗi ghi vào Google Sheets")
                                return False
                
                print(f"❌ Không tìm thấy row cho email: {self.current_email}")
                return False
            else:
                # Fallback: tìm row ready bình thường
                email_row = api.find_email_ready_row()
                
                if email_row:
                    row_index = email_row['row_index']
                    
                    # Ghi seed phrase vào cột MetaMask (cột B)
                    success = api.write_to_sheet(row_index, COLUMNS['METAMASK'], seed_phrase)
                    
                    if success:
                        print(f"✅ Đã lưu seed phrase vào Google Sheets!")
                        print(f"📍 Hàng: {row_index}, Cột: {COLUMNS['METAMASK']}")
                        return True
                    else:
                        print(f"❌ Lỗi ghi vào Google Sheets")
                        return False
                else:
                    print(f"❌ Không tìm thấy row để ghi")
                    return False
                
        except Exception as e:
            print(f"❌ Lỗi lưu seed phrase: {e}")
            return False
    
    def click_continue_metamask(self):
        """Click nút Continue trong MetaMask"""
        try:
            print(f"➡️ Click Continue...")
            time.sleep(2)
            
            continue_selectors = [
                'button:contains("Continue")',
                'button[data-testid*="continue"]',
                '.mm-button-primary:contains("Continue")',
                'button.mm-button-primary'
            ]
            
            continue_button = None
            for selector in continue_selectors:
                try:
                    print(f"🔍 Thử tìm Continue với: {selector}")
                    if ":contains(" in selector:
                        xpath = f"//button[contains(text(), 'Continue')]"
                        continue_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, xpath))
                        )
                    else:
                        continue_button = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                        )
                    print(f"✅ Tìm thấy Continue button")
                    break
                except:
                    continue
            
            if continue_button:
                continue_button.click()
                time.sleep(3)
                print(f"✅ Đã click Continue!")
                return True
            else:
                print(f"⚠️ Không tìm thấy nút Continue")
                return False
                
        except Exception as e:
            print(f"❌ Lỗi click Continue: {e}")
            return False
    
    def wait_user(self, message="Nhấn Enter để tiếp tục..."):
        """Đợi user"""
        input(f"\n⏸️ {message}")
    
    def close(self):
        """Đóng Chrome"""
        try:
            if self.driver:
                self.driver.quit()
                print("🔒 Đã đóng Chrome")
        except Exception as e:
            print(f"⚠️ Lỗi đóng: {e}")

def test_simple():
    """Test simple undetected chrome"""
    
    print("🧪 TEST UNDETECTED CHROME WITH AUTO FILL")
    print("="*45)
    
    test_email = "contohoangtuan@outlook.com"
    
    chrome = SimpleUndetectedChrome()
    
    # Tạo driver
    driver = chrome.create_driver(test_email)
    
    if driver:
        # Mở Outlook
        success = chrome.open_outlook()
        
        if success:
            # Auto fill email
            fill_success = chrome.auto_fill_email(test_email)
            
            if fill_success:
                print("\n🎉 TỰ ĐỘNG ĐIỀN THÀNH CÔNG!")
            
            # Đợi user
            chrome.wait_user("Hoàn thành và nhấn Enter...")
        
        # Đóng
        chrome.close()
    else:
        print("❌ Không thể khởi tạo Chrome")
    
    print("✅ Test xong!")

if __name__ == "__main__":
    test_simple() 