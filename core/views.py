from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from core.forms import RegisterForm
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password


def homepage(request):
    # return HttpResponse("homepage")
    return render(request, 'base.html')

# def register(request): 
#     # return HttpResponse("hi")
#     return render(request, 'register.html')

def user_login(request):
    # return HttpResponse("k")
    return render(request, 'user_login.html')

def user_page(request):
    # return HttpResponse("p")
    return render(request, 'user_page.html')


#FormView is generic class based view (see "generic editing views" in docs)for when you want valid form to perform certain action. 
class RegisterView(FormView):

    def get(self, request):
        content = {}
        content['form'] = RegisterForm
        return render(request, 'register.html', content)

    def post(self, request):
        content = {}
        form = RegisterForm(request.POST, request.FILES or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect(reverse('dashboard-view'))
        content['form'] = form
        template = 'register.html'
        return render(request, template, content)


