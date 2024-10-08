from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"

    parameter_name = "word"

    def lookups(self, request, ReviewAdmin):
        return [
            ("good", "Good",),
            ("great", "Great",),
            ("thanks", "Thanks",),
        ]
    
    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ("__str__","payload",)
    list_filter = (WordFilter, "rating", "user__is_host", "room__category", )