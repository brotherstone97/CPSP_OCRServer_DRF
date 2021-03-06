## Environment
+ Python 3.9.7
+ Django 4.0.4
+ Django REST Framework 3.13.1
+ Pillow 9.1.0
+ django-cors-headers 3.13.0

## 주의사항
+ 최초 실행 전 ```python3 manage.py migrate``` 명령어 입력이 필요합니다.
+ 스크린샷이 저장되는 images 디렉토리는 runserver 시 존재유무 확인 후 자동 생성됩니다.
+ images폴더의 최대용량은 1GB입니다.
+ 사용자 업로드 이미지의 최대 용량은 50MB로 제한되며 이미지 최적화를 통해 다운사이징됩니다.
+ 단일 이미지 업로드만 가능하며 허용된 확장자명은 'png', 'jpg', 'jpeg'입니다.
+ 이미지 전송 시 key는 'file'이어야하며 enctype="multipart/form-data"이어야합니다.

## API Docs
### Method
method | URL
---|---
POST | [BaseURL]/screenshot/
GET | [BaseURL]/screenshot/files

### Parameter

key | value
---|---
file| image file(Required)

### Responses

case | response code
---|---|
성공|204: No Contents
업로드 이미지 용량초과(50MB) | 413: Payload Too Large
images폴더 용량 초과(1GB) | 413: Payload Too Large
Request에 파일이 생략된 경우 | 400: Bad Request

## Deployment
python3 manage.py runserver:```PORT```

example: python manage.py runserver:8080
