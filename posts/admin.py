from django.contrib import admin

# Register your models here.
from .models import Post

# """ Django 管理サイト名変更 """
# admin.site.site_header = 'Django カスタムサイト'

# """ サイト管理名変更 """
# admin.site.index_title = 'モデルリスト'

admin.site.register(Post)
