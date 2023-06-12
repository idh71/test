import os
from dotenv import load_dotenv

def test_func():
    load_dotenv()
    secret_code = os.environ.get('SECRET_CODE')
    extra_secret_code = os.environ.get('EXTRA_SECRET_CODE')

    print(secret_code, extra_secret_code)

test_func()