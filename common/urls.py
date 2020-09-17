# ----- edit -----
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# -

# ----- edit -----
app_name = 'common'

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(), name='login') # view는 따로 만들 필요 없이 loginView를 사용한다.
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'), # template_name을 인자값으로 주어 경로를 수정할 수 있다.

    # ----- edit -----
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # -

    # ----- edit -----
    path('signup/', views.signup, name='signup'),
    # -
]
# -