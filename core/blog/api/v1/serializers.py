from rest_framework import serializers
from blog.models import Post,Category
from accounts.models import Profile

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    # relative_url = serializers.URLField(source='get_absolute_api_url',read_only=True)
    absolute_url = serializers.SerializerMethodField(method_name='get_absolute_url')

    class Meta:
        model = Post
        fields = ['id','author','title','category','snippet','content','status','absolute_url',
                  'created_date','published_date']
        read_only_fields = ['author'] 
    
    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)
    
    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context['kwargs'].get('pk'):
            rep.pop('snippet',None)
            rep.pop('absolute_url',None)
        else:
            rep.pop('content',None)
        rep['category'] = CategorySerializer(instance.category).data
        return rep
    
    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = Profile.objects.get(user_id = request.user.id)
        return super().create(validated_data)
