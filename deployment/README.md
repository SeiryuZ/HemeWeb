# HemeWeb deployment scripts
# Work in progress

This is an ansible deployment script for the HemeWeb architecture.

** Do not use the default insecure key on production **


How to use

```bash

# Install required openssl on your system


# Make virtual env for the development environment (optional)
mkvirtualenv hemeweb_deploy


# Install all the needed tools for deployment
pip install -r requirements.txt



# This if for manual stuff
# Update the hostsfile before running this command
# All the hosts need to be connected by private networking options,
# or OpenMPI will complain
vim hostsfile


# Deploy
export ANSIBLE_HOST_KEY_CHECKING=False; ansible-playbook -i hostsfile deploy.yml

# SSH to manager node
ssh ...

# run HemeLB
mpirun.openmpi --mca btl_tcp_if_include eth0  -np 8  --host hemelb-node-1,hemelb-node-2 hemelb -in /shared/input.xml -out /shared/result/

```
