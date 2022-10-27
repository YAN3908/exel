from django.contrib import admin

# Register your models here.

from import_export.admin import ImportExportActionModelAdmin
from .models import Book
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget

# admin.site.register(Book)

# class BookImageInline(admin.TabularInline):
#     model =

class BookResurse(resources.ModelResource):
    class Meta:
        model = Book

class BookAdmin(ImportExportActionModelAdmin):
    resource_class = BookResurse
    list_display = [field.name for field in Book._meta.fields if field.name != id]
    # inlines = [BookResurse]


admin.site.register(Book, BookAdmin)