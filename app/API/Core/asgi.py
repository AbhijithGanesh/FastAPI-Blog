from logging import debug
import os
import uvicorn
from Blogs.main import app
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Core.settings')

application = get_asgi_application()



app = app 