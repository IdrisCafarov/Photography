from blog.models import *


def extras(request):
    context = {}
    general_set = GeneralSettings.objects.all()

    context["general_set"] = general_set
    context["contact"] = Contact.objects.all()

    return context