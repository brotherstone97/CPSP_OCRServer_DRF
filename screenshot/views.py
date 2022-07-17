from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView

from .models import Screenshot

from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view
import os

from .image_preprocessing import reduce_size
from .handle_file_system import dir_size

# images폴더의 용량 제한을 1GB로 설정함.
LIMIT_IMAGE_FOLDER = 1024 ** 3


class ScreenshotAPI(APIView):
    # 스크린샷 업로드 기능을 수행하는 함수
    def post(self, request):
        # images폴더의 용량 제한을 1GB로 설정함.
        if dir_size('media/images') >= LIMIT_IMAGE_FOLDER:
            print("images directory size is fulled.")
            return Response(status=413)
        # request의 FILES가 존재하지 않는 경우 return
        if not request.FILES:
            print("files not exist")
            return Response(status=400)
        # 전송받은 file
        image_dict = request.FILES
        # 전송 시 key값은 'file'이어야함
        file = image_dict.get('file')
        print(f'value.size: {file.size / (50 * 1024 * 1024)}mb')
        # 50mb이하의 파일로 제한
        if file.size < 50 * 1024 * 1024:
            # 확장자 제한(png, jpg, jpeg)
            file_extensions = ['.png', '.jpg', '.jpeg']
            is_allowed_extension = [file_extension in str(file) for file_extension in file_extensions]
            if True in is_allowed_extension:
                print(file)
                ss = Screenshot()
                ss.image = file
                # image/temp에 임시저장
                ss.save()
                # reducing size
                # temp내 이미지 optimizing 후 상위폴더에 이미지 재저장
                reduce_size('media/images/temp/', 'media/images/', filename=file)
                # 모델에 저장된 record 삭제(모델을 이미지 파일 저장용도로 사용하고 db로 사용하지 않기 위함)
                ss.delete()
            else:
                print("value's type: ", type(str(file)))
                print("value: ", file)
                print("this file isn't contain png | jpg | jpeg")
                return Response(status=400)
        else:
            print("50mb 초과")
            return Response(status=413)
        return Response(status=204)

    def get(self, request):
        images_dir = 'media/images/'
        images = os.listdir(images_dir)

        images.remove('temp')

        return Response(status=200, data=images)


# 저장된 이미지 접근하는 함수
@api_view(['GET'])
@csrf_exempt
def get_static_images(request, name):
    # query param
    # file_name = request.GET['name']
    with open(f'media/images/{name}', 'rb') as f:
        return HttpResponse(f.read(), content_type='image/jpeg')
