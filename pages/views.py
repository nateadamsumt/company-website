from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

def home_page_view(request):
    context = {
        "inventory_list": ["Thing", "Doohickey", "Gadget"],
        "greeting": "Hello! This is Company Website!",
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Place Street"
        context["phone_number"] = "123-456-7890"
        return context