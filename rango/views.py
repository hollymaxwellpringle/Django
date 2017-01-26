from django.shortcuts import render


from django.http import HttpResponse

def index(request):
    return HttpResponse ("Rango says hey there partner here is the link! <br/> <a href = '/rango/about/'> About</a>")
def about(request):
    return HttpResponse("Rango says is the about page")

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request, 'rango/index.html', context=context_dict)
