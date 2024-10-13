from django.shortcuts import render
from django.views.generic import TemplateView


def functional_view(request):
    return render(request, 'second_task/function_template.html')


class ClassBasedView(TemplateView):
    template_name = 'second_task/class_template.html'
