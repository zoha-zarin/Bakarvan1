from django.db import models
from datetime import datetime


# Create your models here.

    
class hamlonaghlModel(models.Model):
    vasileNaghlie = models.CharField(max_length=50)
    zamaneRaft = models.CharField(max_length=50, null=True)
    zamaneBargasht = models.CharField(max_length=50, null=True)
    tozihat = models.CharField(max_length=500, null=True)

class eskanModel(models.Model):
    noeEskan = models.CharField(max_length=50, null=True)
    nameEskan = models.CharField(max_length=50)
    nahveEskan = models.CharField(max_length=50, null=True)
    adres = models.CharField(max_length=500, null=True)
    tozihat = models.CharField(max_length=500, null=True)

class davatModel(models.Model):
    tarikheEngheza = models.CharField(max_length=50,null=True)
    linkeDavat = models.CharField(max_length=50)
    matneDavat = models.CharField(max_length=500, null=True)

class javazModel(models.Model):
    javaz = models.CharField(max_length=50, null=True)
    tozihat = models.CharField(max_length=50, null=True)


class safarModel(models.Model):
    nameModir = models.CharField(max_length=50)
    nameKhanevadegiModir = models.CharField(max_length=50, null=True)
    shomareMobileModir = models.CharField(max_length=14, null=False, blank=False, unique=True)
    nameSafar = models.CharField(max_length=50)
    kodeSafar = models.CharField(max_length=8)
    noeSafar = models.CharField(max_length=50, null=True)
    mabda = models.CharField(max_length=50)
    maghsad = models.CharField(max_length=50)
    tarikheIjad = models.CharField(max_length=50,default=datetime.now)
    tarikheShoru = models.CharField(max_length=50) 
    tarikhePayan = models.CharField(max_length=50)
    moddat = models.CharField(max_length=10, null=True)
    profileSafar = models.FileField(null=True)
    hamlonaghl = models.OneToOneField(hamlonaghlModel, on_delete=models.CASCADE, null=True)
    eskan = models.OneToOneField(eskanModel, on_delete=models.CASCADE, null=True)
    javazHamrahan = models.OneToOneField(javazModel, on_delete=models.CASCADE, null=True)
    davat = models.OneToOneField(davatModel, on_delete=models.CASCADE)


class karbarModel(models.Model):
    JENSIAT_CHOICES = (
    ("آقا", "آقا"),
    ("خانم", "خانم"),
    )   

    jensiat = models.CharField(max_length=9,
                  choices=JENSIAT_CHOICES,
                  default="آقا")

    name = models.CharField(max_length=50)
    nameKhanevadegi = models.CharField(max_length=50, null=True)
    shomareMobile = models.CharField(max_length=14, null=False, blank=False, unique=True)
    safarePazirofte = models.ManyToManyField(safarModel, related_name='accepted')   # سفرهایی که مسافر در آن پذیرفته شده
    safareRadkarde = models.ManyToManyField(safarModel, related_name='denied')  # سفرهایی که مسافر دعوت را نپذیرفته
    safareTasmimNagerefteh = models.ManyToManyField(safarModel, related_name='hanging') # سفرهایی که ماسفر هنوز درباره دعوت تصمیم نگرفته (نه رد کرده نه قبول)
    safareDarEntezareTayid = models.ManyToManyField(safarModel, related_name='waiting')    # سفرهای در انتظار تایید مدیر
    safareRadshode = models.ManyToManyField(safarModel, related_name='rejected')      # سفرهای که مدیر این مسافر را از پیوستن به آن منع کرده
    safareMotevajehShode = models.ManyToManyField(safarModel, related_name='understood')  # اعلان این که "مدیر سفر تقاضای پیوستن به سفرت را نپذیرفت" را قبلا دیده شده