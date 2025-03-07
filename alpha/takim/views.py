from django.shortcuts import render,redirect,get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Takim,Sporcu,Antrenman,Yarislar,HaftalikAntrenman,DAY_OF_WEEKS_CHOICES
from .forms import FormTakim,FormSporcu,FormAntrenman
from datetime import  time, datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def base(request):
    return render(request,'base.html')

def takim_list(request):
    takim_list=Takim.objects.all()
    return render(request,'takim_list.html',{'takim_list':takim_list})

@login_required
def takim_ekle(request):
   if request.method == "POST":
       form = FormTakim(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('takim_list')  # Adjust this to your post list view
   else:
       form = FormTakim()
   return render(request, 'takim_ekle.html', {'form': form})

@login_required
def takim_guncelle(request,id):
    takim = get_object_or_404(Takim, id = id)
    if request.method == 'POST':
        post=request.POST
        if request.FILES == None:
            post = request.POST.copy() # to make it mutable
            post['resim'] = takim.resim
        form=FormTakim(post,request.FILES,instance=takim)
    
        if form.is_valid():
            form.save()
            return redirect('takim_list') 

    form = FormTakim(instance = takim)
    return render(request, "takim_ekle.html", {'form':form,'takim':takim})

def sporcu_list(request):
    sporcu_list=Sporcu.objects.all()
    return render(request,'sporcu_list.html',{'sporcu_list':sporcu_list})

@login_required
def sporcu_ekle(request):
   if request.method == "POST":
       form = FormSporcu(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('sporcu_list')  # Adjust this to your post list view
   else:
       form = FormSporcu()
   return render(request, 'sporcu_ekle.html', {'form': form})

@login_required
def sporcu_guncelle(request,id):
    sporcu = get_object_or_404(Sporcu, id = id)
    if request.method == 'POST':
        post=request.POST
        post = request.POST.copy() # to make it mutable
        if request.FILES == None:
            post['resim'] = sporcu.resim

        
        form=FormSporcu(post,request.FILES,instance=sporcu)
    
        if form.is_valid():
            form.save()
            return redirect('sporcu_list') 

    form = FormSporcu(instance = sporcu)
    return render(request, "sporcu_ekle.html", {'form':form,'sporcu':sporcu})



def antrenman_list(request):
    antrenman_list=Antrenman.objects.all()
    return render(request,'antrenman_list.html',{'antrenman_list':antrenman_list})


@login_required
def antrenman_ekle(request):
   if request.method == "POST":
       form = FormAntrenman(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('antrenman_list')  # Adjust this to your post list view
   else:
       form = FormAntrenman()
       
   return render(request, 'antrenman_ekle.html', {'form': form})


@login_required
def antrenman_guncelle(request,id):
    antrenman = get_object_or_404(Antrenman, id = id)
    if request.method == 'POST':
        post=request.POST        
        form=FormAntrenman(post,instance=antrenman)
    
        if form.is_valid():
            form.save()
            return redirect('antrenman_list') 

    form = FormAntrenman(instance = antrenman)
    return render(request, "antrenman_ekle.html", {'form':form,'antrenman':antrenman})

def haftalik_antrenman(request):
    haftalik_list=HaftalikAntrenman.objects.all().order_by('dayofweek',)
    haftalik_nested={}
    for gun in DAY_OF_WEEKS_CHOICES:
        haftalik_nested[gun[1]]={'sabah':[],'aksam':[]}
    
    for antrenman in haftalik_list:
        gunluk=haftalik_nested.get(antrenman.get_dayofweek_display())
        donem= 'sabah' if antrenman.baslangic < time(13,00) else 'aksam'
        gunluk[donem].append(antrenman)
        
    print(haftalik_nested)    
    return render(request,'haftalik_antrenman.html',{'haftalik_list':haftalik_list,
                                                     'haftalik_nested':haftalik_nested})

def antrenman_yap(request):

    return render (request,'antrenman.html')
    gun=datetime.today().weekday()
    gun+=1
    gunluk_antrenman=HaftalikAntrenman.objects.filter(dayofweek=gun)
    return render(request,'antrenman.html',{'gunluk_antrenman':gunluk_antrenman})


def gunluk_ekle(request):
    takim_id=int(request.POST.get('antrenman'))
    takim=get_object_or_404(Takim,id=takim_id)
    yeni_antrenman=Antrenman()
    yeni_antrenman.save()
    yeni_antrenman.takimlar.add(takim)
    sporcu_list=Sporcu.objects.filter(takim=takim_id)
    response=render_to_string('sporcu_antrenman.html',{'sporcu_list':sporcu_list,'antrenman':yeni_antrenman})
    return HttpResponse(response)

@csrf_exempt
def htmx_sporcu_ekle(request):
    sporcu_id=int(request.POST.get('sporcu'))
    ekle_cikar=request.POST.get('ekle_cikar')
    print(ekle_cikar)
    sporcu_tek=get_object_or_404(Sporcu,id=sporcu_id)
    response=render_to_string('sporcu_antrenman.html',{'sporcu_tek':sporcu_tek,
                                                       'ekle_cikar':ekle_cikar})
    return HttpResponse(response)

def yaris_list(request):
    yaris_list=Yarislar.objects.all()
    return render(request,'yaris_list.html',{'yaris_list':yaris_list})
