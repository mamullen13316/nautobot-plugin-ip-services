"""nautobot-plugin-ip-services Plugin Initilization."""

from nautobot.extras.plugins import PluginConfig


class NautobotPluginIpServicesConfig(PluginConfig):
    """Plugin configuration for the nautobot-plugin-ip-services plugin."""

    name = "nautobot_plugin_ip_services"  # Raw plugin name; same as the plugin's source directory.
    verbose_name = "nautobot-plugin-ip-services"  # Human-friendly name for the plugin.
    description = "Plugin providing ability to view/add services from an IP Address"
    version = "1.0.0"
    author = "Matt Mullen"
    author_email = "mullenmd@gmail.com"
    base_url = "nautobot-plugin-ip-services"  # (Optional) Base path to use for plugin URLs. Defaulting to app_name.
    required_settings = []  # A list of any configuration parameters that must be defined by the user.
    min_version = "1.0.0"  # Minimum version of Nautobot with which the plugin is compatible.
    max_version = "1.999"  # Maximum version of Nautobot with which the plugin is compatible.
    default_settings = {}  # A dictionary of configuration parameters and their default values.
    caching_config = {}  # Plugin-specific cache configuration.


config = NautobotPluginIpServicesConfig