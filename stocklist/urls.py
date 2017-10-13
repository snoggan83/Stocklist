from django.conf.urls import url
from . import views


app_name = "stocklist"

urlpatterns = [
    # /stocklist/
    url(r'^$', views.index, name='index'),

    # /stocklist/<stocklist_id>/
    url(r'^(?P<stocklist_id>[0-9]+)/$', views.detail, name="detail"),

    # /stocklist/portfolio/
    url(r'^(?P<stocklist_id>[0-9]+)/portfolio$', views.portfolio, name="portfolio"),
]

# Create your views here.
