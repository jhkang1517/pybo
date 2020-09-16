"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path # 아래에서 사용

# ----- edit -----
from pybo import views
# -

# ----- edit -----
from django.urls import include, path
# -


urlpatterns = [
    path('admin/', admin.site.urls),
    # ----- edit -----
    path('pybo/', views.index),
    # 특별한 경우가 아니라면, 항상 URL 매핑시 끝에 / 를 붙여줄 것 (웹 브라우저 변환 시 URL을 정규화하는 장고의 기능으로 인해 자동으로 변환된다.)
    # views.index = views.py 파일의 index 함수를 의미
    # -

    # ----- edit -----
    path('pybo/', include('pybo.urls')),
    # pybo/ 로 시작되는 URL이 요청되면, 이제 pybo/urls.py 파일의 매핑정보를 읽어서 처리하라는 의미.
    # 따라서 이제 pybo/question/craate, pybo/answser/create 등의 URL이 추가되어도 config/urls.py 파일을 수정할 필요 없다.
    # -



]
