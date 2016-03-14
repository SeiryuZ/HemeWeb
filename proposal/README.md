# Informatic Research Proposal - Docker-based high performance computing in the cloud

## Motivation

High Performance Computing (HPC) is traditionally done in a high
performance computing infrastructures like cluster of computation nodes or
supercomputers. This setup allows some complex computation, for example
scientific computation like blood flow simulation, to be done in a high
performing fashion that normal consumer desktip computers cannot achieve.

Due to this high startup cost, many computation on a scientific research scenario are tied down to the
setup that the research is done on, for example HemeLB paper that run
the simulation on Cray XT3 MPP TerraGrid Machine located on Pittsburgh,
and Cray XT4 at University of Edinburgh[1]. To validate the result of the
research, People need to have access to the similar computational resources
which is often gated by institutions toward their members, like
government or university, or highly costly if want to be replicated
privately. Moreover, complex setup process and toolings provided further
discourage people from replicating scientific computing research
results.

Some research have tried to overcome this limitations by utilizing the
power of cloud computing. Galaxy[2], for example tried to be
the web-based reproducible research platform that
allows everyon to compose, run, and share results of the research to
everyone using the power of cloud computing. However, the degree of the
computations configurations are limited to the resources that are available to the
computing infrastructure and tools provided by Galaxy project.

We need a better way to compose our high performance computing resources
so that we are not restrained by what exist on the running
infrastructure or tools provided by said project. Docker container could
be the answer for this problem. Docker container is virtualized linux
container that can be shared easily. Computing resources or tools could
be easily baked into a docker container image, pushed to the docker hub
and duplicated by everyone easily. This is a perfect answer to the problem of 
composing computational research scenario. Researchers should be able to
package all of their tools into a docker container, publish it and run
it on the cloud to produce the desired results. This scenario then can
be shared, via url, to the scientific community so that people could run
their own computation with the exact same resources. Or, more
importantly, people could inspect the tools and settings so that they
can fiddle around to understand the research better.

Using docker container, allows the running infrastructure to simply
don't care what the underlying implementation details of the
computations. User could just run






## Background

This has been the condition for past decades [?] because access of
computational power is hard to acquire back then [?]. Currently, with
the introduction of new computational service such as Infrastructure as
A Service, Hardware as a Service, cloud computing has allowed people to
acquire this resources easily and dynamically.


## Methodology

## Main Claim

X is better than Y on task Z along some dimension W

Docker-based HPC computing in cloud is better than supercomputer on
scientific computing along some dimension of usability, openess,
replicability

**How to support this claim** Theoritical ? Experimental?


## Expected Outcome

Working prototype that enable HPC computing to be done in the cloud,
that enable the computations to be done easily (usable), shared
(replicable), and inspected (openness).

On this project, the main example of the application to be used is
HemeLB.

## References

[1] HemeLB: A high performance parallel lattice-Boltzmann code for large scale fluid flow in complex geometries
[2] Galaxy: Data intesive science for everyone - https://github.com/galaxyproject/galaxy
