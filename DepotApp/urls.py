from django.urls import path 
from . import  views
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('' , views.AllDepot,name='depots'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('AllProduct/<int:id>', views.AlLProduct, name='AllProduct'),
    path('Allhistorique/<int:id>', views.AlLHistorique, name='Allhistorique'),
    path('AllProduct/<int:id>/AjouterProduit/', views.AjouterProduit, name='AjouterProduit'),
    path('AllProduct/<int:id>/modificationProduct', views.modifier_produit, name='modificationProduct'),
    path('AllOperation/', views.AllOperation, name='AllOperation'),
    path('modificationIperation/<int:id>', views.modificationOperation, name='modificationOperation'),
    path('AjouterOperation/', views.AjouterOperatione, name='AjouterOperation'),
    path('register/', views.register, name='register'),
    path('AllAdmin/', views.AllAdmin, name='AllAdmin'),
    path('AcueilPage/<int:id>', views.AcueilPage, name='AcueilPage'),
    path('AcueilPage/<int:id>/AjouterVente/', views.AjouterVente, name='AjouterVente'),
    path('logout/', views.user_logout, name='logout'),


    ]