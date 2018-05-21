Classes inside:
Project, Screen, Element, TestData, Action, Condition, Step, TestStep, Tag, TestCase, Cases, TestCycle








Specification for classes:

class Project(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True, default='example')
    slug = models.SlugField(max_length=250, unique=True, default='example')

class Screen(models.Model):
    title = models.CharField(max_length=250)
    project = models.ForeignKey(Project, default=1, on_delete=models.CASCADE)
    deeplink = models.CharField(max_length=250, blank=True, null=True, default='deeplink_dflt')

class Element(models.Model):
    title = models.CharField(max_length=250)
    screen = models.ManyToManyField(Screen)
    project = models.ForeignKey(Project, default=1, on_delete=models.CASCADE)
    locator = models.CharField(max_length=250, blank=True, null=True, default='locator_dflt')

class TestData(models.Model):
    data = models.CharField(max_length=250)

class Action(models.Model):
    title = models.CharField(max_length=250)

class Condition(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True, default='somevalue')
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE, blank=True, null=True)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    testdata = models.ForeignKey(TestData, on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(Project, default=1, on_delete=models.CASCADE)

class Step(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True, default='somevalue')
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    expresult = models.TextField()
    project = models.ForeignKey(Project, default=1, on_delete=models.CASCADE)

class TestStep(models.Model):
    step = models.ForeignKey(Step, on_delete=models.CASCADE, blank=True, null=True)
    number = models.BigIntegerField(default=1)

class Tag(models.Model):
    title = models.CharField(max_length=250)

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

class Cases(models.Model):
    testcase = models.ForeignKey(TestCase, on_delete=models.CASCADE, blank=True, null=True)
    check = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)


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