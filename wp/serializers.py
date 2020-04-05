from rest_framework import serializers
from .models import wp_term_taxonomy


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = wp_term_taxonomy
        fields = '__all__'
