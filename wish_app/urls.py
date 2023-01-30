
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('logout',views.logout, name='login'),
    path('new_wish', views.new_wish, name='new_wish'),
    path('stats', views.stats, name='stats'),
    path('remove_wish/<int:wish_id>', views.remove_wish, name='remove_wish'),
    path('edit_wish/<int:wish_id>', views.edit_wish, name='edit_wish'),
    path('grant_wish/<int:wish_id>', views.grant_wish, name='grant_wish'),
    path('like_wish/<int:wish_id>', views.like_wish, name='like_wish'),
    path('unlike_wish/<int:wish_id>', views.unlike_wish, name='unlike_wish'),

]