from django import template
from ..models import *

register = template.Library()

@register.filter(name='fee_filter')
def fee_filter(formno):
    try:
        fee_structure = fees.objects.get(form_no=formno)
        left = str(fee_structure.due)
    except:
        fee_structure = None
    if fee_structure is not None:
        if left == "0":
            return "NIL"
        else:
            return left
    else:
        return "Not Found"

@register.filter(name='certi_filter')
def certi_filter(formno):
    try:
        cert_object = certificate2.objects.get(regno = formno)
    except:
        cert_object = None

    if cert_object is not None:
        return True
    else:
        return False
