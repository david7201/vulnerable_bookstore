from django.urls import path
from .views import BookListView, BookDetailView, SearchResultsListView, add_review, csrf_attack


urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<uuid:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('book/<uuid:book_id>/review/', add_review, name='add_review'),
    path('book_attack/', csrf_attack.as_view(), name='csrf_attack'),
]
