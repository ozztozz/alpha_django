from django.db import models
from main.models import Antrenor

# Create your models here.


class Takim (models.Model):
    adi=models.CharField(max_length=30)
    antrenor=models.ManyToManyField(Antrenor)
    resim=models.ImageField(null=True,blank=True)
    aktif=models.BooleanField(default=True)
    def __str__(self):
        return self.adi

class Sporcu (models.Model):
    adi=models.CharField(max_length=30)
    soyadi=models.CharField(max_length=30)
    anne=models.CharField(max_length=30)
    baba=models.CharField(max_length=30)
    dogum_tarihi=models.DateField()
    okulu=models.CharField(max_length=30)
    resim=models.ImageField(upload_to='media/')
    telefon=models.CharField(max_length=10)
    telefon_veli=models.CharField(max_length=10)
    aktif=models.BooleanField(default=True)
    takim=models.ForeignKey(Takim,on_delete=models.CASCADE)
    def __str__(self):
        return self.adi +' '+ self.soyadi

class Ozellikler(models.Model):
    boy=models.IntegerField()
    kilo=models.IntegerField()
    tarih=models.DateField(auto_now_add=True)
    sporcu=models.ForeignKey(Sporcu,on_delete=models.CASCADE)


DAY_OF_WEEKS_CHOICES = (
    (0, "Pazar"),
    (1,"Pazartesi"),
    (2,"Sali"),
    (3,"Carsamba"),
    (4,"Persembe"),
    (5,"Cuma"),
    (6,"Cumartesi"),
  
)
ANTRENMAN_YERI = (
    ('Hacettepe', "Hacettepe"),
    ('Atlas', "Atlas"),
)
ANTRENMAN_TURU = (
    ('Yüzme', "Yüzme"),
    ('Kara', "Kara"),
)
class HaftalikAntrenman(models.Model):
    dayofweek=models.IntegerField(choices=DAY_OF_WEEKS_CHOICES)
    baslangic=models.TimeField()
    bitis=models.TimeField(null=True)
    takim=models.ForeignKey(Takim,on_delete=models.CASCADE)
    yer=models.TextField(choices=ANTRENMAN_YERI,null=True)
    tur=models.TextField(choices=ANTRENMAN_TURU,null=True)
  
    def __str__(self):
        return str(self.dayofweek)

class Antrenman(models.Model):
    gun=models.DateField()
    takimlar=models.ManyToManyField(Takim)
    sporcular=models.ManyToManyField(Sporcu,null=True,blank=True)
    mesafe=models.IntegerField()

    class Meta:
        ordering=['-gun']
