from django.shortcuts import render
from django.http import HttpResponse


ksiazki = [{'title': "w pustyni i w puszczy", "id": 1}, {'title': "rok 1984", "id": 2}]

def hello_world(request, name=""):
    if name:
        text = f"hello{name}"
    else:
        text = "hello world"
    return HttpResponse(text)

def lista_ksiazek(request):
    ksiazki = [{'title': "w pustyni i w puszczy"},{'title': "rok 1984"}]
    output = ""
    for k in ksiazki:
        output += k["title"] +"<br>"
    return HttpResponse(output)

def books_list(request, id):
      return render(
        request = request,
        template_name = "index.html",
        context = {"ksiazka": ksiazki}

    )
def books_details(request, id):
    ksiazka = ksiazki[id -1]
    return render(
        request = request,
        template_name = "index.html",
        context = {"ksiazka": ksiazki}
    )


# Create your views here.
