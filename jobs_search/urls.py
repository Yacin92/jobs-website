from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'jobs_search'


urlpatterns = [

    #/
    url(r'^$', views.AnnoncesListView.as_view(), name='index'),

    #/annonce pk/
    url(r'^(?P<pk>[0-9]+)/$', views.AnnonceDetailView.as_view(), name='detail'),

    #/add/
    url(r'^add',views.CreateAnnonce.as_view(), name='create'),

    # /register/
    url(r'^register', views.UserFormView.as_view(), name='register'),

    # /login/
    url(r'^login', views.UserLoginFormView.as_view(), name='login'),

    # /logout/
    url(r'^logout', views.user_logout, name='logout'),

    # /list_annonces/
    url(r'^list_annonces', views.user_annonces_list, name='list_annonces'),

    # #/search_results/
    url(r'^search_results', views.search, name='search'),

]
