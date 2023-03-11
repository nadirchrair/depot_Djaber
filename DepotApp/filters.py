import django_filters
from django import forms
from django_filters import DateFilter

from .models import *
class OperationFilter(django_filters.FilterSet):
    start_date= DateFilter(field_name='vendu_at',lookup_expr='gte')
    end_date= DateFilter(field_name='vendu_at',lookup_expr='lte')

    class Meta:
        model = Vente
        fields = '__all__'
        exclude=['vendu_at']