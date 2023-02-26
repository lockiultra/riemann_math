from django.core.paginator import Paginator
from ..models import Book

def get_page_obj(request, topic=''):
    page_num = _get_page_num(request)
    books_query = _get_books_query(topic)
    paginator = Paginator(books_query, 12)
    print(books_query)
    return paginator.get_page(page_num)
    
def _get_page_num(request):
    if request.GET:
        return request.GET.get('page')
    return 1

def _get_books_query(topic):
    if topic and topic != 'all':
        return Book.objects.filter(categories__topic_name=topic)
    return Book.objects.all()