from django.conf.urls import url
from games import views

# url 을 뷰로 보냄
urlpatterns = [
    url(r'^games/$', views.game_list),
    url(r'^games/(?P<pk>[0-9]+)/$', views.game_detail),
]