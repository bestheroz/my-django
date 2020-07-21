from django.contrib import admin

from mydjango.codes.models import CodeGroup, Code


@admin.register(CodeGroup)
class CodeGroupAdmin(admin.ModelAdmin):
    fields = (
        "code_group",
        "name",
    )


@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    fields = (
        "code_group",
        "code",
        "name",
        "available",
        "display_order",
        "authority",
    )
