from django.shortcuts import render,redirect
from django.http import HttpResponse

def nav_home(request):

    return render(request,'nav/nav.html',{})

def search(request):
    if request.method == 'POST':
        data=request.POST
        kw=data.get('kw')
        if 'baidu' in data:
            url = f"https://www.baidu.com/s?wd={kw}"
        else:
            url = f"https://www.google.com/search?q={kw}"
        return redirect(url)
    else:
        return HttpResponse('仅接受POST请求')
