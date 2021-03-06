from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newsStory'),
    path('<int:pk>/delete-story/', views.DeleteStoryView.as_view(), name='deleteStory'),
    path('<int:pk>/update-story/', views.UpdateStoryView.as_view(), name='updateStory'),
    path('<int:pk>/author/', views.AuthorView.as_view(), name='author'),
]