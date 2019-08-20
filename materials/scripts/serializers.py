from rest_framework import serializers

from materials.scripts.models import Scripts


class ScriptsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scripts
        fields = ('id', 'name', 'description', 'file')
