from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home (request):
    text ="""<h1> "Изучаем Django"</h1>
            <strong> Author </strong> : <i>Жамалетдинов Т.Р.</i>
          """
    return HttpResponse(text)