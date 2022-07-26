from django.contrib import admin

from .models import Estate, Details, Feature, Tag


class AdminDetail(admin.TabularInline):
    model = Details


class AdminEstate(admin.ModelAdmin):
	inlines = [
		AdminDetail,
	]
	list_display = [
		'id', 'title','posted_on'
	]


admin.site.register(Estate, AdminEstate)
admin.site.register(Details)
admin.site.register(Feature)
admin.site.register(Tag)
