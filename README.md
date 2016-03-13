# **Plan for HemeWeb (Tentative Name)**

# Shortcut / Table of Contents
* [Important Dates](#important-dates)
* [Motivation](#motivation)
* [Current Workflow](#current-workflow)
* [Plan of Attack](#plan-of-attack)
* [Risks](#risks)
* [Other Related Issues](#other-related-issues)
* [Resources](#resources)


## Important Dates

1. **31st March 2016**, Due date of AWS research grant, See other
   related issue A)
2. **15th April 2016**, Due date of Informatics Research Proposal
3. **2nd June 2016**, Official start of work on the projects
4. **Early July**, Presentation of project progress to peer
5. **19th August 2016**, Noon, deadline for dissertation submission



## Motivation

[HemeLB](https://github.com/UCL/hemelb) currently run on ARCHER super
computer. The exclusitivity of the resource coupled with the long list
of dependencies and technical know-how, limit the access of doing the
simulation by the domain experts like scientist or doctor.

This project is an arrangement to solve this problem. Decouple the
components of the simulation and provide a web interface so that people
could upload necessary files easily and do the simulation without
knowing the technical know-how. Also, running it on the cloud will also
means that this project is capable to be run on the commodity servers
that people could easily replicate the simulation or workflow on any
other capable fleet of servers without resorting to supercomputers.


# Current Workflow

To understand how we could improve the workflow better, we need to
understand the current workflow.

### Current life cycle of the workflow


![alt text](resources/images/HemeLB-workflow.png "HemeLB current workflow")




## Plan of Attack
These are the steps we are going to take for this project:

### 1) Separate HemeLB core into its own container
This is a straight-forward step. Whatever the implementation in the end, having HemeLB on its own container, separately from the container which contains the whole workflow from setup step is better. We want to have a HemeLB-core only clusters that do not need other part.

**Decision Point!**
a)  (Adam asked) Do we even need docker container? Yes, the purpose of having HemeLB core packaged into its own container on dockerhub is that people can easily install HemeLB core on their own. It's not a required step for this project to be successful, but it will benefit the community for easy distribution of HemeLB core.

### 2) Orchestrate the deployment of HemeLB cluster

We need tools to deploy HemeLB core as a compute server in AWS easily. There are few possible tools:

1. CfnClusters, basically python CLI with boto lib, optimized for HPC, [doc](http://cfncluster.readthedocs.org/en/latest/hello_world.html)
2. Ansible, more general-purpose system automation, [Ansible-Docker](https://www.ansible.com/docker)
3. Chef [doc](https://www.chef.io/chef/)
4. Other deployment tools

**Decision Point!**
Decide which tools is more appropriate for the task of deploying the cluster

### 3) Develop web interface to accept user input

This web interface should receive two files(.xml + .gmy) that will be
fed to the HemeLB core clusters. After simulation is done, an .xpf file
will be available for download to the user.


### Checkpoint

The system should look like this:

![alt text](resources/images/HemeWeb-phase-1.png "Phase 1 of HemeWeb")


### 4) Extends HemeWeb to handle geometry generation workflow

The planned approach is for the web interface to receive upload from the
user in forms of .stl and .pr2 files. The web server then will spun up
a docker container in a new EC2 instance or some kind of reserved
instances specially used for docker containers. User will then get
access to the docker container via [noVNC](https://github.com/kanaka/noVNC) 
and proceed to do geometry generation inside the container.

Once the geometry generation is done, the resulting .xml and .gmy file
will be fed into the HemeLB cluster to run the simulation.

### Checkpoint

The system should look like this at this point:

![alt text](resources/images/HemeWeb-phase-2.png "Phase 2 of HemeWeb")


### 5) Extends HemeWeb to handle domain definition step or even Viewing of HemeLB simulation result

There are two possible extension possible at this point. First, we
accomodate even farther the pre-processing step. Allowing users to
generate the STL file only and do the domain definition step (GPU
Intensive) to generate .stl + .pr2 files that is used in step 4). Or
alternatively, we could do the post-processing step that allow the user
to view the result of the simulation to be viewed on the browser
directly.




## Risks

As with all projects with limited time and budget, there are risks
involved in planning the project. Result of the project does not always
accurately fit what we have planned.

This project is structured in such a way that minimize the
risk of having nothing at the end of the dissertation period. We
decoupled the components and plan on working the most important
component first, the HemeLB container cluster and web interface.

After we finished the first phase, have everything working, then we
could take a crack at other components of the workflow, which is the
geometry generations. This way, we could plan for the project to
"degrade gracefully" if the plan does not work perfectly.



## Other related issues

### A) Intellectual Property issues with Indonesia Endowment Fund for Education(LPDP)
I have to make sure that we are on the clear on the IP issues. HemeLB is in LGPL3, so HemeWeb should also be LGPL3. Will the Indonesia Endowment Fund for Education be okay with having their name on the web interface and my dissertation report (Some kind of *"This project is supported/funded by the Indonesia Endowment Fund for Education(LPDP)"*)? Technically, as per license, they can not prevent somebody working on them in the future.

Also the source of funding, will research grant from AWS be a problem?
If it is a problem, I should use the allocated budget for my
dissertation, but then will that be okay?

**Status**
Got through the Customer Service Officer, She explained that they would
prefer for me to use my allocated budget for dissertation. But when
asked about the IP related questions, she referred me to the higher ups.

The higher ups are "not sure" since she didn't really understand legal
repercussion of open source software, but in her opinion, it should not
be a problem, and she prefered me to use my allocated budget for
disertation. She will check with the legal team first before writing
formal response to my email.




## Resources

### Papers

* ✓ [Shifter Paper](https://www.nersc.gov/assets/Uploads/cug2015udi.pdf)
* ✓ [Shifter Press release](https://www.nersc.gov/news-publications/nersc-news/nersc-center-news/2015/shifter-makes-container-based-hpc-a-breeze/)
* ✓ [Nekkloud: A Software Environment for High-order
Finite Element Analysis on Clusters and Clouds](https://www.chriscantwell.co.uk/wp-content/uploads/2013/09/nekkloud.pdf)
* [Massively parallel fluid simulations on
Amazon’s HPC cloud](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=6123441)
* ✓ [Performance Evaluation of Amazon EC2 for NASA HPC Applications ](http://dl.acm.org/citation.cfm?id=2287045)

---
### Filesystem related stuff

* [sshfs](https://www.digitalocean.com/community/tutorials/how-to-use-sshfs-to-mount-remote-file-systems-over-ssh)
* [aws elastic file storage, preview state](https://aws.amazon.com/efs/)

---
### Others
* CFD Direct, [link](http://cfd.direct/cloud/) << Not sure what to do with this yet
