from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, Comment

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'login', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'login')
    ordering = ('username',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'login', 'home_page', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'login', 'password1', 'password2'),
        }),
    )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'likes')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at', 'likes')
    list_filter = ('created_at', 'post')
    search_fields = ('text', 'user__username', 'post__title')
    date_hierarchy = 'created_at'
    raw_id_fields = ('user', 'post', 'parent')
