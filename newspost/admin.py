from django.contrib import admin
from django.db import models

from django_summernote.admin import SummernoteModelAdmin

from .models import *

class ArticlesAdmin(SummernoteModelAdmin):
	summernote_fields = ('description',)
	prepopulated_fields = {'slug': ('url_title',)}

admin.site.register(Articles, ArticlesAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

# admin.site.register(Category)
# admin.site.register(SubCategory)
# admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Profile)
admin.site.register(Advertisment)
admin.site.register(Video)
admin.site.register(Reporter)
