from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import regiter,rstr

# Create your views here.
def sr (request):
   return HttpResponse("name")

def odd (request,num):

    if num == 0:
        return HttpResponse("enter a valid number")
    elif(num % 2) == 0:
    
        return HttpResponse("%d is even "%num)
    else:
        return HttpResponse(" %d is odd "%num)
    
def str (request,n):
      a = n[::-1]
      return HttpResponse(a)
  
def abc(request,n,m):
      c =m+n
      return HttpResponse(c)
  
def index(request):
    return render(request,'index.html')

def ind(request):
    return render(request,'index1.html')

def vowel(request, v):
    vowels = ["a", "e", "i", "o", "u"]
    if v in vowels:
        return HttpResponse("%s is a vowel" % v)
    else:
        return HttpResponse("%s is not a vowel" % v)
    
def indo(request):
    if request.method == 'POST':
        frst=request.POST['fname']
        lst=request.POST['lname']
        phn=request.POST['phone_number']  
        email=request.POST['email']   
        password=request.POST['psw'] 
        data=regiter.objects.create(firstname=frst,lastname=lst,phonenumber=phn,email=email,password=password)
        data.save()     
        return HttpResponse('sucessfull')
    else :
        return render(request,'index3.html')
    
    
def ind_4(request):
    if request.method == 'POST':
        sclnm=request.POST['sname']
        dst=request.POST['Dict']
        adrss=request.POST['adrs']
        phone=request.POST['phn_no']
        email=request.POST['email']
        pswd=request.POST['psw']
        data =rstr.objects.create(schlname=sclnm,district=dst,address=adrss,phoneno=phone,email=email, password=pswd)
        data.save()
        return redirect(rgr)
    else :
        return render(request,'index4.html')
    
def rgr(request):
    a=rstr.objects.all()
    return render(request,'indexl.html',{'abc':a})
    
def search(request):
    if request.method == 'POST':
        data = request.POST['schoolname']
        a = rstr.objects.filter(schlname=data)
        return render(request,'indexl.html',{'abc':a})
    else:
            return render(request,'indexl.html')
        
def deleteschool(request,id):
    da = rstr.objects.get(id=id)
    da.delete()
    return redirect(rgr)

def editschool(request,id):
    di= rstr.objects.get(id=id)
    if request.method =='POST':
        di.schlname=request.POST['sname']
        di.district=request.POST['Dict']
        di.address=request.POST['adrs']
        di.phoneno=request.POST['phn_no']
        di.email=request.POST['email']
        di.password=request.POST['psw']
        di.save()
        return redirect(rgr)
    else:
        return render(request,'index5.html',{'data':di})