from django.urls import path,include
from django.conf import settings
from .views import *


urlpatterns = [

    path('', homepage, name="homepage"),

    path('fetch_graph/', fetch_graph, name='fetch_graph'),
    # path('studentinfo/<int:rollno>', Student_detail, name="homepage"),

]
