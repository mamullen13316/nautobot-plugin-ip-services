"""Urls for nautobot_plugin_ip_services."""

from django.urls import path

from nautobot_plugin_ip_services import views

urlpatterns = [
    path(
        "devices/<uuid:device>/services/assign/<uuid:ipaddress>/",
        views.CustomServiceEditView.as_view(),
        name="custom_service_edit",
    )
]