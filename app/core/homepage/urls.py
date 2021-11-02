from django.urls import path
from core.homepage.views import productosindex

app_name = 'erp'

urlpatterns = [
    # category
    path('', productosindex.as_view(), name='productos_index'),
]