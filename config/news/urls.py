from django.urls import path
from news import views

urlpatterns = [
    path("", views.ListPostAPIView.as_view(), name="post_list"),
    path("create/", views.CreatePostAPIView.as_view(), name="post_create"),
    path("update/<int:pk>/", views.UpdatePostAPIView.as_view(), name="update_post"),
    path("delete/<int:pk>/", views.DeletePostAPIView.as_view(), name="delete_post"),
    path("comments/", views.ListCommentAPIView.as_view(), name="comment_list"),
    path("comments/create/", views.CreateCommentAPIView.as_view(), name="comment_create"),
    path("comments/update/<int:pk>/", views.UpdateCommentAPIView.as_view(), name="update_comment"),
    path("comments/delete/<int:pk>/", views.DeleteCommentAPIView.as_view(), name="delete_comment"),
    path("upvote/", views.PostUpvote.as_view(), name="upvote_post")
]
