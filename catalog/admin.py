from django.contrib import admin
from.models import Author,Genre,Book,BookInstance




# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

class Author_book(admin.TabularInline):
    model = Book
# class Author_bookInstance(admin.TabularInline):
#     model = BookInstance

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [Author_book]




class BooksInstanceInline(admin.StackedInline):
    model = BookInstance
  #  model = [Author,BookInstance]
## 怎么才能放更多的内容进去

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]




@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('status','book','borrower', 'due_back','id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        ('base info', {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )
