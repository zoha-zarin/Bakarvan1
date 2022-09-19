from django.shortcuts import render, redirect
from .models import davatModel, eskanModel, hamlonaghlModel, safarModel, karbarModel
from django.contrib import messages
from django.utils.crypto import get_random_string

# Create your views here.


def newSafar(request):
    unique_link = get_random_string(length=20)     # استرینگ رندوم برای ساخت لینک جوین
    unique_id = get_random_string(length=8)     # استرینگ رندوم برای ساخت کد سفر

    if request.method=='POST':    
        this_user = karbarModel.objects.filter(shomareMobile=request.user.username).first()  
        
        idChecker = safarModel.objects.none()       # این قسمت کد تا پایان حلقه وایل، برای تکراری نبودن کد سفر است
        idChecker = safarModel.objects.filter(kodeSafar = unique_id).first()
        while idChecker:
            unique_id = get_random_string(length=8)   
            idChecker = safarModel.objects.none()
            idChecker = safarModel.objects.filter(kodeSafar = unique_id).first() 
        
        new_davat = davatModel(linkeDavat ='http://127.0.0.1:8000/safar/join/' + unique_link +'/') # ساختن لینک جوین، با توجه به آدرس سرور باید تغییر کند  
        new_davat.save()

        new_safar = safarModel.objects.create(      # ساخت سفر با اطلاعات دریافت شده از فرم داخل اچ تی ام ال
        nameModir = this_user.name,
        nameKhanevadegiModir = this_user.nameKhanevadegi,
        shomareMobileModir = this_user.shomareMobile,
        nameSafar = request.POST['nameSafar'],
        kodeSafar = unique_id,
        mabda = request.POST['mabda'],
        maghsad = request.POST['maghsad'],
        tarikheShoru = request.POST['tarikheShoru'],
        tarikhePayan = request.POST['tarikhePayan'],
        davat = new_davat
        )   
        
        new_safar.save()
        messages.info(request,'ثبت شد')
    return render(request, 'newSafar.html')


def addDetail(request):
    if request.method=='POST':
        new_eskan = eskanModel(nameEskan = request.POST['nameEskan'])   # ثبت اطلاعات اسکان
        new_eskan.save()
        new_hamlonaghl = hamlonaghlModel(vasileNaghlie = request.POST['vasileNaghlie'])     # ثبت اطلاعات حمل و نقل
        new_hamlonaghl.save()
        safarModel.objects.filter(id=request.session.get('clicked_id')).update(     # آی دی کلیک شده از تابع قبلی دریافت میشود
            hamlonaghl = new_hamlonaghl,    # ثبت اسکان و حمل و نقل برای سفر کلیک شده
            eskan = new_eskan,
        )
        del request.session['clicked_id']   # حذف آی دی کلیک شده از سشن
        messages.info(request,'ثبت شد')
    return render(request, 'addDetail.html')
