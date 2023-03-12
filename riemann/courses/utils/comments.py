from courses.models import Comment, Course

def add_comment_to_db(post_request, course_slug):
    author = post_request['author']
    text = post_request['text']
    course = Course.objects.get(slug_name=course_slug)
    comment = {
        'author': author,
        'text': text,
        'course': course
    }
    Comment.objects.create(author=author, text=text, course=course)

def get_comments(course_slug):
    return Comment.objects.filter(course__slug_name=course_slug)[::-1]