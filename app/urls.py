from django.urls import path
from . import views # Importa as funções com as views definidas

urlpatterns = [
    path('produtos/',views.buscar_produtos_get), # Associa a URL '/produtos' com a função buscar_produtos_get
    path('cadastra_produto',views.cadastra_produto_post),
]