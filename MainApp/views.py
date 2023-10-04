from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseNotFound


items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
]

def home (request):
    text ="""<h1> "Изучаем Django"</h1>
            <strong> Author </strong> : <i>Жамалетдинов Т.Р.</i>
          """
    return HttpResponse(text)

def about (request):
    message = """ Имя: <strong>Тимур</strong><br>
               Отчество:<strong> Жамалетдинов</strong><br>
               Фамилия:<strong> Жамалетдинов</strong><br>
               телефон:<strong> 8-9</strong><br>
               email: <strong>tim.@mail.ru</strong><br>
        """
    return HttpResponse(message)

def get_item(request,id):
    """ возвращает имя и кол во по ид"""
    for item in items:
        if item ["id"]==id:
            result = f"""
            <h2>Имя:{item["name"]}</h2>
            <p> Количество{item["quantity"]}</p>
            """
            return HttpResponse(result)
    return HttpResponseNotFound (f'item whith id = {id} not found')

def items_list(request):
    result= '<h2> Список товаров<h2><ol>'
    for item in items:
        result +=f"""<li><a href="/item/{item["id"]}">{item['name']}</a></li>"""
    result+="<ol>"
    return HttpResponse(result)
