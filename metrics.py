import operator
import subprocess
import shlex
from functools import reduce

def get_average_cpu_usage():
  cpu_usage = []

  nodes = get_agent_nodes()
  for node in nodes:
    cpu_usage.append(get_node_cpu_usage(node))
  
  return reduce(lambda x, y: x + y, cpu_usage) / len(cpu_usage)

def get_agent_nodes():
  proc1 = subprocess.Popen(shlex.split('kubectl get nodes'),stdout=subprocess.PIPE)
  proc2 = subprocess.Popen(shlex.split("awk '{print $1}'"),stdin=proc1.stdout,
                          stdout=subprocess.PIPE)
  proc3 = subprocess.Popen(shlex.split('grep agent'), stdin=proc2.stdout,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

  proc1.stdout.close() # Allow proc1 to receive a SIGPIPE if proc2 exits.
  proc2.stdout.close()
  out,err=proc3.communicate()
  return out.decode("utf-8").splitlines()

def get_node_cpu_usage(node):
  proc1 = subprocess.Popen(shlex.split('kubectl top nodes {}'.format(node)),stdout=subprocess.PIPE)
  proc2 = subprocess.Popen(shlex.split('grep [0-9]'),stdin=proc1.stdout,stdout=subprocess.PIPE)
  proc3 = subprocess.Popen(shlex.split("awk '{print $3}'"),stdin=proc2.stdout,
                        stdout=subprocess.PIPE)
  proc1.stdout.close() 
  proc2.stdout.close() 
  out,err=proc3.communicate()
  return int(out.decode("utf-8").replace("%","").rstrip())
  