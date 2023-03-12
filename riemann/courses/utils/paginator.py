from django.core.paginator import Paginator
from courses.models import Course

def get_page_obj(request, topic=''):
    page_num = _get_page_num(request)
    courses_query = _get_courses_query(topic)
    paginator = Paginator(courses_query, 12)
    return paginator.get_page(page_num)
    
def _get_page_num(request):
    if request.GET:
        return request.GET.get('page')
    return 1

def _get_courses_query(topic):
    if topic and topic != 'all':
        return Course.objects.filter(categories__slug_name=topic)
    return Course.objects.all()