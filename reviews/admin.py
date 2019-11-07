from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources


class ReviewImageInline(admin.TabularInline):
    model = ReviewImage
    extra = 0


class ReviewResource(resources.ModelResource):

    class Meta:
        model = Review
        exclude = ['id', 'updated', 'created']


class ReviewAdmin (ImportExportActionModelAdmin):
    save_as = True
    resource_class = ReviewResource
    fields = [('first_name', 'last_name'), 'message', 'is_active']
    list_display = ['id', 'first_name', 'last_name', 'Отзыв', 'is_active']
    list_editable = ['is_active']
    inlines = [ReviewImageInline]
    list_filter = ['is_active']
    search_fields = ['first_name', 'last_name']

    class Meta:
        model = Review


admin.site.register(Review, ReviewAdmin)


class ReviewImageAdmin (admin.ModelAdmin):
    save_as = True
    list_display = ['review', 'is_main', 'image', 'is_active', 'created']
    list_filter = ['is_main', 'is_active', 'review']

    class Meta:
        model = ReviewImage


admin.site.register(ReviewImage, ReviewImageAdmin)