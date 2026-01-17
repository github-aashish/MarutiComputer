from django import template
from urllib.parse import urlencode
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag(takes_context=True)
def sort_col(context, field, label):
    request = context["request"]
    params = request.GET.copy()

    # Remove previous sorting values
    params.pop("sort", None)
    params.pop("ord", None)

    current_sort = request.GET.get("sort")
    current_ord = request.GET.get("ord", "asc")

    # Toggle order
    if current_sort == field:
        new_order = "desc" if current_ord == "asc" else "asc"
    else:
        new_order = "asc"

    params["sort"] = field
    params["ord"] = new_order

    url = f"?{urlencode(params)}"

    # FontAwesome icons
    icon = ""
    if current_sort == field:
        if current_ord == "asc":
            icon = '<i class="fa-solid fa-sort-up ms-1"></i>'
        else:
            icon = '<i class="fa-solid fa-sort-down ms-1"></i>'

    tooltip = f"Sort by {label}"

    html = f"""
    <a href="{url}" 
       data-bs-toggle="tooltip"
       title="{tooltip}" 
       class="sort-header d-flex align-items-center gap-1"
       style="text-decoration:none; color:inherit;">
        <span>{label}</span>
        {icon}
    </a>
    """

    return mark_safe(html)
