from azure.mgmt.compute import ComputeManagementClient
from azure.cli.core.commands.client_factory import get_mgmt_service_client

a = get_mgmt_service_client(ComputeManagementClient).container_services
print(a)
