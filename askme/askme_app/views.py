from django.shortcuts import render
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)

QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'content': f'Long lorem ipsum {i}',
    } for i in range(20)
]

def paginate(objects, page, per_page=5):
    paginator = Paginator(QUESTIONS, per_page)
    default_page = 1
    try:
        items_page = paginator.page(page)
    except PageNotAnInteger:
        items_page = paginator.page(default_page)
    except EmptyPage:
        items_page = paginator.page(paginator.num_pages)
    return items_page
# Create your views here.
def index(request):
    page = request.GET.get('page', 1)
    items_page = paginate(QUESTIONS, page)
    return render(request, 'index.html', {'questions': items_page, 'pages': items_page})


def question(request, question_id):
    comments = [
        {
            'id': i,
            'content': f'Long lorem ipsum {i}',
        } for i in range(30)
    ]
    page = request.GET.get('page', 1)
    items_page = paginate(comments, page)
    item = QUESTIONS[question_id]
    return render(request, 'question.html', {'question': item, 'comments': items_page, 'pages': items_page})

def ask(request):
    return render(request, 'ask.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')


