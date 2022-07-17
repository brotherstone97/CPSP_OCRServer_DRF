from django.urls import path
# from .views import upload_screenshot
# from .views import get_screenshot
from .views import ScreenshotAPI
from .views import get_static_images

urlpatterns = [
    # post = 스크린샷 업로드  get = images폴더 내 이미지 파일 리스트 출력
    path('', ScreenshotAPI.as_view()),
    # 저장된 이미지 접근
    path('<str:name>', get_static_images),
]