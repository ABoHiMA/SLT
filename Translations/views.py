from django.shortcuts import render
# from django.http import HttpResponseRedirect
from .models import Image

# Create your views here.

def translate(request):
    letters = request.GET.get('letters', '')
    images = Image.objects.filter(letter__in=letters)
    context = {'images': images}
    if images:
        context['letter'] = images[0].letter
    return render(request, 'Translations/Trans.html', context)    
