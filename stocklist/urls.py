from django.conf.urls import url
from . import views

app_name = "stocklist"

urlpatterns = [
    # /stocklist/
    url(r'^$', views.index, name='index'),

    # /stocklist/<stocklist_title>/
    url(r'^(?P<stocklist_title>\w+)/$', views.detail, name="detail"),

    # /stocklist/<stocklist_id>/
    url(r'^(?P<stocklist_title>\w+)/(?P<stocknum>[0-9]+)/$', views.detail_stock, name="detail_stock"),

    # /stocklist/portfolio/
    url(r'^(?P<stocklist_id>[0-9]+)/portfolio$', views.portfolio, name="portfolio"),
]

