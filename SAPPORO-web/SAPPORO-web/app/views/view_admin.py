# coding: utf-8
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.generic import View

from app.forms import ServiceAdditionForm
from app.models import Service, Workflow


class AdminHomeView(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        if not request.user.is_superuser:
            raise PermissionDenied

        return render(request, "app/admin_home.html")


class AdminServiceView(LoginRequiredMixin, View):
    raise_exception = True

    def get(self, request):
        if not request.user.is_superuser:
            raise PermissionDenied
        service_addition_form = ServiceAdditionForm()

        return self.general_render(request, service_addition_form)

    def post(self, request):
        if not request.user.is_superuser:
            raise PermissionDenied
        if request.POST.get("button_add_service"):
            service_addition_form = ServiceAdditionForm(request.POST)
            if service_addition_form.is_valid():
                service = Service()
                service.name = service_addition_form.cleaned_data["service_name"]
                service.api_server_url = service_addition_form.cleaned_data["api_server_url"]
                d_res = service.get_dict_response()
                service.insert_from_dict_response(d_res)
                service.save()
                l_workflow_d_res = service.get_workflows_dict_response()[
                    "workflows"]
                for workflow_d_res in l_workflow_d_res:
                    workflow = Workflow()
                    workflow.insert_from_dict_response(service, workflow_d_res)
                    workflow.save()

        elif request.POST.get("button_delete_service"):
            for service_name in request.POST.getlist("delete_check"):
                service = Service.objects.get(name=service_name)
                service.delete()
            service_addition_form = ServiceAdditionForm()
        else:
            service_addition_form = ServiceAdditionForm()

        return self.general_render(request, service_addition_form)

    def general_render(self, request, service_addition_form):
        services = [service.expand_to_dict()
                    for service in Service.objects.all()]
        context = {
            "services": services,
            "service_addition_form": service_addition_form,
        }
        return render(request, "app/admin_service.html", context)