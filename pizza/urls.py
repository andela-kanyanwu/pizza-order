from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from pizza_app import views

urlpatterns = patterns('',
    # url(r'^$', 'pizza.views.home', name='home'),
    url(r'^pizzas/$', views.PizzaList.as_view(), name='pizza_list'),
    url(r'^pizzas/(?P<name>[a-zA-Z]+)$', views.PizzaDetail.as_view(), name='pizza_detail'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

urlpatterns = format_suffix_patterns(urlpatterns)
