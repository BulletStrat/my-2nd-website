from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)

from quote.models import Post

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'user',
            'status',
            'published_date',
        ]


class PostListSerializer(ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'user',
            'status',
            'published_date',
        ]
    def get_user(self,obj):
        return str(obj.user.username)