from django.contrib import admin
from .models import Wiki
from django.utils.html import format_html
from django.urls import reverse
from django.shortcuts import redirect

@admin.register(Wiki)
class WikiAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'creado', 'ver_en_sitio')
    prepopulated_fields = {'slug': ('titulo',)}

    def ver_en_sitio(self, obj):
        if obj.slug:
            url = reverse('wiki:detalle', kwargs={'slug': obj.slug})
            return format_html('<a href="{}" target="_blank">👁️ Ver</a>', url)
        return "-"

    def response_change(self, request, obj):
        if "_save_and_view" in request.POST:
            return redirect('wiki:detalle', slug=obj.slug)
        return super().response_change(request, obj)
    
    ver_en_sitio.short_description = 'Ver en sitio'

