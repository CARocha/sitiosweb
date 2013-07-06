from django.contrib import admin
from .models import Publicaciones

class PublicacionesAdmin(admin.ModelAdmin):

    def queryset(self, request):
        qs = super(PublicacionesAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(autor=request.user)

admin.site.register(Publicaciones, PublicacionesAdmin)