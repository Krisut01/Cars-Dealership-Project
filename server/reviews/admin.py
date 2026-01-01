from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'dealer', 'car_make', 'car_model', 'sentiment', 'created_at')
    list_filter = ('dealer', 'car_make', 'sentiment', 'created_at')
    search_fields = ('user__username', 'dealer__name', 'review_text')
    readonly_fields = ('created_at',)
