from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # Django 모델을 첫번째 인자로 받고, 몇개의 키워드 인수를 모델 관리자의 get() 함수에 넘깁니다.
    # 만약 객체가 존재하지 않을 경우, Http404 예외가 발생
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
