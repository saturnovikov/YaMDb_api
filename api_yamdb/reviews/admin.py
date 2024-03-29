from django.contrib import admin
from .models import Category, Comment, Review, User, Title, Genre


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'score', 'title')


admin.site.register(User)
admin.site.register(Title)
admin.site.register(Genre)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment)
admin.site.register(Category)
