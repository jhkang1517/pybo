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
    path('question/create/', views.question_create, name='question_create')
]
# urlpattern의 path는 path('', views.index) 처럼 pybo/ 를 생략한다.
# 그 이유는 config/urls.py 파일에서 이미 pybo/ 로 시작하는 URL이 매핑되었기 때문이다.
# -