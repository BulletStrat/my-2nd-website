from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from quote.models import Post

from .serializers import (
    PostListSerializer,
    PostCreateUpdateSerializer
)
from django.db.models import Q

class PostListAPIView(ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(text__icontains=query)
            ).distinct()
        return queryset_list

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save()



