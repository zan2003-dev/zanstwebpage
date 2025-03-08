from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>My name is zanst and this is my website / Django project, created with  only using cmd and pycharm</h1>")