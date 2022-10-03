from email.message import Message
from genericpath import exists
from django.shortcuts import render, redirect

from home.models import Jewelry
from .models import Bead, Rig, RigImage, Decor
# Create your views here.

def creator(request):
    
    page = "rigs"
    rigs = Rig.objects.all()
    images = RigImage.objects.all()
    
    if request.method == 'POST':
        request.session['rigs_color'] = request.POST.get('rigs_color')
        return redirect('/creator/beads')
    
    
    context = {'rigs': rigs, 'images':images, 'page': page}
    
    return render(request, 'creator/creator.html', context)

def beads(request):
    
    page = "beads"
    
    id = request.session.get('rigs_color')
    if id == '':
        return redirect('/creator/rigs')
    
    rigimages = RigImage.objects.filter(id=id)
    beads = Bead.objects.all()
     

    context = {'rigimages':rigimages, 'page': page, 'beads':beads}
    
    return render(request, 'creator/creator.html', context)

def decor(request):
    
    page = "decor"
    
    decor = Decor.objects.all()
    boxes = decor.filter(type=1)
    bags = decor.filter(type=2)
    cards = decor.filter(type=3)
    
    
    if request.method == 'POST':
        request.session['rigs_color'] = request.POST.get('rigs_color')
        return redirect('/creator/beads')
    
    
    context = {'boxes': boxes, 'bags':bags, 'page': page, 'cards':cards}
    
    return render(request, 'creator/creator.html', context)