from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('registration/', views.regView, name='reg'),
    path('registration/login', views.MyLoginView.as_view(), name='login'),
    path('accounts/<int:pk>', views.Profile.as_view(), name='profile'),
]