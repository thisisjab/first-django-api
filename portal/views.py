from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class JobViewSet(ModelViewSet):
    queryset = models.Job.objects.prefetch_related('category').all()
    serializer_class = serializers.JobSerializer


class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CompnayViewSet(ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer
