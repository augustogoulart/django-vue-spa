from django.shortcuts import render


def home(request):
    return render(request, 'app_shell.html')