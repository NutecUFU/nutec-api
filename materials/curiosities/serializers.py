from rest_framework import serializers

from materials.curiosities.models import Curiosities


class CuriositiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curiosities
        fields = ('id', 'name', 'description', 'file')
