### ModelAdmin

```python
from django.contrib import admin


class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = "pub_date"

```

#### ModelAdmin options

```python
# ModelAdmin.actions : List of actions on the change list page
# ModelAdmin.actions_on_top:Boolaen
# ModelAdmin.actions_on_bottom:Boolean
# ModelAdmin.actions_selection_counter:Boolean
# ModelAdmin.date_hierarchy: field_name (Date,DatetimeField)
# ModelAdmin.empty_value_display:field_name or function
# ModelAdmin.exclude:field_name[] to be exclude
# ModelAdmin.fields:simple layout in the add and change page
# ModelAdmin.fieldsets:control the layout of admin add and change page.The 2-tuples are in the format (name, field_options(fields, classes, description))
# ModelAdmin.filter_horizontal:filed_name[]
# ModelAdmin.filter_vertical:filed_name[]
# ModelAdmin.form:the form for add/change pages
# ModelAdmin.inlines:inline forms
# ModelAdmin.list_display:field_names[], a callable that accept one argument, a string representing  a ModelAdmin method, a string representing a model attribute or method
#  ModelAdmin.list_display_links:field_name[]
#  ModelAdmin.list_editable:field_name[]
#  ModelAdmin.list_filter:field_name[]
#  ModelAdmin.list_per_page=int(100)
#  ModelAdmin.list_max_show_all:int(200)
#  ModelAdmin.list_select_related
#  ModelAdmin.ordering:field_name[]
#  ModelAdmin.paginator:paginator_class
#  ModelAdmin.prepopulated_fields:dictionary mapping field names to the fields it should prepopulate from: {'slug':['title']}
# ModelAdmin.show_facets:ShowFacets.ALWAYS, ALLOW, NEVER
#  ModelAdmin.radio_fields:
#  ModelAdmin.autocomplete_fields:must define search_fields
#  ModelAdmin.raw_id_fields:
#  ModelAdmin.readonly_fields:field_name[] will display its data as-is and non-editable;
#  ModelAdmin.save_as:“Save and add another” will be replaced by a “Save as new"
#  ModelAdmin.save_as_continue:bool
#  ModelAdmin.save_on_top:bool
#  ModelAdmin.search_fields:field_name[]
#  ModelAdmin.search_help_text:str
#  ModelAdmin.show_full_result_count:bool(False)
#  ModelAdmin.sortable_by:field_name[]
#  ModelAdmin.view_on_site:str ÷ callable
```

#### ModelAdmin custpm template options

```python
# ModelAdmin.add_form_template
# ModelAdmin.change_form_template
# ModelAdmin.change_list_template
# ModelAdmin.delete_confirmation_template
# ModelAdmin.delete_selected_confirmation_template
# ModelAdmin.object_history_template
# ModelAdmin.popup_response_template
```

#### ModelAdmin methods

```python
# ModelAdmin.save_model(request,obj,form,change)
# ModelAdmin.delete_model(request,obj)
```

#### ModelAdmin methods

```python
class ArticleAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all": ["my_styles.css"],
        }
        js = ["my_code.js"]
```
