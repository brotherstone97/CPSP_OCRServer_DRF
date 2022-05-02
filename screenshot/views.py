from django.shortcuts import render
from .models import Screenshot

from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
@csrf_exempt
def upload_screenshot(request):
    if request.method == 'POST':
        if not request.FILES:
            print("files not exist")
            return
        image_dict = request.FILES
        print(image_dict)
        for value in image_dict.getlist('files'):
            ss = Screenshot()
            ss.image = value
            ss.save()
    return Response(data={
        'message': 'Success',
    })
