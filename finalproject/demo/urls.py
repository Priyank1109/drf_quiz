
from django.urls import path
from demo import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home1', views.home1, name='home1'),
    path('signup1/', views.signup1, name='signup1'),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)