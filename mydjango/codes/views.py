import logging

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from mydjango.codes.models import CodeGroup, Code
from mydjango.codes.serializers import CodeGroupSerializer, CodeSerializer

logger = logging.getLogger(__name__)


class CodeGroupViewSet(viewsets.ModelViewSet):
    queryset = CodeGroup.objects.all()
    serializer_class = CodeGroupSerializer
    ordering = ["code_group"]


class CodeViewSet(viewsets.ModelViewSet):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("code_group",)
    ordering = ["display_order"]
