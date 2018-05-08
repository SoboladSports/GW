from django.db import models
from django.template.defaultfilters import slugify


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
	screen = models.ManyToManyField(Screen)
	"""docstring for Element"""
	
	def save(self, arg):
		super(Element, self).save()
		self.arg = arg

	def __str__(self):
		return self.title

class TestData(object):
	data = models.CharField(max_length = 250)

	"""docstring for TestData"""

	def save(self, arg):
		super(TestData, self).save()
		self.arg = arg

	def __str__(self):
		return self.data

class Action(object):
	title = models.CharField(max_length = 250)
	element = models.ManyToManyField(Element)
	testdata = models.ForeignKey(TestData)
	"""docstring for Action"""


	def save(self, arg):
		super(Action, self).save()
		self.arg = arg

	def __str__(self):
		return self.title	

class Condition(object):
	title = models.CharField(required=False, blank=True, null=True)
	screen = models.ForeignKey(Screen)
	element = models.ForeignKey(Element)
	action = models.ForeignKey(Action)
	testdata = models.ForeignKey(TestData)
	#expresult = models.OneToOneField(ExpectedResult)

	"""docstring for Condition"""
	def save(self, arg):
		super(Condition, self).save()
		self.arg = arg

	def __str__(self):
		return self.title

class TestStep(object):
	title = models.CharField(required=False, blank=True, null=True)
	condition = models.ForeignKey(Condition)
	expresult = models.TextField()

	"""docstring for TestStep"""

	def save(self, arg):
		super(TestStep, self).save()
		self.arg = arg
		
	def __str__(self):
		return self.title

class Tag(object):
	title = models.CharField(max_length = 250)
	"""docstring for Tag"""
	def save(self, arg):
		super(Tag, self).save()
		self.arg = arg

	def __str__(self):
		return self.title
		
class TestCase(object):
	title = models.CharField(max_length = 250)
	description = models.TextField()
	condition = models.ManyToManyField(Condition)
	teststep = models.ManyToManyField(TestStep)
	tag = models.ManyToManyField(Tag)


	"""docstring for TestCase"""
	def save(self, arg):
		super(TestCase, self).save()
		self.arg = arg

	def __str__(self):
		return self.title
						
		
		

		




'''
class TestCase(object):
	title = models.CharField(max_length = 250)
	description = models.TextField()
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

'''class ExpectedResult(object):
	text = models.TextField()

	"""docstring for ExpectedResult"""

	def __init__(self, arg):
		super(ExpectedResult, self).__init__()
		self.arg = arg

	def __str__(self):
		return self.text
	'''