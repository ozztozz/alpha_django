from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Takim,Sporcu,Antrenman,Ozellikler
from .forms import FormTakim,FormSporcu,FormAntrenman

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
       print(form)
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

