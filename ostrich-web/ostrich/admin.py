# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Light, Status,Camera, Density, Update

from socketIO_client import SocketIO, LoggingNamespace


class StatusInline(admin.TabularInline):
    model = Status
    readonly_fields = ('broken','sender','status','mobile','recieved_at')
    can_delete = False
    extra = 0

    def has_add_permission(self, request):
        return False

# class CategoryAdmin(admin.ModelAdmin):

# def make_published(modeladmin, request, queryset):
#     # queryset.update(status='p')
#     with SocketIO('localhost', 3000, LoggingNamespace) as socketIO:
#     	socketIO.emit('connectme','python-client')
#     	# socketIO.emit('get_status', {'xxx': 'yyy'})
    
#     print "Sending status broadcast - Select  at least one to broadcast the signal"

# make_published.short_description = "Status Broadcast"



class LightAdmin(admin.ModelAdmin):
	readonly_fields = ['active']
	list_display = ['title','active','operating']
	# actions = [make_published]
	inlines = [StatusInline,]
	def get_actions(self, request):
		return []


class StatusAdmin(admin.ModelAdmin):
	readonly_fields = ['broken','sender','status','mobile','light','recieved_at']
	list_display = ['light','broken','sender']

	def has_delete_permission(self, request, obj=None):
		return False
	def has_add_permission(self, request, obj=None):
		return False

	# def change_view(self, request, object_id, form_url='', extra_context=None):
	# 	extra_context = {}
	# 	extra_context['really_hide_save_and_add_another_damnit'] = True
	# 	return super(StatusAdmin, self).change_view(request, object_id,form_url, extra_context=extra_context)

admin.site.register(Light,LightAdmin)
admin.site.register(Status,StatusAdmin)
admin.site.register(Update)
admin.site.register(Camera)
admin.site.register(Density)

# Register your models here.