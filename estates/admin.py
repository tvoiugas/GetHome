from django.contrib import admin

from .models import Estate, Details, Features


class AdminDetail(admin.TabularInline):
	model = Details


class AdminEstate(admin.ModelAdmin):
	inlines = [
		AdminDetail,
	]



admin.site.register(Estate, AdminEstate)
admin.site.register(Details)
admin.site.register(Features)