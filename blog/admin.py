# -*- coding:utf-8 -*-
from django.contrib import admin
from blog.models import User,Tag,Article,Category,Comment,Links,Ad

# Register your models here.自定义方式注册module
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'desc', 'click_count',)#定义想要显示的列
    list_display_links = ('title', 'desc', )
    list_editable = ('click_count',)

    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', 'user', 'category', 'tag', )
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend',)
        }),
    )

    class Media:#引入富文本编辑器媒体文件
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )
#admin中注册module
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)