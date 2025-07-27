import os
from dotenv import load_dotenv

load_dotenv()

# Google Sheets Configuration
GOOGLE_SHEETS_CREDENTIALS_FILE = 'credentials.json'
GOOGLE_SHEETS_TOKEN_FILE = 'token.json'
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID', '')
SHEET_NAME = 'Onefootball Club'  # Tên sheet chứa dữ liệu tài khoản

# Chrome Configuration  
CHROME_PROFILES_DIR = './chrome_profiles'
CHROME_EXECUTABLE_PATH = None  # Auto detect

# Columns in Google Sheets (theo cấu trúc thật của sheet)
COLUMNS = {
    'EMAIL': 'A',         # Email 
    'METAMASK': 'B',      # Metamask wallet
    'TWITTER': 'C',       # Twitter username
    'STATUS_X': 'D',      # Tình trạng X
    'DONE': 'E'           # Done?
}

# URLs
OUTLOOK_SIGNUP_URL = 'https://outlook.live.com/owa/'
TWITTER_SIGNUP_URL = 'https://twitter.com/signup'
METAMASK_DOWNLOAD_URL = 'https://metamask.io/download/'

# Delays (seconds)
DELAYS = {
    'SHORT': 2,
    'MEDIUM': 5, 
    'LONG': 10,
    'VERY_LONG': 30
} 