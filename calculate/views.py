from django.shortcuts import render
from django.views.generic import TemplateView
from .utility import Calculator

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        return render(request, 'index.html')
    
    def post(self, request):
        x = request.POST.get('x')
        y = request.POST.get('y')
        z = request.POST.get('z')

        result = Calculator.calculate(x, y, z)

        print(result)
        return render(request, 'result.html', {'original_values': {'x': x, 'y': y, 'z': z}, 'result': result})