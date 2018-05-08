from django.contrib import admin
from .models import Action, Condition, Element, Screen, Tag, TestCase, TestData, TestStep


class TestCaseAdmin(admin.ModelAdmin):
	exclude = ('slug',)
	list_display = ('title', 'priority', 'created', 'edited', )
	list_filter = ('priority', )
	search_fields = ('title', 'description')
		
admin.site.register(Action)
admin.site.register(Condition)
admin.site.register(Element)
admin.site.register(Screen)
admin.site.register(Tag)
admin.site.register(TestStep)
admin.site.register(TestData)
admin.site.register(TestCase, TestCaseAdmin)

