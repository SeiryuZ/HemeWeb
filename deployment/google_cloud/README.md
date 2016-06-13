
This is an ansible deployment script for the HemeWeb architecture
specific for GCE



How to use

1. Go to console.cloud.google.com

2. Compute Engine

3. Metadata > SSH Keys, add ssh key to be used

```bash


# Write credentials on secrets.py, make sure this is available on $PYTHONPATH
# It should only contain these lines
# GCE_PARAMS = ('i...@project.googleusercontent.com', '/path/to/project.json')
# GCE_KEYWORD_PARAMS = {'project': 'project_id'}

vim secrets.py


# Disable host key check
export ANSIBLE_HOST_KEY_CHECKING=False


# Provision GCE instances
ansible-playbook provision.yml


# You can dynamically query hostfile with this script
./gce.py --list


# Configure all instances
ansible-playbook -i ./gce.py -u <SSH key user> deploy.yml


# SSH to master node
ssh <ip of master node>


# run HemeLB
mpirun.openmpi --mca btl_tcp_if_include eth0  -np 8  --host hemelb-node-1,hemelb-node-2 hemelb -in /shared/input.xml -out /shared/result/


```
