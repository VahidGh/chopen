from rest_framework import serializers
from ion_channel.models import *
from channelworm.models import *


class IonChannelGeneSerializer(serializers.ModelSerializer):

    class Meta:
        model = IonChannelGene
        fields = '__all__'


class ProteinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Protein
        fields = '__all__'


class IonChannelSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = IonChannel
        fields = '__all__'
        # fields = ('id', 'channel_name', 'create_date', 'last_update')
        # read_only_fields = ('create_date', 'last_update')


class PatchClampSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatchClamp
        fields = '__all__'


class ReferenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reference
        fields = '__all__'


class CellSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cell
        fields = '__all__'


class GraphSerializer(serializers.ModelSerializer):

    class Meta:
        model = Graph
        fields = '__all__'


class GraphDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = GraphData
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

