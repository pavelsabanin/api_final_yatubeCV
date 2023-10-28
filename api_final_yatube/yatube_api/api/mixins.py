from rest_framework import mixins
from rest_framework import viewsets


class CreateRetrieveViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    pass
