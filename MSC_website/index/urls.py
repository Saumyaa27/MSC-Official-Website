from django.conf.urls import url
from index import views

urlpatterns = [
    url(r'^$',views.home, name = 'home'),
    ]