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


class Screen(models.Model):
    title = models.CharField(max_length=250)
    Project = models.ForeignKey(Project, default=1, on_delete=models.CASCADE)
    deeplink = models.CharField(max_length=250, blank=True, null=True, default='deeplink_dflt')

    def save(self, *args, **kwargs):
        super(Screen, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Element(models.Model):
    title = models.CharField(max_length=250)
    screen = models.ManyToManyField(Screen)
    Project = models.ForeignKey(Project, default=1, on_delete=models.CASCADE)
    locator = models.CharField(max_length=250, blank=True, null=True, default='locator_dflt')

    def save(self, *args, **kwargs):
        super(Element, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_screen(self):
        screens = [t.title for t in self.screen.all()]
        return screens


class TestData(models.Model):
    data = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        super(TestData, self).save(*args, **kwargs)

    def __str__(self):
        return self.data


class Action(models.Model):
    title = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        super(Action, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Condition(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True, default='somevalue')
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE, blank=True, null=True)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    testdata = models.ForeignKey(TestData, on_delete=models.CASCADE, blank=True, null=True)
    Project = models.ForeignKey(Project, default=1, on_delete=models.CASCADE)

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


class TestStep(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True, default='somevalue')
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    expresult = models.TextField()
    Project = models.ForeignKey(Project, default=1, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(TestStep, self).save(*args, **kwargs)

    def __str__(self):
        if (self.title == '' or self.title == 'somevalue'):
            return str(str(self.condition) + ' ' + str(self.expresult)).replace('None', '')
        else:
            return self.title


class Tag(models.Model):
    title = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    # class Meta:


#	ordering = ('title',)


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

    def get_tags(self):
        tags = [t.title for t in self.tag.all()]
        return tags

    def get_conditions(self):
        condition = []
        condition.append(self.condition.get_screen)
        return condition

    def get_project(self):
        return self.project
