from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return  render(request, 'home.html')
def cheak(request):
    hii = request.POST.get('text', 'default')
    # print(hii)
    cheak = request.POST.get('check', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # analized = hii

    if (cheak == 'on'):
        puntuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analized = ""
        for char in hii:
            if char not in puntuation:
                analized = analized + char
        ana = {"purpose": "remove pantuation", "analizedtext": analized}
        return render(request, 'cheak.html', ana)
    elif uppercase == 'on':
        letter = ""
        pantuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in hii:
            if char not in pantuation:
                letter = letter + char.upper()
        upper = {'purpose': 'upper_case', 'uppercaseletter': letter}
        return render(request, 'cheak.html', upper)
    elif extraspaceremover == 'on':
        letter = ""
        for index, char in enumerate(hii):
            if  hii[index] == " " and hii[index+1] == " ":
                pass
            else:
                letter = letter + char
        upper = {'purpose': 'upper_case', 'space': letter}
        return render(request, 'cheak.html', upper)

    else:
        return HttpResponse('error')
