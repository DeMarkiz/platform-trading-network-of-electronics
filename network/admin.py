from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import NetworkNode, Product


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'email', 'city', 'supplier_link', 'debt', 'created_at')
    list_filter = ('city',)
    actions = ['clear_debt']

    def supplier_link(self, obj):
        if obj.supplier:
            url = reverse("admin:network_networknode_change", args=(obj.supplier.id,))
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return "-"

    supplier_link.short_description = 'Поставщик'

    inlines = [ProductInline]

    def level(self, obj):
        return obj.get_level()

    level.short_description = "Уровень"

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)

    clear_debt.short_description = "Очистить задолженность"
