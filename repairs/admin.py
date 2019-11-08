from django.contrib import admin
from django.template.defaultfilters import truncatechars
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from import_export.widgets import BooleanWidget

class ProductImageInline(admin.TabularInline):
    model = RepairImage
    extra = 0

    class RepairCategoryAdmin(admin.ModelAdmin):
        list_display = ['name', 'is_active', 'created']
        list_filter = ['name']
        search_fields = ['name']

        class Meta:
            model = RepairCategory

    admin.site.register(RepairCategory, RepairCategoryAdmin)

class RepairResource(resources.ModelResource):
    category = fields.Field(column_name='category', attribute='category', widget=ForeignKeyWidget(RepairCategory,
                                                                                                  'name'))

    class Meta:
        model = Repair
        exclude = ['id', 'updated', 'created']

class RepairAdmin (ImportExportActionModelAdmin):
    save_as = True
    resource_class = RepairResource
    fields = ['category', 'iphone_4', ('iphone_5', 'iphone_5s'), ('iphone_6', 'iphone_6_plus', 'iphone_6s', 'iphone_6s_plus'), 'iphone_se', ('iphone_7', 'iphone_7_plus'), ('iphone_8', 'iphone_8_plus'), 'iphone_x', 'iphone_xr', 'iphone_xs', 'iphone_xs_max', 'is_active']
    list_display = ['category', 'is_active', 'iphone_4', 'iphone_5', 'iphone_5s', 'iphone_6', 'iphone_6_plus', 'iphone_6s', 'iphone_6s_plus', 'iphone_se', 'iphone_7', 'iphone_7_plus', 'iphone_8', 'iphone_8_plus', 'iphone_x', 'iphone_xr', 'iphone_xs', 'iphone_xs_max']
    list_editable = ['is_active']
    inlines = [ProductImageInline]
    list_filter = ['category']

    class Meta:
        model = Repair


admin.site.register(Repair, RepairAdmin)

class RepairImageAdmin (admin.ModelAdmin):
    save_as = True
    list_display = ['repair', 'is_main', 'is_active', 'created']
    list_filter = ['is_main', 'is_active', 'repair']

    class Meta:
        model = RepairImage


admin.site.register(RepairImage, RepairImageAdmin)

class StatementAdmin(admin.ModelAdmin):
    save_as = True
    fields = [('email', 'name', 'phone'), 'subject', 'message', ('created', 'updated')]
    list_display = ['name', 'email', 'phone', 'subject', 'Сообщение', 'created']
    list_filter = ['email']
    search_fields = ['email', 'name', 'phone']

    class Meta:
        model = Statement


admin.site.register(Statement, StatementAdmin)




