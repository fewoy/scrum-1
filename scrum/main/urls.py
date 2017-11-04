from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^backlog/$', views.backlog, name='backlog'),
    url(r'^tags/$', views.tags, name='tags'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^points/$', views.points, name='points'),
    url(r'^leaderboard/$', views.leaderboard, name='leaderboard'),

    url(r'^users/$', views.users, name='users'),
    url(r'^user/(?P<user_id>[0-9]+)/$', views.user, name='user'),

    url(r'^stories/$', views.stories, name='stories'),
    url(r'^story/(?P<story_id>[0-9]+)/$', views.story, name='story'),

    url(r'^releases/$', views.releases, name='releases'),
    url(r'^release/(?P<release_id>[0-9]+)/$', views.release, name='release'),
    url(r'^retrospective/(?P<release_id>[0-9]+)/$', views.retrospective, name='retrospective'),

    url(r'^sprints/$', views.sprints, name='sprints'),
    url(r'^sprint/(?P<sprint_id>[0-9]+)/$', views.sprint, name='sprint'),
]
