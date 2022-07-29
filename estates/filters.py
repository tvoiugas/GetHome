import django_filters
from .models import Tag


class EstateFilter(django_filters.FilterSet):
    tags = django_filters.ModelMultipleChoiceFilter(
        label='тег', field_name="tags", queryset=Tag.objects.all(), widget=django_filters.widgets.LinkWidget)
