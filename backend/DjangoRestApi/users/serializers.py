from rest_framework import serializers 
from users.models import User
 
 
class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('id',
                'username',
                'password',
                'is_superuser',
                'is_active',
                'contract_signed',
                'created_at',
                'last_modified_at')