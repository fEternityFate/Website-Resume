from django.shortcuts import render


def Home(request):
    return render(request, 'Home.html')


def Contacts(request):
    return render(request, 'Contacts.html')
