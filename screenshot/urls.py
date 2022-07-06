from django.urls import path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_screenshot
from .views import get_screenshot

urlpatterns = [
    path('', upload_screenshot),
    path('files', get_screenshot)
]
urlpatterns += static(settings.SCREENSHOT_URL, document_root=settings.SCREENSHOT_ROOT)

