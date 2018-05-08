from django.db import models
from django.template.defaultfilters import slugify




class Screen(object):
	title = models.CharField(max_length = 250)

	def save(self, arg):
		super(Screen, self).save()
		self.arg = arg

	def __str__(self):
		return self.title




class Element(object):
	title = models.CharField(max_length = 250)
	screen = models.ManyToManyField(Screen)
	
	def save(self, arg):
		super(Element, self).save()
		self.arg = arg

	def __str__(self):
		return self.title




class TestData(object):
	data = models.CharField(max_length = 250)

	def save(self, arg):
		super(TestData, self).save()
		self.arg = arg

	def __str__(self):
		return self.data




class Action(object):
	title = models.CharField(max_length = 250)
	element = models.ManyToManyField(Element)
	testdata = models.ForeignKey(TestData)

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

	def save(self, arg):
		super(Condition, self).save()
		self.arg = arg

	def __str__(self):
		return self.title




class TestStep(object):
	title = models.CharField(required=False, blank=True, null=True)
	condition = models.ForeignKey(Condition)
	expresult = models.TextField()

	def save(self, arg):
		super(TestStep, self).save()
		self.arg = arg
		
	def __str__(self):
		return self.title




class Tag(object):
	title = models.CharField(max_length = 250)

	def save(self, arg):
		super(Tag, self).save()
		self.arg = arg

	def __str__(self):
		return self.title



		
class TestCase(object):
	PRIORITY_CHOICES = (
			('Smoke', 'Smoke'),
			('General', 'General'),
			('Detailed', 'Detailed'),
		)
	title = models.CharField(max_length = 250)
	description = models.TextField()
	condition = models.ManyToManyField(Condition)
	teststep = models.ManyToManyField(TestStep)
	tag = models.ManyToManyFnfvield(Tag)
	priority = models.CharField(max_length = 10, default = 'Smoke', choices = PRIORITY_CHOICES)
	created = models.DateTimeField(auto_now_add = True)
	edited = models.DateTimeField(auto_now = True)
	slug = models.SlugField(max_length = 250, unique = True)

	def save(self, arg):
		self.slug = slugify(self.title)
		super(TestCase, self).save()
		self.arg = arg

	def __str__(self):
		return self.title
