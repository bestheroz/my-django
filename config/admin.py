from django.contrib import admin

from mydjango.todos.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    fields = (
        "id",
        "text",
        "checked",
    )
