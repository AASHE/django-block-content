from django.contrib import admin
from .models import Block, Theme


class BlockAdmin(admin.ModelAdmin):
    pass
admin.site.register(Block, BlockAdmin)


class ThemeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Theme, ThemeAdmin)
