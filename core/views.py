from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("hi")

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
