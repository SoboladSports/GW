from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.

class Screen(object):
	title = models.CharField(max_length = 250)

	"""docstring for Screen"""

	def save(self, arg):
		super(Screen, self).save()
		self.arg = arg

	def __str__(self):
		return self.title

class Element(object):
	title = models.CharField(max_length = 250)
	#screen = models.ManyToManyField(Screen)
	"""docstring for Element"""
	
	def save(self, arg):
		super(Element, self).save()
		self.arg = arg

	def __str__(self):
		return self.title

class Action(object):
	title = models.CharField(max_length = 250)
	#element = models.ManyToManyField(Element)
	"""docstring for Action"""


	def save(self, arg):
		super(Action, self).save()
		self.arg = arg

	def __str__(self):
		return self.title

class TestData(object):
	data = CharField(max_length = 250)

	"""docstring for TestData"""

	def save(self, arg):
		super(TestData, self).save()
		self.arg = arg

	def __str__(self):
		return self.data




class Condition(object):


	"""docstring for Condition"""


	def __init__(self, arg):
		super(Condition, self).__init__()
		self.arg = arg
		
		
		
		

		




'''
class TestCase(object):
	title = models.CharField(max_length = 250)
	description = models.TextField
	created = models.DateTimeField(auto_now_add = True)
	update = models.DateTimeField(auto_now_add = True)
	slug = models.SlugField(max_length = 200, unique = True)


	"""docstring for TestCase"""
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(TestCase, self).save(*args, **kwargs)

	def __str__(self):
		return self.title	
		

'''

