import ray
import os
import sys

ray.init(address='auto')
nodes_info = ray.nodes()
cpu_nodes = [n['NodeManagerAddress'] for n in nodes_info if not 'GPU' in n["Resources"].keys()]
gpu_nodes = [n['NodeManagerAddress'] for n in nodes_info if 'GPU' in n["Resources"].keys()]

nworkers = int(sys.argv[1])
assert(nworkers <= min(len(cpu_nodes), len(gpu_nodes))), "Cannot provide this many workers"

with open(f'hosts{nworkers}', 'w') as f:
    f.write('\n'.join(cpu_nodes[0:nworkers] + gpu_nodes[0:nworkers]))

# os.system("cat hosts")
os.system('xargs -a hosts -n 1 ssh-keygen -f "/home/ubuntu/.ssh/known_hosts" -R')
