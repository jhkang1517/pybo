# ----- edit -----
from django.urls import path

from . import views

# ----- edit -----
app_name = 'pybo'
# -

urlpatterns = [
    path('', views.index, name='index'), # name = index 라고 이름을 부여함
    # ----- edit -----
    path('<int:question_id>/', views.detail, name='detail'), # name = detail 이라고 이름을 부여함
    # -
    # ----- edit -----
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    #-

    # ----- edit -----
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    # -

    # ----- edit -----
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    # -

    # ----- edit -----
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    # -

    # ----- edit -----
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    # -

    # ---- edit -----
    path('comment/create/question/<int:question_id>/', views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', views.comment_delete_question, name='comment_delete_question'),
    # -

    # ----- edit -----
    path('comment/create/answer/<int:answer_id>/', views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', views.comment_delete_answer, name='comment_delete_answer'),
    # -
]
# urlpattern의 path는 path('', views.index) 처럼 pybo/ 를 생략한다.
# 그 이유는 config/urls.py 파일에서 이미 pybo/ 로 시작하는 URL이 매핑되었기 때문이다.
# -