from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class DepotAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...
class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...
class ProduitAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...
class VenteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...
class OperationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
        ...
admin.site.register(Depot,DepotAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Produit,ProduitAdmin)
admin.site.register(Vente,VenteAdmin)
admin.site.register(Operation,OperationAdmin)

