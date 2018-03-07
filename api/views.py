from rest_framework import generics, permissions
from .serializers import *
from ion_channel.models import *


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

