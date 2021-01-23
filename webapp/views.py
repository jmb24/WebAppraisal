from django.shortcuts import render


def default_view(request):
    return render(request, 'coming-soon.html')


def login_view(request):
    return render(request, 'coming-soon.html')


def create_account_view(request):
    return render(request, 'coming-soon.html')

