from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        url = serializers.HyperlinkedIdentityField(
            view_name='users',
            lookup_field='id'
        )
        fields = ('id', 'url', 'first_name', 'last_name', 'email')


class UserViewSet(viewsets.ModelViewSet):
    url = serializers.HyperlinkedIdentityField(view_name="myapp:user-detail")

    class Meta:
        model = User
        fields = ('url', 'username')
    
    serializer_class = UserSerializer
    queryset = User.objects.all()
