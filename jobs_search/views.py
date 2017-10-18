from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Annonce
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class IndexView(generic.ListView):

    template_name = "jobs_search/index.html"
    context_object_name = "all_annonces"
    paginate_by = 3

    def get_queryset(self):

        return Annonce.objects.order_by('-date')


class DetailView (generic.DetailView):

    model = Annonce
    context_object_name = 'annonce'
    template_name = 'jobs_search/detail.html'


# @method_decorator(login_required, name='dispatch')
class CreateAnnonce(CreateView):

    template_name = "jobs_search/annonce_form.html"
    model = Annonce
    fields = ['title', 'domaine', 'region', 'description', 'image', 'phone']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateAnnonce, self).form_valid(form)

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(CreateAnnonce, self).dispatch(*args, **kwargs)

class UserFormView(View):

    # user registration view

    form_class = UserForm
    template_name = 'jobs_search/register.html'

    def get(self, request):

        form = self.form_class(None)
        return render (request, self.template_name, {'form':form})

    def post(self, request):

        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.username = username
            user.save()


            # return user object if credentials are correct

            user = authenticate (username = username, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('jobs_search:index')

        return render (request, self.template_name, {'form':form})




class UserLoginFormView(View):

    # user login view

    form_class = UserLoginForm
    template_name = 'jobs_search/login.html'

    def get(self, request):

        form = self.form_class(None)
        return render (request, self.template_name, {'form':form})

    def post(self, request):

        form = self.form_class(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:

            login(request, user)
            return redirect('jobs_search:index')

        else:

            return render (request, self.template_name, {'form':form})


def user_logout(request):

    logout(request)
    return redirect('jobs_search:index')


def user_annonces_list(request):

    user = request.user
    list_annonces = user.annonce_set.all()
    context = {
    'list_annonces':list_annonces
    }
    return render(request, 'jobs_search/annonces_list.html', context)


def search(request):

    region = request.POST.get('region')
    domaine = request.POST.get('domaine')


    annonces = Annonce.objects.filter(region__contains=region)


    return render(request, 'jobs_search/search_results.html', {'annonces': annonces})

