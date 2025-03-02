### Models

A model is the single definitive of information about your data.

```python
from django.db import models

class Person(models.Model):
    first_name = model.CharField("optional verbosename",max_length=30)
    last_name = model.CharField(max_length=50)

    class Meta:
        ordering=['last_name']

```

Each field in your model should be an instance of the appropriate Field class.(column type, widget, validation)

#### Field Options

null, blank, choices, default, db_default, help_text, primary_key, unique

#### Realationship

###### Many-to-one relationships

```python
from django.db import models

class Manufacturer(model.Model):
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    #...
```

It’s suggested, but not required, that the name of a ForeignKey field (_manufacturer in the example above_) be the name of the model, lowercase.

###### Many-to-many relationships

```python
from django.db import models

class Topping(model.Model):
    pass

class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)
    #...
```

It’s suggested, but not required, that the name of a ManyToManyField (toppings in the example above) be a plural describing the set of related model objects.
Generally, ManyToManyField instances should go in the object that’s going to be edited on a form.

###### Extra fields on many-to-many relationships

Django allows you to specify the model that will be used to govern the many-to-many relationship. You can then put extra fields on the intermediate model.

```python
from django.db import models

class Person(model.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class MemberShip(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
    #...

ringo = Person.objects.create(name='Ringo')
paul = Person.objects.create(name='Paul')
beatles = Group.objects.create(name='The beatles')

m1 = Membership(person=ringo, group=beatles, date_joined=date(1962.8.16), invite_reason='Needs')
m1.save()

beatles.members.all()

beatles.members.add(john, through_defaults={"date_joined": date(1960, 8, 1)})
beatles.members.create(name="George Harrison", through_defaults={"date_joined": date(1960, 8, 1)})
beatles.members.set([john, paul, ringo, george], through_defaults={"date_joined": date(1960, 8, 1)})

Group.objects.filter(members__name__startswith="Paul")


# Beatles have broken up
beatles.members.clear()
# Note that this deletes the intermediate model instances
Membership.objects.all()

```

You can also use add(), create(), or set() to create relationships, as long as you specify through_defaults for any required fields:

### Meta Options

```python
from django.db import models


class Ox(models.Model):
    horn_length = models.IntegerField()

    class Meta:
        ordering = ["horn_length"]
        verbose_name_plural = "oxen"
        verbose_name=""
        app_label=""
        abstract=True
        db_table="db_name"
        get_latest_by="field_name"
        permissions=[("can_deliver_pizzas", "Can deliver pizzas")]
        default_permissions=('add', 'change', 'delete', 'view')
        proxy=True
        indexes=[
            models.Index(fields=["last_name", "first_name"]),
            models.Index(fields=["first_name"], name="first_name_idx"),
        ]
        unique_together = [["driver", "restaurant"]]
```

#### Model attributes

**objects**

The most important attribute of a model is the Manager. It’s the interface through which database query operations are provided to Django models and is used to retrieve the instances from the database. If no custom Manager is defined, the default name is objects. Managers are only accessible via model classes, not the model instances.

#### Model methods

Define custom methods on a model to add custom “row-level” functionality to your objects.

```python
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    @property
    def full_name(self):
        "Returns the person's full name"
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        "This tells Django how to calculate the URL for an object"
        return 'some/path/object_id'

    def save(self, **kwargs):
        do_something()
        super().save(**kwargs) #Call the real save() method
        do_something_else()

    def delete(self, **kwargs):
        super().delete(**kwargs)

```

#### Model inheritance

- Often, you will just want to use the parent class to hold information that you don’t want to have to type out for each child model. This class isn’t going to ever be used in isolation, so Abstract base classes are what you’re after.
- If you’re subclassing an existing model (perhaps something from another application entirely) and want each model to have its own database table, Multi-table inheritance is the way to go.
- Finally, if you only want to modify the Python-level behavior of a model, without changing the models fields in any way, you can use Proxy models.

```python
from django.db import models


class CommonInfo(models.Model):
    # ...
    class Meta:
        abstract = True
        ordering = ["name"]


class Student(CommonInfo):
    # ...
    class Meta(CommonInfo.Meta):
        db_table = "student_info"


#Proxy method
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class MyPerson(Person):
    class Meta:
        proxy = True

    def do_something(self):
        # ...
        pass
```
