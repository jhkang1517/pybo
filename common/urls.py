# ----- edit -----
from django.urls import path
from django.contrib.auth import views as auth_views
# -

# ----- edit -----
app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login') # view는 따로 만들 필요 없이 loginView를 사용한다.
]
# -