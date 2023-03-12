from courses.models import Course

def get_course(slug_name):
    course = Course.objects.get(slug_name=slug_name)
    return course