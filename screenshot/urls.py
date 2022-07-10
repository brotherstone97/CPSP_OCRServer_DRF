from django.urls import path
from .views import upload_screenshot
from .views import get_screenshot
from .views import get_static_images

urlpatterns = [
    # 스크린샷 업로드
    path('', upload_screenshot),
    # images폴더 내 이미지 파일 리스트 출력
    path('files', get_screenshot),
    # 저장된 이미지 접근
    path('images', get_static_images)
]