from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^$", views.index, name='index'),
    url("put", views.present, name='present'),
]
