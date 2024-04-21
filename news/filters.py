from django.forms import DateInput
from django_filters import FilterSet, ModelMultipleChoiceFilter, DateFilter

from .models import Post, Category


class PostFilter(FilterSet):
    categories = ModelMultipleChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label='Категория',
        conjoined=True,
    )

    time_post = DateFilter(
        lookup_expr='icontains',
        widget=DateInput(attrs={'placeholder': 'Select a date', 'type': 'date'}),
        label='Date',
    )

    class Meta:
        model = Post
        fields = ['title']


