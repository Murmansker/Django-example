from django.shortcuts import render
from django.http import HttpResponse

from .models import File
import os

def index(request):
    if request.method=='POST':   #判断是否为POST请求
        myFile=request.FILES.get('myfile',None)
        print(myFile)
        if not myFile:
            return HttpResponse('no file for index')
        f=open(os.path.join('D:/sword',myFile.name),'wb+')
        print(f)
        for chunk in myFile.chunks():  #分块写入文件
            print(chunk)
            f.write(chunk)
        f.close()
        return HttpResponse('index over')
    else:
        return render(request,'index.html')#请求方法为GET时候，生成文件上传页面
