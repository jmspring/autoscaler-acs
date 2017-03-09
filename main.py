from azure.mgmt.compute import ComputeManagementClient
from azure.cli.core.commands.client_factory import get_mgmt_service_client
from azure.mgmt.compute.models import ContainerServiceOchestratorTypes
from azure.cli.command_modules.acs import acs_client
import sys
import getopt
import login
import os
import metrics

def main(argv):
  username = ''
  password = ''
  service_principal = False
  tenant = ''
  agent_count = 0

  try:
    opts, args = getopt.getopt(argv, "hsu:p:t:c:")
  except getopt.GetoptError:
    print('main.py [-s] -u <username> -p <password>  -t <tenant>')
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print('main.py [-s] -u <username> -p <password> -t <tenant>')
      sys.exit()
    elif opt == '-u':
      username = arg
    elif opt == '-p':
      password = arg
    elif opt == '-s':
      service_principal = True
    elif opt == '-t':
      tenant = arg
    elif opt == '-c':
      agent_count = int(arg)

  login.login(username,password,service_principal,tenant)
  client = get_mgmt_service_client(ComputeManagementClient).container_services
  container_service_name = 'containerservice-kub'
  resource_group_name = 'kub'
  cpu = metrics.get_average_cpu_usage()
  print('average CPU usage: {}'.format(cpu))

  # acs_info = client.get(resource_group_name, container_service_name)
  # kube_config_path = os.path.join(os.path.expanduser('~'), '.kube', 'config')
  # ssh_keyfile_path = os.path.join(os.path.expanduser('~'), '.ssh', 'id_rsa')
  # print(kube_config_path)
  # print(ssh_keyfile_path)
  # _k8s_get_credentials_internal(container_service_name, acs_info, kube_config_path, ssh_keyfile_path)
  # instance.agent_pool_profiles[0].count = agent_count  # pylint: disable=no-member


  # a = client.create_or_update(resource_group_name, container_service_name, instance)
  # a.wait()
  # print(a.result())


# def _k8s_get_credentials_internal(name, acs_info, path, ssh_key_file):
#     dns_prefix = acs_info.master_profile.dns_prefix  # pylint: disable=no-member
#     location = acs_info.location  # pylint: disable=no-member
#     user = acs_info.linux_profile.admin_username  # pylint: disable=no-member
#     _mkdir_p(os.path.dirname(path))

#     path_candidate = path
#     ix = 0
#     while os.path.exists(path_candidate):
#         ix += 1
#         path_candidate = '{}-{}-{}'.format(path, name, ix)

#     # TODO: this only works for public cloud, need other casing for national clouds

#     acs_client.SecureCopy(user, '{}.{}.cloudapp.azure.com'.format(dns_prefix, location),
#                           '.kube/config', path_candidate, key_filename=ssh_key_file)

#     # merge things
#     if path_candidate != path:
#         try:
#             merge_kubernetes_configurations(path, path_candidate)
#         except yaml.YAMLError as exc:
#             logger.warning('Failed to merge credentials to kube config file: %s', exc)
#             logger.warning('The credentials have been saved to %s', path_candidate)



# def _mkdir_p(path):
#     # http://stackoverflow.com/a/600612
#     try:b
#         os.makedirs(path)
#     except OSError as exc:  # Python >2.5
#         pass

# def merge_kubernetes_configurations(existing_file, addition_file):
#     with open(existing_file) as stream:
#         existing = yaml.load(stream)

#     with open(addition_file) as stream:
#         addition = yaml.load(stream)

#     # TODO: this will always add, we should only add if not present
#     existing['clusters'].extend(addition['clusters'])
#     existing['users'].extend(addition['users'])
#     existing['contexts'].extend(addition['contexts'])
#     existing['current-context'] = addition['current-context']

#     with open(existing_file, 'w+') as stream:
#         yaml.dump(existing, stream, default_flow_style=True)
            
# if __name__ == "__main__":
#     main(sys.argv[1:])



