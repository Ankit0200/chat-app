from django.urls import path,include
from . import views
urlpatterns = [
    path('<groupname>/',views.index_page,name='index')
]