from django.shortcuts import render, HttpResponse
from .models import Vacancy
# Create your views here.
def homepage(request):
    return render(request=request, template_name="index.html")

def about(request):
    return HttpResponse("Найдите работу или работника мечты!")

def contact_view(request):
    return HttpResponse('''
        <div>
            Phone: +996777123456 <br>
            Email: kaium@gmail.com
        </div>
    
    ''')
def address(request):
    return  HttpResponse('''
        <ul>
            <li>г. Бишкек, 7 м-н, 26/1</li>
            <li>г. Ош, Черемушка, дом 235 </li>
        </ul>    
    ''')

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    context = {"vacancies": vacancies}
    return render(request, 'vacancies.html', context)

