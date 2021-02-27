from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request, 'generator/index.html')

def about(request):
    return render(request,'generator/about.html')
def password(request):

    length = int(request.GET.get('length', 4))
    randomPass = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()-+:;'))

    for i in range(length):
       randomPass += random.choice(characters)
    

    return render(request, 'generator/password.html', {'password': randomPass})