from rest_framework import serializers
from experiments.models import Experiment


class ExperimentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experiment
        fields = ('name', 'description', 'domain', 'status', 'photo')
