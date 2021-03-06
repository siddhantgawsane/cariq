from units.models import Unit, Workshop, Owner
from django.contrib import admin

class UnitsInline(admin.StackedInline):
    model = Unit
    extra = 3

class UnitAdmin(admin.ModelAdmin):
    fieldsets = [
    #    ('Action info',               {'fields': ['action']}),
    ]
    list_filter = ['action']


class OwnerAdmin(admin.ModelAdmin):
    fieldsets = [
    #    (None,               {'fields': ['status']}),
    ]
    list_filter = ['status']

class WorkshopAdmin(admin.ModelAdmin):
    fieldsets = [
    #    (None,               {'fields': ['status']}),
    ]
    list_filter = ['status']
#    inlines = [UnitsInline]

admin.site.register(Unit,UnitAdmin)
admin.site.register(Workshop,WorkshopAdmin)
admin.site.register(Owner,OwnerAdmin)
