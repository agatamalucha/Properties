from django.contrib import admin

from core.models import PropertyTypeModel, BallincolligPropertyModel




class BallincolligPropertyModelAdmin(admin.ModelAdmin):
    list_display = ["full_address", "area", "price", "sold_date"]
    class Meta:
        model = BallincolligPropertyModel


admin.site.register(BallincolligPropertyModel, BallincolligPropertyModelAdmin)
admin.site.register(PropertyTypeModel)