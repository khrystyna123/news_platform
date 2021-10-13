from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from news.serializers import CommentSerializer, PostSerializer
from news.models import Comment, Post


# # Create your views here.
class ListPostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreatePostAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UpdatePostAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DeletePostAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpvote(ListPostAPIView):
    def get_queryset(self):
        queryset = Post.objects.all()
        post_id = self.request.query_params.get('post')

        if post_id:
            post = get_object_or_404(queryset, id=post_id)
            post.upvotes += 1

            post.save()

        return queryset


class ListCommentAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CreateCommentAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UpdateCommentAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class DeleteCommentAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

