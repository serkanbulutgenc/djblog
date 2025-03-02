### Form

```python
from django import  forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="your name", max_length=100)

```

This defines a Form class with a single field(your_name).

A Form instance has an `is_valid()` method, which runs validation routines for all its fields. When this method is called, if all fields contain valid data, it will:

- return `True`
- place the form’s data in its `cleaned_data` attribute.

#### The View

Form data sent back to a Django website is processed by a view, generally the same view which published the form. This allows us to reuse some of the same logic.

```python
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "name.html", {"form": form})


```

#### Looping over form's fields

```python
{% for field in form %}
    <div class="fieldWrapper">
        {{ field.errors }}
        {{ field.label_tag }} {{ field }}
        {% if field.help_text %}
          <p class="help" id="{{ field.auto_id }}_helptext">
            {{ field.help_text|safe }}
          </p>
        {% endif %}
    </div>
{% endfor %}
```

Useful attributes on {{ field }} include:

- {{ field.errors }}
- {{ field.field }}
- {{ field.help_text }}
- {{ field.html_name }}
- {{ field.id_for_label }}
- {{ field.is_hidden }}
- {{ field.label }}
- {{ field.label_tag }}
- {{ field.legend_tag }}
- {{ field.use_fieldset }}
- {{ field.value }}

## ModelForm

```python

from django.forms import ModelForm
from myapp.models import Article

# Create the form class.
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["pub_date", "headline", "content", "reporter"]

# Creating a form to add an article.
form = ArticleForm()

# Creating a form to change an existing article.
article = Article.objects.get(pk=1)
form = ArticleForm(instance=article)

```

The generated Form class will have a form field for every model field specified, in the order specified in the fields attribute.

Just like normal form validation, model form validation is triggered implicitly when calling `is_valid()` or accessing the errors attribute and explicitly when calling `full_clean()`, although you will typically not use the latter method in practice.

You can override the `clean()` method on a model form to provide additional validation in the same way you can on a normal form.

Error messages defined at the form field level or at the form Meta level always take precedence over the error messages defined at the model field level.

Every ModelForm also has a save() method. This method creates and saves a database object from the data bound to the form.

```python
>>> from myapp.models import Article
>>> from myapp.forms import ArticleForm

# Create a form instance from POST data.
>>> f = ArticleForm(request.POST)

# Save a new Article object from the form's data.
>>> new_article = f.save()

# Create a form to edit an existing Article, but use
# POST data to populate the form.
>>> a = Article.objects.get(pk=1)
>>> f = ArticleForm(request.POST, instance=a)
>>> f.save()
```

**Selecting the fields to use**

It is strongly recommended that you explicitly set all fields that should be edited in the form using the fields attribute.

** Overriding the default fields **

```python
from django.utils.translation import gettext_lazy as _


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["name", "title", "birth_date"]
        labels = {
            "name": _("Writer"),
        }
        help_texts = {
            "name": _("Some useful help text."),
        }
        error_messages = {
            "name": {
                "max_length": _("This writer's name is too long."),
            },
        }
```
