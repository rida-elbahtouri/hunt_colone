from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def singhup(request):
    if request.method =='POST':
        eror=""
        if request.POST['username']=="":
            eror +="username field is requered"
        if request.POST['password']=="":
            eror +="\npassword is empty"
        elif len(request.POST['password']) < 8:
            eror +="\n Make sure your password is at lest 8 letters"
        elif len(request.POST['password']) < 8 and  request.POST['password2']=="":
            eror +="please config password<br>"

        if eror =="":
            if request.POST['password']==request.POST['password2']:
                try:
                    user = User.objects.get(username=request.POST['username'])
                    return render(request,'account/singhup.html',{'eror':'\n username has been used before'})
                except User.DoesNotExist:
                    user=User.objects.create_user(request.POST['username'],password = request.POST['password'])
                    auth.login(request,user)
                    return redirect('home')
                else:
                    eror+="passwords does not match"
        if eror !="":
            return render(request,'account/singhup.html',{'eror':eror})


    else:
        return render(request,'account/singhup.html')
def login(request):
    if request.method =='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'account/login.html',{'eror':'username or password are wrong'})



    else:
       return render(request,'account/login.html')

def logout(request):
    if request.method =='POST':
        auth.logout(request)
        return redirect('home')
