from django.urls import path
from .views import ListImage, ImageProd, ListColor, ColorProd, ListProduct, ProdProduct


urlpatterns = [
  
    
    path('img', ListImage.as_view(), name='img'),
    path('imgs/<int:pk>/', ImageProd.as_view(), name='imgs'),
    
    
    path('clr', ListColor.as_view(), name='clr'),
    path('clrs/<int:pk>/', ColorProd.as_view(), name='clrs'),
    
    path('prd', ListProduct.as_view(), name='prd'),
    path('prds/<int:pk>/', ProdProduct.as_view(), name='prds'),

]

