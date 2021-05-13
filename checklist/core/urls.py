from django.urls import path
from .views import CheckListsAPIView,CheckListItemCreateAPIView,CheckListAPIView,CheckListItemAPIView
urlpatterns = [
    path('api/checkLists/',CheckListsAPIView.as_view()),
    path('api/checkLists/<int:pk>',CheckListAPIView.as_view()),
    path('api/checkListItem/create',CheckListItemCreateAPIView.as_view()),
    path('api/checkListItem/<int:pk>',CheckListItemAPIView.as_view()),
]