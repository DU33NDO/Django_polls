from django import template


register = template.Library()


@register.filter()
def custom_add(value, name="lolollololol"):
    return f"{value}: {name}"


@register.filter()
def back_title(string: str):
    return string[:-1] + string[-1].upper()


@register.simple_tag(takes_context=True)
def hello_dude(context, name, *args):
    return f"<div>Hello - {name}</div>"


# register.filter('custom_add', custom_add)
