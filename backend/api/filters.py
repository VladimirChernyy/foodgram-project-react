from django_filters.rest_framework import FilterSet, filters
from recipe.models import Ingredient, Recipe, Tag
from rest_framework.filters import SearchFilter


class IngredientFilter(SearchFilter):
    search_param = 'name'

    class Meta:
        model = Ingredient
        fields = ('name',)


class RecipeFilter(FilterSet):
    tags = filters.ModelMultipleChoiceFilter(field_name='tags__slug',
                                             to_field_name='slug',
                                             queryset=Tag.objects.all())
    is_favorited = filters.BooleanFilter(
        method='is_favorited_filter')
    is_in_shopping_cart = filters.BooleanFilter(
        method='is_in_shopping_cart_filter')

    class Meta:
        model = Recipe
        fields = ('tags', 'author',)

    def is_favorited_filter(self, queryset, name, value):
        if value:
            return queryset.filter(favorites__user=self.request.user.id)
        return queryset

    def is_in_shopping_cart_filter(self, queryset, name, value):
        if value:
            return queryset.filter(shopping_list__user=self.request.user.id)
        return queryset
