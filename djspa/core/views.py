from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.response import Response


def home(request):
    return render(request, 'app_shell.html')


@api_view(['GET', 'POST'])
def return_data(request):

    return Response({'name': 'augusto'})
