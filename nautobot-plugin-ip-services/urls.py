"""Urls for nautobot-plugin-ip-services."""

from django.urls import path

from nautobot-plugin-ip-services import views

urlpatterns = [
    path(
        "devices/<uuid:device>/services/assign/<uuid:ipaddress>/",
        views.CustomServiceEditView.as_view(),
        name="custom_service_edit",
    )
]