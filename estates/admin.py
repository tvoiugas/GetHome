from django.contrib import admin

from .models import Estate, Details, Feature


class AdminDetail(admin.TabularInline):
	model = Details


class AdminEstate(admin.ModelAdmin):
	inlines = [
		AdminDetail,
	]



admin.site.register(Estate)
admin.site.register(Details)
admin.site.register(Feature)