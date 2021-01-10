from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from core.forms import RegisterForm, LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.shortcuts import render_to_response
from core.models import Questions, Answers, QuestionGroups


def homepage(request):
    # return HttpResponse("homepage")
    return render(request, 'homepage.html')

def user_page(request):
    return render(request, 'user_page.html')


#FormView is generic class based view (see "generic editing views" in docs)for when you want valid form to perform certain action. 
class Register(FormView):

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
            return redirect(reverse('homepage'))
        content['form'] = form
        template = 'register.html'
        return render(request, template, content)

class Homepage(FormView):

    def get(self, request):
        content = {}
        if request.user.is_authenticated:
            user = request.user
            user.backend = 'django.contrib.core.backends.ModelBackend'
            ques_obj = Questions.objects.filter(user=user)
            content['userdetail'] = user
            content['questions'] = ques_obj
            ans_obj = Answers.objects.filter(question=ques_obj[0])
            content['answers'] = ans_obj
            return render(request, 'homepage.html', content)
        else:
            return redirect(reverse('login'))

class Login(FormView):

    content = {}
    content['form'] = LoginForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Login, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        content = {}
        if request.user.is_authenticated:
            return redirect(reverse('homepage'))
        content['form'] = LoginForm
        return render(request, 'login.html', content)

    def post(self, request):
        content = {}
        email = request.POST['email']
        password = request.POST['password']
        try:
            users = User.objects.filter(email=email)
            user = authenticate(request, username=users.first().username, password=password)
            login(request, user)
            return redirect(reverse('homepage'))
        except Exception as e:
            content = {}
            content['form'] = LoginForm
            content['error'] = 'Unable to login with provided credentials' + e
            return render_to_response('login.html', content)


class Logout(FormView):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


