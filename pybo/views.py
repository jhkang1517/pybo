from django.shortcuts import render
# ----- edit -----
from django.http import HttpResponse
# -

# ----- edit -----
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
# -

# Create your views here.
# ----- edit -----
def index(request):
    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
    # ----- edit -----
    """
    pybo 목록 출력
    """

    # ----- edit -----
    page = request.GET.get('page', '1') # 페이지

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(question_list, 10) # 페이지 당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    # -

    context = {'question_list': page_obj}
    return render(request, 'pybo/question_list.html', context)
    # -

# ----- edit -----
def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = Question.objects.get(id=question_id)

    # ----- edit -----
    question = get_object_or_404(Question, pk=question_id)
    # -
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)
# -

def question_create(request):
    """
    pybo 질문 등록
    """
    # ----- edit -----
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')

    else:
        form = QuestionForm()
    context = {'form' : form}
    return render(request, 'pybo/question_form.html', context)
    # form = QuestionForm()
    # return render(request, 'pybo/question_form.html', {'form' : form})
    # -

# ----- edit -----
def answer_create(request, question_id):
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)

    else:
        form = AnswerForm()
    context = {'question' : question, 'form' : form}
    return render(request, 'pybo/question_detail.html', context)
# -