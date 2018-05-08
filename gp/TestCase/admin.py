from django.contrib import admin
from .models import Action, Condition, Element, Screen, Tag, TestCase, TestData, TestStep



admin.site.register(Action)
admin.site.register(Condition)
admin.site.register(Element)
admin.site.register(Screen)
admin.site.register(Tag)
admin.site.register(TestStep)
admin.site.register(TestCase)
admin.site.register(TestData)

