from builtins import print

from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from .forms import *

from .models import *

menu = [{'title': 'Главная', 'url_name': 'home'},
        {'title': "Турнирная таблица", 'url_name': 'table'},
        {'title': "Войти", 'url_name': 'input'},
]
menu2 = [{'title': 'Главная', 'url_name': 'home'},
        {'title': "Судейство", 'url_name': 'juds'},
        {'title': "Турнирная таблица", 'url_name': 'table'},
        {'title': "Выйти", 'url_name': 'logout'},
]
# Create your views here.
def index(request):
    posts = Comand.objects.all()
    cats = Category.objects.all()
    judjs = Judj.objects.all()
    context = {
        'judjs': judjs,
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'menu2': menu2,
        'title': 'Главная',
        'cat_selected': 0,
    }
    return render(request, 'minin/index.html', context=context)

def judging(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Comand.objects.filter(title__icontains=search_query)
    else:
        posts = Comand.objects.all()

    cats = Category.objects.all()
    judjs = Judj.objects.all()
    context = {
        'judjs': judjs,
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'menu2': menu2,
        'title': 'Главная',
        'cat_selected': 0,
    }
    return render(request, 'minin/judging.html', context=context)

def table(request):
    posts = Comand.objects.all()
    cats = Category.objects.all()
    judjs = Judj.objects.all()
    itog1 = Comand.objects.all()[0:1]
    itog2 = Comand.objects.all()[1:2]
    itog3 = Comand.objects.all()[2:3]
    context = {
        'itog1': itog1,
        'itog2': itog2,
        'itog3': itog3,
        'judjs': judjs,
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'menu2': menu2,
        'title': 'Главная',
        'cat_selected': 0,
    }
    return render(request, 'minin/turnir.html', context=context)



def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

def show_category(request, cat_id):
    posts = Comand.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    judjs = Judj.objects.all()
    users = User.objects.all()
    context = {
        'users': users,
        'judjs': judjs,
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'menu2': menu2,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }
    return render(request, 'minin/index.html', context=context)

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        users = User.objects.all()
        context['users'] = users
        context['menu'] = menu
        context['menu2'] = menu2
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'minin/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class NewsUpdateView(DataMixin, UpdateView):
    model = Comand
    template_name = 'minin/update.html'

    form_class = ComandForm
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

def LogoutUser(request):
    logout(request)
    return redirect('input')




