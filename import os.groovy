import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# مسارات الملفات
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
TRANSCRIPT_FOLDER = os.path.join(BASE_DIR, 'transcriptions')

# اللغات المدعومة
LANGUAGES = {
    'ar': 'العربية',
    'en': 'English',
    'fr': 'Français',
    'ja': '日本語',
    'ko': '한국어',
    'vi': 'Tiếng Việt'
}

# إعدادات Flask
SECRET_KEY = 'your-secret-key'  # غيّره بمفتاح قوي
SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/speechwise.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
