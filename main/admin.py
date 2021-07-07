from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Suscribes


class SuscribesResourseces(resources.ModelResource):
    class Meta:
        model = Suscribes


class SuscribesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ['name', 'email']
    resource_class = SuscribesResourseces


admin.site.register(Suscribes, SuscribesAdmin)
