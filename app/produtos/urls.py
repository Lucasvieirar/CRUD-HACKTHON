from django.urls import path
from .views import (
    ProdutoListView,
    ProdutoDetailView,
    ProdutoCreateView,
    ProdutoUpdateView,
    ProdutoDeleteView
)

urlpatterns = [
    path('', ProdutoListView.as_view(), name='produto_list'),
    path('<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    path('novo/', ProdutoCreateView.as_view(), name='produto_create'),
    path('<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('<int:pk>/deletar/', ProdutoDeleteView.as_view(), name='produto_delete'),
]