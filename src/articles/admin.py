from django.contrib import admin
from django.core.exceptions import MultipleObjectsReturned
from revisions.models import Revision

# Register your models here.
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'pub_date', 'likes', 'approved', 'updated']
    list_editable = ['likes', 'approved']
    list_filter = ['approved']
    readonly_fields = ['updated', 'timestamp']

    class Meta:
        model = Article

    def save_model(self, request, obj, form, change):
        if change:
            try:
                revision, created = Revision.objects.get_or_create(article=obj)
            except MultipleObjectsReturned:
                created = False
                revision = Revision.objects.filter(article=obj).order_by('-timestamp')[0]
            if not created:
                user_changed = revision.article.user != obj.user
                title_changed = revision.article.title != obj.title
                body_changed = revision.article.body != obj.body
                likes_changed = revision.article.likes != obj.likes
                if user_changed or title_changed or body_changed or likes_changed:
                    new_revision = Revision()
                    new_revision.article = obj
                    new_revision.user = obj.user
                    new_revision.title = obj.title
                    new_revision.body = obj.body
                    new_revision.likes = obj.likes
                    new_revision.save()
                obj.save()
        else:
            obj.save()
            Revision.objects.create(article=obj, user=obj.user, title=obj.title, body=obj.body, likes=obj.likes)


admin.site.register(Article, ArticleAdmin)
