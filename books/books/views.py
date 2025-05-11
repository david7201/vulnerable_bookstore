from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Review
from .forms import ReviewForm
from django.db import connection  # Allows direct DB access
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.shortcuts import render, get_object_or_404
import os
from django.db.models import Q
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list' # use this name in for loops	 
    template_name = 'books/book_list.html'
    login_url = 'account_login'
    
class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'
    
class SearchResultsListView(ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        
        # SQL Injection Vulnerability: Directly inserting user input into query
        raw_sql = f"SELECT id, title, author, price FROM books_book WHERE title LIKE '%{query}%'"
        
        with connection.cursor() as cursor:
            cursor.execute(raw_sql)
            columns = [col[0] for col in cursor.description]
            results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        return results
    
    

    
    
    # return Book.objects.filter(
        #     Q(title__icontains=query) | Q(title__icontains=query)
            
        # ) 
        
@csrf_exempt
def add_review(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.author = request.user  # Assuming user is logged in
            review.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        form = ReviewForm()
    
    return render(request, 'books/book_detail.html', {'book': book, 'form': form})

class csrf_attack(ListView):
    model = Book
    template_name = 'csrf_attack.html'
