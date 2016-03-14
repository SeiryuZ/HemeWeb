# Informatic Research Proposal - Docker-based high performance computing in the cloud

## Motivation

High Performance Computing (HPC) requires high performing infrastructures
like supercomputers or huge clusters of compute node to be run effectively.
This computational setup allows some complex computation,
usually a scientific computation simulation, to be done in a high
performing fashion that traditional consumer desktop computers cannot achieve.
However acquiring access to this computation resources are not easy, nor
cheap, i.e, you have to be member of a university, government
institute, licensed, or build your own cluster.

In scientific community, especially in scientific computation,
researchers utilize these infrastructures for their research. For
example, HemeLB that utilize Cray XT3 MPP TerraGrid Machine located on Pittsburgh,
and Cray XT4 at University of Edinburgh[1]. These infrastructures,
unfortunately often not available to most people or unfeasible to
replicate. Moreover, complex setup process and toolings needed further
discourage people from replicating computations from these researches.

Galaxy[2], a web-based reproducible research platform is developed to
answer to these issues. It allows its user to compose, customize, run
and share their simulations utilizing cloud computing resources.
However, these computational models are limited to the tools provided by
the web application, Galaxy, and the infrastructures that it rans on
(i.e, OS) which require researches/ computational researches to
understand/ have experience with the toolings provided or create their
own based on the restriction. For example, most of the tools that is ran
on Galaxy, require python script.

<!--Some research have tried to overcome this limitations by utilizing the-->
<!--power of cloud computing. Galaxy[2], for example tried to be-->
<!--the web-based reproducible research platform that-->
<!--allows everyon to compose, run, and share results of the research to-->
<!--everyone using the power of cloud computing. However, the degree of the-->
<!--computations configurations are limited to the resources that are available to the-->
<!--computing infrastructure and tools provided by Galaxy project.-->

Limitation above is the impetus for this project. In an ideal scenario,
researchers do not need to port their computation project to the provided toolings,
environment of an infrastructure of a computational models provider.
Researchers could just compose their computation project with whatever
tools and environment they are comfortable with and run with it. And
this is where docker[3] comes into the picture. Docker allows us to compose
our computation environment and tools as we wanted and allow it to be
shared easily. Our project will utilize this unique trait of docker to
allow researchers compose their computational project as they see fit.

There will be a web interface to set the running parameter of the computations
and to run the project utilizing cloud computing resources. This allows
researchers to be free from tools that they are not familiar with or
specific implementations which is a barrier for replication of project.
Infrastructure choice also become agnostic, our computational node do
not have to install dependencies or tools that each project needs
because it is already packaged in the containers, making the
computational node reusable with different projects without getting
bogged down with tools and variables of all projects.





## Background

* History of Research Computing
* - Grid Computing
* - Cloud Computing

* Scientific Computing
* - Reproducible research
* - Science code manifesto
* - Example of scientific computing



<!--This has been the condition for past decades [?] because access of-->
<!--computational power is hard to acquire back then [?]. Currently, with-->
<!--the introduction of new computational service such as Infrastructure as-->
<!--A Service, Hardware as a Service, cloud computing has allowed people to-->
<!--acquire this resources easily and dynamically.-->


## Methodology

## Main Claim

X is better than Y on task Z along some dimension W

Docker-based HPC computing in cloud is better than supercomputer on
scientific computing along some dimension of usability, openess,
replicability

**How to support this claim** Theoritical ? Experimental?


## Expected Outcome/ Success Criteria

Working prototype that enable HPC computing to be done in the cloud,
that enable the computations to be done easily (usable), shared
(replicable), and inspected (openness).

On this project, the main example of the application to be used is
HemeLB.

## References

[1] HemeLB: A high performance parallel lattice-Boltzmann code for large scale fluid flow in complex geometries

[2] Galaxy: Data intesive science for everyone - https://github.com/galaxyproject/galaxy

[3] Docker - http://www.docker.com/
