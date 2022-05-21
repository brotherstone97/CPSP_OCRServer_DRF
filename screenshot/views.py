from django.shortcuts import render
from .models import Screenshot

from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
@csrf_exempt
#스크린샷 업로드 기능을 수행하는 함수
def upload_screenshot(request):
    if request.method == 'POST':
        if not request.FILES:
            print("files not exist")
            return
        image_dict = request.FILES
        for value in image_dict.getlist('files'):
            print(f'value.size: {value.size / 1000000}mb ')
            # 50mb이하의 파일로 제한
            if value.size < 52428800:
                # 확장자 제한(png, jpg, jpeg)
                if '.png' in str(value) or '.jpg' in str(value) or '.jpeg' in str(value):
                    print(value)
                    ss = Screenshot()
                    ss.image = value
                    ss.save()
                    #reducing quality

                else:
                    print("value's type: ", type(str(value)))
                    print("value: ", value)
                    print("this file isn't contain png | jpg | jpeg")
            else:
                print("50mb 초과")

    return Response(status=204)
