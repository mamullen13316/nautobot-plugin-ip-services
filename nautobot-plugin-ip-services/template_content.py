# template_content.py
from nautobot.extras.plugins import PluginTemplateExtension
from nautobot.ipam.models import Service

class IPServices(PluginTemplateExtension):
    """Template extension to display Services on IP Addresses in IPAM."""

    model = 'ipam.ipaddress'
  
    def right_page(self):
        """Display table on right side of page."""
        self.ipaddr_obj = self.context["object"]
        self.assigned_device = self.ipaddr_obj.assigned_object.device if hasattr(self.ipaddr_obj.assigned_object, 'device') else None

        services = Service.objects.filter(ipaddresses=self.ipaddr_obj)
        self.exposed_services = [{
         "proto": obj.protocol,
         "port": ', '.join(str(port) for port in obj.ports),
         "name": obj.name
         } for obj in services]

        return self.render("nautobot-plugin-ip-services/ipaddress_services.html", extra_context={
            "exposed_services": self.exposed_services,
            "assigned_device": self.assigned_device,
            "ipaddress": self.ipaddr_obj 
            })
    
template_extensions = [IPServices]