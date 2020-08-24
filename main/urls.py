from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='test_list'),
    path('results/<int:pk>/page=<int:page>', views.results_by_test, name='results_page'),
    path('results/<int:pk>/', views.results_by_test, name='results'),
    path('page=<int:page>', views.index, name='test_list_page'),
    path('result/<int:pk>', views.result, name='result'),
    path('test/<int:pk>', views.test_passing, name='test'),
    path('new_test', views.new_test, name='new_test'),
]
