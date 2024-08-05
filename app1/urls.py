from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.index,name='home'),
    path('',views.signup,name='signup'),
    path('login/',views.loginn,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
]