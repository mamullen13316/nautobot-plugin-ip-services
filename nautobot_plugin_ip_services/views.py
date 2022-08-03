"""Views for nautobot-plugin-ip-services."""

from django.shortcuts import get_object_or_404, redirect, render
from nautobot.ipam.forms import ServiceForm
from nautobot.core.views import generic
from nautobot.ipam.models import Service
from nautobot.dcim.models import Device
from nautobot.ipam.models import IPAddress


from nautobot_plugin_ip_services import models

class CustomServiceEditView(generic.ObjectEditView):
    queryset = Service.objects.prefetch_related("ipaddresses")
    model_form = ServiceForm
    template_name = "ipam/service_edit.html"

    def alter_obj(self, obj, request, url_args, url_kwargs):
        if "device" in url_kwargs:
            obj.device = get_object_or_404(Device.objects.restrict(request.user), pk=url_kwargs["device"])
        if "ipaddress" in url_kwargs:
            obj.ipaddr = get_object_or_404(IPAddress.objects.restrict(request.user), pk=url_kwargs["ipaddress"])
            # This code below takes the IP address and defaults it in the IP addresses field of the form
            # See nautobot.core.views.generic.py ObjectEditView class GET method
            # line 384 - initial_data = normalize_querydict(request.GET)
            tempdict = self.request.GET.copy()
            tempdict['ipaddresses'] = obj.ipaddr
            self.request.GET = tempdict
        return obj