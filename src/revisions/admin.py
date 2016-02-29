from django.contrib import admin

# Register your models here.
from .models import Revision


class RevisionAdmin(admin.ModelAdmin):
    list_display = ['article', 'user', 'timestamp']
    readonly_fields = ['timestamp']

    class Meta:
        model = Revision


admin.site.register(Revision, RevisionAdmin)
