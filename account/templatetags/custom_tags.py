from django import template

register = template.Library()

@register.filter(name="get_first")
def get_first(my_dict_values):
    return list(my_dict_values)[0]
