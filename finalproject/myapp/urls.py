from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('addoffer/', views.addoffer, name='addoffer'),
    path('viewoffer/', views.viewoffer, name='viewoffer'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('pagecontent/', views.pagecontent, name='pagecontent'),
    path('pagecontent1/', views.pagecontent1, name='pagecontent1'),
    path('faq/', views.faq, name='faq'),
    path('logout/', views.logout, name='logout'),
    path('header/', views.header, name='header'),
    path('base/', views.base, name='base'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
