from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^backlog/$', views.product_backlog, name='product_backlog'),
    url(r'^tags/$', views.tags, name='tags'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^points/$', views.points, name='points'),
    url(r'^users/$', views.users, name='users'),
    url(r'^leaderboard/$', views.leaderboard, name='leaderboard'),
    url(r'^user/(?P<user_id>[0-9]+)/$', views.user, name='user'),
    url(r'^story/(?P<story_id>[0-9]+)/$', views.story, name='story'),
    url(r'^release/(?P<release_id>[0-9]+)/$', views.release, name='release'),
    url(r'^retrospective/(?P<release_id>[0-9]+)/$', views.retrospective, name='retrospective'),
    url(r'^sprint/(?P<sprint_id>[0-9]+)/$', views.sprint, name='sprint'),
]