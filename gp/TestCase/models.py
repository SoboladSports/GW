from django.db import models
from django.template.defaultfilters import slugify


class Project(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True, default='example')
    slug = models.SlugField(max_length=250, unique=True, default='example')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_title(self):
        return self.title

    def get_slug(self):
        return self.slug

    def get_project(self):
        result = {
            'title': self.get_title(),
            'slug': self.get_slug(),
        }

        return result


class Screen(models.Model):
    title = models.CharField(max_length=250)
    project = models.ForeignKey(Project, default=1, on_delete=models.CASCADE)
    deeplink = models.CharField(max_length=250, blank=True, null=True, default='deeplink_dflt')

    def save(self, *args, **kwargs):
        super(Screen, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_title(self):
        return self.title

    def get_project(self):
        return self.project

    def get_deeplink(self):
        return self.deeplink

    def get_screen(self):
        result = {
            'title': self.get_title(),
            'project': self.get_project(),
            'deeplink': self.get_deeplink(),
        }
        return result


class Element(models.Model):
    title = models.CharField(max_length=250)
    screen = models.ManyToManyField(Screen)
    project = models.ForeignKey(Project, default=1, on_delete=models.CASCADE)
    locator = models.CharField(max_length=250, blank=True, null=True, default='locator_dflt')

    def save(self, *args, **kwargs):
        super(Element, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)

    def get_screen(self):
        screens = [t.title for t in self.screen.all()]
        return screens

    def get_title(self):
        return self.title

    def get_project(self):
        return self.project

    def get_locator(self):
        return self.locator

    def get_element(self):
        result = {
            'title': self.get_title(),
            'screen': self.get_screen(),
            'project': self.get_project(),
            'locator': self.get_locator(),
        }
        return result


class TestData(models.Model):
    data = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        super(TestData, self).save(*args, **kwargs)

    def __str__(self):
        return self.data

    def get_data(self):
        return self.data

    def get_testdata(self):
        result = {
            'testdata': self.get_data(),
        }
        return result


class Action(models.Model):
    title = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        super(Action, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_title(self):
        return self.title

    def get_action(self):
        result = {
            'title': self.get_title(),
        }
        return result


class Condition(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True, default='somevalue')
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE, blank=True, null=True)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    testdata = models.ForeignKey(TestData, on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(Project, default=1, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Condition, self).save(*args, **kwargs)

    def __str__(self):
        if (self.title == '' or self.title == "somevalue"):
            return str(str(self.action) + ' ' + str(self.element) + ' at ' + str(self.screen) + ' screen ' + str(
                self.testdata)).replace('None', '').replace('  ', ' ')
        else:
            return str(self.title)

    def get_screen(self):
        return self.screen

    def get_title(self):
        return self.title

    def get_element(self):
        return self.element

    def get_action(self):
        return self.action

    def get_testdata(self):
        return self.testdata

    def get_project(self):
        return self.project

    def get_condition(self):
        result = {
            'title': self.get_title(),
            'screen': self.get_screen(),
            'element': self.get_element(),
            'action': self.get_action(),
            'testdata': self.get_testdata(),
            'project': self.get_project(),
        }
        return result


class Step(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True, default='somevalue')
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    expresult = models.TextField()
    project = models.ForeignKey(Project, default=1, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Step, self).save(*args, **kwargs)

    def __str__(self):
        if (self.title == '' or self.title == 'somevalue'):
            return str(str(self.condition) + ' ' + str(self.expresult)).replace('None', '')
        else:
            return self.title

    def get_title(self):
        return self.title

    def get_condition(self):
        return self.condition

    def get_expresult(self):
        return self.expresult

    def get_project(self):
        return self.project

    def get_teststep(self):
        result = {
            'title': self.get_title(),
            'condition': self.get_condition(),
            'expresult': self.get_expresult(),
            'project': self.get_project(),
        }


class TestStep(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE, blank=True, null=True)
    number = models.BigIntegerField(default=1)

    def __str__(self):
        return str(str(self.number) + ' ' + str(self.step.__str__()))

    def save(self, *args, **kwargs):
        super(TestStep, self).save(*args, **kwargs)

    def get_step(self):
        return self.step


class Tag(models.Model):
    title = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_title(self):
        return self.get_tag()

    def get_tag(self):
        result = {
            'title': self.get_title(),
        }
        return result


class TestCase(models.Model):
    PRIORITY_CHOICES = (
        ('Smoke', 'Smoke'),
        ('General', 'General'),
        ('Detailed', 'Detailed'),
    )
    title = models.CharField(max_length=250)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    condition = models.ManyToManyField(Condition)
    teststep = models.ManyToManyField(TestStep)
    tag = models.ManyToManyField(Tag)
    priority = models.CharField(max_length=10, default='Smoke', choices=PRIORITY_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TestCase, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_title(self):
        return self.title

    def get_project(self):
        return self.project

    def get_description(self):
        return self.description

    def get_slug(self):
        return self.slug

    def get_created(self):
        return self.created

    def get_edited(self):
        return self.edited

    def get_priority(self):
        return self.priority

    def get_tags(self):
        tags = [t.title for t in self.tag.all()]
        return tags

    def get_conditions(self):
        conditions = [t for t in self.condition.all()]
        return conditions

    def get_teststeps(self):
        steps = [t for t in self.teststep.all()]
        return steps

    def get_testcase(self):
        result = {
            'title': self.get_title(),
            'slug': self.get_slug(),
            'project': self.get_project(),
            'description': self.get_description(),
            'condition': self.get_conditions(),
            'teststep': self.get_teststeps(),
            'tag': self.get_tags(),
            'created': self.get_created(),
            'edited': self.get_edited(),
        }
        return result


class Cases(models.Model):
    PRIORITY_CHOICES = (
        ('Passed', 'Passed'),
        ('Failed', 'Failed'),
        ('To be checked', 'To be checked'),
    )
    testcase = models.ForeignKey(TestCase, on_delete=models.CASCADE, blank=True, null=True)
    check = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, default='To be checked', choices=PRIORITY_CHOICES)

    def save(self, *args, **kwargs):
        super(Cases, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.testcase.__str__())

class TestCycle(models.Model):
    PRIORITY_CHOICES = (
        ('Passed', 'Passed'),
        ('Failed', 'Failed'),
        ('Under Construction', 'Under Construction'),
        ('In progress', 'In progress'),
    )
    title = models.CharField(max_length=250)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(default="Some Text")
    slug = models.SlugField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, default='Under Construction', choices=PRIORITY_CHOICES)
    tag = models.ManyToManyField(Tag)
    rcnumber = models.CharField(max_length=10)
    testcase = models.ManyToManyField(Cases)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TestCycle, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_tags(self):
        tags = [t.title for t in self.tag.all()]
        return tags