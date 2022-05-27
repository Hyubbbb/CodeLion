from django.shortcuts import redirect, render
from django.contrib import auth # 로그인 기능을 제공해주는 녀석
from django.contrib.auth.models import User # createsuperuser처럼 id pwd 저장해주는 내장 기능


def login(request):
    # POST 요청이 들어오면 로그인 처리
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html') # badlogin.html 과 같은 html을 추가로 생성해서 "존재하지 않는 계정입니다"와 같은 것도 가능



    # GET 요청이 들어오면 login from을 담고 있는 login.html을 띄워줘
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
