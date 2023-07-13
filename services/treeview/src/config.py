import os


class Config:
    OLFYI_HOST = os.getenv('OLFYI_HOST', 'db.0l.fyi')
    OLFYI_PORT = os.getenv('OLFYI_PORT', 80)
    OLFYI_USERNAME = os.getenv('OLFYI_USERNAME', 'ol')
    OLFYI_PASSWORD = os.getenv('OLFYI_PASSWORD', '869cf751355b4f4b397606f2b3e398c6')
    OLFYI_DATABASE = os.getenv('OLFYI_DATABASE', 'olfyi')
    DATA_PATH = os.getenv('DATA_PATH', '')
