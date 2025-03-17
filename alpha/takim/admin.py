from django.contrib import admin
from .models import Takim,Sporcu,Antrenman,Ozellikler,HaftalikAntrenman,Yarislar,Barajlar
# Register your models here.

admin.site.register(Takim)
admin.site.register(Sporcu)
admin.site.register(Antrenman)
admin.site.register(Ozellikler)
admin.site.register(HaftalikAntrenman)
admin.site.register(Yarislar)
admin.site.register(Barajlar)