from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView

from BEDOLAGA_SITE.forms.forns import CreateUserForm
from phonestore.models import Ad


def login_page(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response = redirect('home')
                response.set_cookie('username', username)
                response.set_cookie('login_status', True)

                return response
            else:
                messages.info(request, 'Credentials are incorrect')

        context = {}
        return render(request, 'login.html', context)


def registration_page(request: HttpRequest):
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('user_login')
    context = {'form': form, }
    return render(request, 'registration.html', context)


def logout_user(request: HttpRequest):
    logout(request)
    messages.success(request, 'Successful logout')
    response = redirect('user_login')
    response.delete_cookie('username')
    response.delete_cookie('login_status')
    return response


def about_page(request: HttpRequest):
    return render(request, 'about.html', {})


class HomeView(ListView):
    model = Ad
    template_name = 'home.html'
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if 'login_status' in self.request.COOKIES and 'username' in self.request.COOKIES:
            context.update({
                'username': self.request.COOKIES['username'],
                'login_status': self.request.COOKIES['login_status'],
            })
            return context
        else:
            return context


class AdDetailedView(DetailView):
    model = Ad
    template_name = 'ad_details.html'
