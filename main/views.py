from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import Feedback


def form(request):

    return render(request, 'main/form.html')


def index(request):
    
    error = ''
    if request.method == 'POST':
        form = Feedback(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма неверна'



    form = Feedback
    data = {
        'form' : form
    }
    return render(request, 'main/index.html', data)

# def feedback(request):
#     return render(request, 'main/feedback.html')

