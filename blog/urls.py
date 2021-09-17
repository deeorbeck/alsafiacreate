from django.urls import path
from .views import *


app_name = 'blog'

urlpatterns = [
    path('',index,name="index"),
    path('signup/',signupPage, name='signup'),
    path('login/',loginPage, name='login'),
    path('eltuvchi/', eltuvchiPage, name='postman'),
    path('offer/<int:pk>/', offerDetailPage, name='offer'),
    path('offers/', offerallproducts, name='offers'),
    path('p/<str:slug>/', productDetail, name='product'),
    path('logout/', logoutPage, name='logout'),
    path('account/user/<str:username>/', user_info),
    path('profile/', profile, name='profile'),
    path('workdesk/', ishxonaPage, name='ishxona'),
    path('oqimlar/', oqimpage, name='oqimlar'),
    path('balans/', balansPage, name='balans'),
    path('news/', newPage, name='news'),
    path('statistika/', statistikaPage, name='statistika')


]