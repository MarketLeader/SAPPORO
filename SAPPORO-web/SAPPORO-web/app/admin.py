# coding: utf-8
from django.contrib import admin
from app.models import Service
from app.models import WorkflowEngine
from app.models import WorkflowType
from app.models import SupportedWesVersion
from app.models import StateCount
from app.models import Workflow
from app.models import WorkflowParameter
# from app.models import Run

admin.site.register(Service)
admin.site.register(WorkflowEngine)
admin.site.register(WorkflowType)
admin.site.register(SupportedWesVersion)
admin.site.register(StateCount)
admin.site.register(Workflow)
admin.site.register(WorkflowParameter)
# admin.site.register(Run)