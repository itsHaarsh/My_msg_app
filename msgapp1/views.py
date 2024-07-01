from django.shortcuts import render,HttpResponse,redirect
from django.views import View
#from message_app.models import Msg
from .models import Msg

# Create your views here.
def testing(request):
    return HttpResponse('hello linked successfully')

def create(request):
    if request.method=='POST':
        print("method is:",request.method)
        n=request.POST['uname']
        mail=request.POST['uemail']
        mob=request.POST['mobile']
        msg=request.POST['msg']
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()
        return redirect('/')
        #return HttpResponse("inserted data into database table")
    else:
        print("method is:",request.method)
    return render(request,'create.html')
def dashboard(request):
    m=Msg.objects.all()
    print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)  
    #return HttpResponse('Data Fetched from database')
    
def delete(request,rid):
    m=Msg.objects.filter(id=rid)
    m.delete()
    return redirect('/')
    #print('id to be deleted:',rid)
    #return HttpResponse('id to be deleted:'+rid)
    
def edit(request,rid):
    if request.method=='POST':
        pass
    else:
        m=Msg.objects.get(id=rid)
        print(m)
        context={}
        context['data']=m
        return render(request,'edit.html',context)