from django.contrib import admin
from .models import Post , Category , comment ,Like_dislike ,Replay
# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(comment)
admin.site.register(Like_dislike)
admin.site.register(Replay)