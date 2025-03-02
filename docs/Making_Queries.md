### Making Queries

Creating and Saving Objects

```python
b = Blog(name="Blog name", tagline="All the latest")
b.save() # create new blog into database
b.name = "New blog name"
b.save() # Updates the blog name

>>> entry = Entry.objects.get(pk=1)
>>> cheese_blog = Blog.objects.get(name="Cheddar Talk")
>>> entry.blog = cheese_blog # ForeignKeyField
>>> entry.save()

>>> john = Author.objects.create(name="John")
>>> paul = Author.objects.create(name="Paul")
>>> george = Author.objects.create(name="George")
>>> ringo = Author.objects.create(name="Ringo")
>>> entry.authors.add(john, paul, george, ringo) #ManyToManyField

```

#### Retrieving objects

To retrieve objects from your database, construct a QuerySet via a Manager on your model class.

```python
Entry.objects.all() # Returns a QuerySet of all objects in the database
Entry.objects.filter(pub_date__year=2006) # Returns a QuerySet of all objects in the database
Entry.objects.exclude(rating__lt=2) # REturns a Queryset all entries except that the rating score less than 2
Entry.objects.get(pk=1)# returns the object directly
Entry.objects.all()[5:10] # Limiting the results

```

#### Field Lookups

Field lookups are how you specify the meat of an SQL WHERE clause. They’re specified as keyword arguments to the QuerySet methods filter(), exclude() and get().
Basic lookups keyword arguments take the form `field__lookuptype=value`. (That’s a double-underscore). For example:

```python
Entry.objects.filter(pub_date__lte="2006-01-01")
Entry.objects.filter(headline_text__exact="Cat bites dog") #Exact match explicit form
Entry.objects.filter(id=14) #__exact is implied
Blog.objects.get(name__iexact='beatles blog') #case-insensitive match
Blog.objects.get(headline__contains='Lennon') #case sensitive containment
Blog.objects.get(headline__icontains='lennon') #case-insensitive containment
Blog.objects.get(headline__startswith='smt') #case-sensitive
Blog.objects.get(headline__endswith='smt') #case-sensitive
Blog.objects.get(headline__istartswith='smt') #case-insensitive
Blog.objects.get(headline__iendswith='smt') #case-insensitive
Entry.objects.filter(blog__name="Beatles blog") #Retrieves all Entry objects with a Blog whose name is 'Beatles Blog'
Blog.objects.filter(entry__headline__contains="Lennon", entry__pub_date__year=2008)


```

#### Filters can reference fields on the model

Django provides F expressions to allow such comparisons. Instances of F() act as a reference to a model field within a query. These references can then be used in query filters to compare the values of two different fields on the same model instance.

Django supports the use of addition, subtraction, multiplication, division, modulo, and power arithmetic with F() objects, both with constants and with other F() objects.

```python
from django.db.models import F

Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks'))
Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks')*2)
Entry.objects.filter(authors__name=F('blog__name'))
```

#### Complex lookups with Q objects

Keyword argument queries – in filter(), etc. – are “AND”ed together. If you need to execute more complex queries (for example, queries with OR statements), you can use Q objects.

Q objects can be combined using the &, |, and ^ operators. When an operator is used on two Q objects, it yields a new Q object.

Lookup functions can mix the use of Q objects and keyword arguments. All arguments provided to a lookup function (be they keyword arguments or Q objects) are “AND”ed together.

```python
from django.db.models import Q

Q(question__startswith="What")
Q(question__startswith="Who") | Q(question__startswith="What")
Poll.objects.get(
    Q(question__startswith="Who"),
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
)

```

#### Deleting objects

The delete method, conveniently, is named delete().

Note that delete() is the only QuerySet method that is not exposed on a Manager itself.

```python
>>> Entry.objects.filter(pub_date__year=2005).delete()
(5, {'webapp.Entry': 5})
```

#### Updating multiple objects at once

Sometimes you want to set a field to a particular value for all the objects in a QuerySet. You can do this with the update() method. For example:

```python
Entry.objects.filter(pub_date__year=2007).update(headline="Everything is the same")
```

#### Relationships forward and backward

If a model has a ForeignKey, instances of that model will have access to the related (foreign) object via an attribute of the model.

You can override the FOO_set name by setting the related_name parameter in the ForeignKey definition.

```python
e = Entry.objects.get(pk=2)
e.blog #Returns the related Blog object

b =Blog.objects.get(id=1)
b.entry_set.all() #Returns all Entry objects related to Blog

#b.entry_set is a manager that returns Querysets
b.entry_set.filter(headline__contains="Lennon")
b.entry_set.count()

```
