from django.contrib import admin
from .models import Videos, Fotos, Audio

class VideosAdmin(admin.ModelAdmin):
    pass

    # def queryset(self, request):
    #     qs = super(VideosAdmin, self).queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(autor=request.user)

class AudioAdmin(admin.ModelAdmin):
    pass
    # def queryset(self, request):
    #     qs = super(AudioAdmin, self).queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(autor=request.user)

admin.site.register(Videos, VideosAdmin)
admin.site.register(Fotos)
admin.site.register(Audio, AudioAdmin)