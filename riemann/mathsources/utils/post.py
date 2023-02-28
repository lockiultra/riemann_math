from ..models import Book

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
        'links': book_obj.link
    }