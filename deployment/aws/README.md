
This is an ansible deployment script for the HemeWeb architecture
specific for AWS.



How to use

```bash


# Credentials stuff
export AWS_ACCESS_KEY_ID=<put access key>
export AWS_SECRET_ACCESS_KEY=<put secret access key>

# Disable host key check
export ANSIBLE_HOST_KEY_CHECKING=False


# Provision EC2 instances
ansible-playbook provision.yml


# You can dynamically query hostfile with this script
./ec2.py --list


# Configure all instances
ansible-playbook -i ./ec2.py --private-key=<path to private key>  -u ubuntu deploy.yml


# SSH to master node
ssh -i <path to private key> ubuntu@<public-dns-ip-of-master-node>


# run HemeLB
mpirun.openmpi --mca btl_tcp_if_include eth0  -np 8  --host hemelb-node-1,hemelb-node-2 hemelb -in /shared/input.xml -out /shared/result/


```
