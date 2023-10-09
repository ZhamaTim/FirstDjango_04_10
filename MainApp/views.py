from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseNotFound

author = {
    "Имя" : "Тимур",
    "Отчество":"Ренатович",
    "Фамилия":"Жамалетдинов",
    "телефон":"8968",
    "email":"my.mail@gmail.com"
}



items = [
{"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
{"id": 2, "name": "Куртка кожаная" ,"quantity":2},
{"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
{"id": 7, "name": "Картофель фри" ,"quantity":0},
{"id": 8, "name": "Кепка" ,"quantity":124},
]

def main(request):
    return render(request,'index.html')

def home (request):
    #text ="""<h1> "Изучаем Django"</h1>
            #<strong> Author </strong> : <i>Жамалетдинов Т.Р.</i>
          #"""
          context = {
               "name":"ZhamTim",
               "email":"my.mail@gmail.com"
            }
          return render (request, 'index.html',context ) 

def about (request):
    message = f""" Имя: <b> {author["Имя"]} </b><br>
               Отчество:<strong> {author["Отчество"]}</strong><br>
               Фамилия:<strong> {author["Фамилия"]}</strong><br>
               телефон:<strong> {author["телефон"]}</strong><br>
               email: <strong>{author["email"]}</strong><br>
        """
    return HttpResponse(message)

def get_item(request, item_id):
    """ По указанному id возвращает имя и количество """
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        context = {
            "item": item
        }
        return render(request, "item-page.html", context)
    return HttpResponseNotFound(f'Item with id={id} not found')
   

def items_list(request):
    #result= '<h2> Список товаров<h2><ol>'
    #for item in items:
    #    result +=f"""<li><a href="/item/{item["id"]}">{item['name']}</a></li>"""
    #result+="<ol>"
    #return HttpResponse(result)
    context = {
         "items":items
        
    }
    return render ( request, "items-list.html", context)