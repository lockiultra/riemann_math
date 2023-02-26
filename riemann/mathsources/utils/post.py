from ..models import Book, Links

def get_book_post(book_name):
    book_obj = Book.objects.get(book_name=book_name)
    book_post = _get_book_context(book_obj)
    return book_post

def _get_book_context(book_obj):
    return {
        'title': book_obj.title,
        'authors': book_obj.authors,
        'desc': book_obj.desc,
        'categories': book_obj.categories,
        'img': book_obj.img,
        'links': _get_book_links(book_obj.book_name)
    }

def _get_book_links(book_name):
    try:
        book_links_query = Links.objects.get(book_name__book_name=book_name)
    except Exception:
        book_links_query = ''
    
    if book_links_query:
        book_links_dict = {'YMarket': book_links_query.ymarket_link, 
                           'Ozon': book_links_query.ozon_link, 
                           'Wildberries': book_links_query.wb_link}
    else:
        book_links_dict = {'YMarket': '', 
                           'Ozon': '', 
                           'Wildberries': ''}
    return book_links_dict