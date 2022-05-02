from django.shortcuts import render
from .models import Screenshot
# from rest_framework.request import Request
#
# request = Request()
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework.response import Response


@csrf_exempt
def upload_screenshot(request):
    if request.method == 'POST':
        if not request.FILES:
            print("files not exist")
            return
        ss = Screenshot()
        ss.image = request.FILES.values()
        # print('ss.image: ' + str(ss.image))
        ss.save()
    return Response(status=200)
