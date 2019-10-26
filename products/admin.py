from django.contrib import admin
from django.template.defaultfilters import truncatechars
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from import_export.widgets import BooleanWidget

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

    class ProductCategoryAdmin(admin.ModelAdmin):
        list_editable = ['is_active']
        list_display = ['name', 'is_active', 'created']
        list_filter = ['name']
        search_fields = ['name']

        class Meta:
            model = ProductCategory

    admin.site.register(ProductCategory, ProductCategoryAdmin)

    class StatusAdmin(admin.ModelAdmin):
        list_display = ['name', 'is_active', 'created']
        list_filter = ['name']
        search_fields = ['name']

        class Meta:
            model = ProductStatus

    admin.site.register(ProductStatus, StatusAdmin)


class ProductResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(ProductCategory,
                                                                                                  'name'))
    status = fields.Field(column_name='status', attribute='status', widget=ForeignKeyWidget(ProductStatus, 'name'))

    class Meta:
        model = Product
        exclude = ['discount', 'id', 'is_active', 'description', 'top_sales', 'updated', 'created', 'memory']

class ProductAdmin (ImportExportActionModelAdmin):
    save_as = True
    resource_class = ProductResource
    fields = [('name', 'category', 'status'), ('price', 'memory', 'vendor_code', 'discount'), 'description', ('is_active', 'top_sales')]
    list_editable = ['price', 'category', 'is_active', 'top_sales', 'status']
    list_display = ['Наименование', 'price', 'category', 'memory', 'is_active', 'top_sales', 'status']
    inlines = [ProductImageInline]
    list_filter = ['category', 'status', 'is_active', 'memory', 'top_sales']
    search_fields = ['name']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)

class ProductImageAdmin (admin.ModelAdmin):
    save_as = True
    list_display = ['product', 'image', 'is_main', 'is_active', 'created']
    list_filter = ['is_main', 'is_active', 'product']

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)




