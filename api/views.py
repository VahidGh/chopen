from rest_framework import generics, permissions
from .serializers import *
from ion_channel.models import *
from channelworm.models import *
from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'templates/index.html')


class ChannelwormGeneCreateAPI(generics.ListCreateAPIView):
    queryset = IonChannelGene.objects.all()
    serializer_class = ChannelwormGeneSerializer

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


class ChannelwormGeneDetailsAPI(generics.RetrieveUpdateDestroyAPIView):

    queryset = IonChannelGene.objects.all()
    serializer_class = ChannelwormGeneSerializer


class ChannelwormGeneListAPI(generics.ListAPIView):

    queryset = IonChannelGene.objects.all()
    serializer_class = ChannelwormGeneSerializer


class ChannelwormProteinCreateAPI(generics.ListCreateAPIView):
    queryset = Protein.objects.all()
    serializer_class = ChannelwormProteinSerializer

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


class ChannelwormProteinDetailsAPI(generics.RetrieveUpdateDestroyAPIView):

    queryset = Protein.objects.all()
    serializer_class = ChannelwormProteinSerializer


class ChannelwormProteinListAPI(generics.ListAPIView):

    queryset = Protein.objects.all()
    serializer_class = ChannelwormProteinSerializer


class IonChannelCreateAPI(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = IonChannel.objects.all()
    serializer_class = IonChannelSerializer
    # permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new item."""
        serializer.save(username=self.request.user)


class IonChannelDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = IonChannel.objects.all()
    serializer_class = IonChannelSerializer


class IonChannelListAPI(generics.ListAPIView):

    queryset = IonChannel.objects.all()
    serializer_class = IonChannelSerializer


class ReferenceCreateAPI(generics.ListCreateAPIView):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer

    def perform_create(self, serializer):
        serializer.save(username=self.request.user)


class ReferenceDetailsAPI(generics.RetrieveUpdateDestroyAPIView):

    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer


class ReferenceListAPI(generics.ListAPIView):

    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer


class PatchClampCreateAPI(generics.ListCreateAPIView):
    queryset = PatchClamp.objects.all()
    serializer_class = PatchClampSerializer

    def perform_create(self, serializer):
        serializer.save()


class PatchClampDetailsAPI(generics.RetrieveUpdateDestroyAPIView):

    queryset = PatchClamp.objects.all()
    serializer_class = PatchClampSerializer


class PatchClampListAPI(generics.ListAPIView):

    queryset = PatchClamp.objects.all()
    serializer_class = PatchClampSerializer


class CellCreateAPI(generics.ListCreateAPIView):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer

    def perform_create(self, serializer):
        serializer.save()


class CellDetailsAPI(generics.RetrieveUpdateDestroyAPIView):

    queryset = Cell.objects.all()
    serializer_class = CellSerializer


class CellListAPI(generics.ListAPIView):

    queryset = Cell.objects.all()
    serializer_class = CellSerializer


class GraphCreateAPI(generics.ListCreateAPIView):
    queryset = Graph.objects.all()
    serializer_class = GraphSerializer

    def perform_create(self, serializer):
        serializer.save()


class GraphDetailsAPI(generics.RetrieveUpdateDestroyAPIView):

    queryset = Graph.objects.all()
    serializer_class = GraphSerializer


class GraphListAPI(generics.ListAPIView):

    queryset = Graph.objects.all()
    serializer_class = GraphSerializer


class GraphDataCreateAPI(generics.ListCreateAPIView):
    queryset = GraphData.objects.all()
    serializer_class = GraphDataSerializer

    def perform_create(self, serializer):
        serializer.save()


class GraphDataSeriesAPI(generics.ListAPIView):

    serializer_class = GraphDataSerializer

    def get_queryset(self):
        self.graph = get_object_or_404(Graph, id=self.kwargs['pk'])
        return GraphData.objects.filter(graph=self.graph)


class GraphDataDetailsAPI(generics.RetrieveUpdateDestroyAPIView):

    queryset = GraphData.objects.all()
    serializer_class = GraphDataSerializer


class GraphDataListAPI(generics.ListAPIView):

    queryset = GraphData.objects.all()
    serializer_class = GraphDataSerializer


class UserDetailsAPI(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListAPI(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

