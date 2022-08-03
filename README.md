# Nautobot IP Services Plugin

Nautobot natively provides the ability to add Services such as TCP/UDP ports that are exposed on an Interface of a Device using the "Assign service" button on the Device view. The Services can also optionally be assigned to an IP address from the Device view.  This plugin for [Nautobot](https://www.github.com/nautobot) extends the functionality by adding the ability to view and add Services from the IP Address view in IPAM.  
  
With the plugin installed, users can see the list of services associated with an IP address in IPAM.

![image](https://user-images.githubusercontent.com/6945229/182711099-9d07c716-a8a0-44f0-93eb-7d2763f77388.png)

In addition, users can also use the `Assign service` button to define new Services associated with the IP Address.  The IP address from the previous IP Address view is automatically programmed into the `IP Addresses` field on the form. 

![image](https://user-images.githubusercontent.com/6945229/182711414-a1f1636f-74cc-4d67-ba69-0867263e9076.png)

## Setup
1. Install the package on the Nautobot server:
```bash
pip install nautobot-plugin-ip-services
```
  
2. Add plugin to `PLUGINS` in `nautobot_config.py`:
```python
PLUGINS = [
    "nautobot-plugin-ip-services",
]
```
3. Restart the Nautobot services:
```bash
sudo systemctl restart nautobot nautobot-worker nautobot-scheduler 
```


