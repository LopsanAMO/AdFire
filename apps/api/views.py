from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Api

class Home(View):
    def get(self, request):
        template_name = 'index.html'
        return render(request, template_name)

    def post(self, request):
        init_date = request.POST.get('init')
        final = request.POST.get('final')
        image = request.FILES.get('archivo')
        api = Api()
        api.name = "hasfsa"
        api.publication_file = image
        api.date = init_date
        api.final_date = final
        api.type = "hola"
        api.save()
        return redirect('/')


class Test(View):
    def get(self, request):
        template_name = 'test.html'
        return render(request, template_name)
