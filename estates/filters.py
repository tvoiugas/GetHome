from cgitb import lookup
from secrets import choice
import django_filters
from pkg_resources import empty_provider
from .models import Tag


class EstateFilter(django_filters.FilterSet):
    tags = django_filters.ModelMultipleChoiceFilter(
        label='тег', field_name="tags", queryset=Tag.objects.all())
