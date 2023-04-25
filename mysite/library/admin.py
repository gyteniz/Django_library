from django.contrib import admin
from . import models

class BooksInstanceInline(admin.TabularInline):
    model = models.BookInstance
    readonly_fields = ['uuid']
    can_delete = False
    extra = 0

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'author', 'display_genre']
    inlines = [BooksInstanceInline]

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['book', 'uuid', 'status', 'due_back']
    list_filter = ['status', 'due_back', 'book']


    fieldsets = (
        ('General', {'fields': ('uuid', 'book')}),
        ('Availability', {'fields': ('status', 'due_back')}),
    )

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'display_books']


# Register your models here.
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Genre)
admin.site.register(models.BookInstance, BookInstanceAdmin)

