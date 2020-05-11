from django.urls import path
from django.contrib.auth import views as auth_views
from app1 import views
urlpatterns=[
path('about/',views.Indexview.as_view(),name='about'),
path('login/list/',views.Passlist.as_view(),name='list'),
path('login/list/<int:pk>/',views.Passdetail.as_view(),name='detail'),
path('create/',views.Passcreate.as_view(),name='create'),
path('<int:pk>/update/',views.Passupdate.as_view(),name='update'),
path('<int:pk>/delete/',views.Passdelete.as_view(),name='delete'),
path('login/',auth_views.LoginView.as_view(),name='login'),
path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]
