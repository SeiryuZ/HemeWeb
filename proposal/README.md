# HemeWeb: Container based high performance computing scenario for HemeLB


## Purpose


<!-- HemeLB simulation is reproducible, but not easy  -->
HemeLB [1], a fluid dynamic simulation software that is used for the study of
blood flow, have complex workflow that cause simulation reproduction
challenging. Every simulation requires correctly
configured tools with correct version, parameters and inputs which may be different on each run.
Moreover, minimum computing resources needed by each steps of the
workflow to run efficiently also varies, from consumer-grade computing resources like personal
PC to a highly parallel one like ARCHER supercomputer.
These facts, coupled with the manual documentation of each simulation
configurations, versions, and input files render the simulation
reproduction non-trivial for interested parties. One should get access to
similar computing resources, correctly configure tools, and exact
duplicate of inputs before reproducing the simulation.



<!--HemeLB, a fluid dynamic simulation project that is used for the study of-->
<!--blood flow, currently have workflow that requires varying-->
<!--degree of computational power on each steps. Most notably, the simulation part-->
<!--of HemeLB requires high performing computing resources like-->
<!--ARCHER supercomputer [1] to run effectively, while the-->
<!--setup process for the simulation can be done in consumer-grade computing-->
<!--resources. Exclusivity of computing resources on certain step of the workflow-->
<!--and the overhead of documentation make simulation results done with HemeLB non-trivial to be reproduced.-->
<!--If anyone want to replicate a simulation, one should have the exact same configurations-->
<!--for the simulation  and run the simulation with similar-->
<!--computing resources to the original simulation to replicate it closely.-->
<!--This feat however is not easy, because acquiring acquire access to or-->
<!--building computing resources similar to original simulation might be-->
<!--infeasible.-->

With pushes for reproducible computing research in general [2][3][4], HemeLB
needs to improve its reproducible computing aspect for the benefit of
the simulations that run with it. HemeLB Simulations should  adhere to a higher
standard of validation from the community, making it more transparent
and trustworthy. This trustworthiness is especially more important
when this research area is described in media as an "integral" part in
clinicial decision in the future [6].

In adhering to the reproducible aspect,
the author propose on creating an "extension" to HemeLB called HemeWeb.
HemeWeb will be a web application for HemeLB simulation workflow that
allows interested party to configure and run blood flow simulation on
the cloud, or even, their own computing resources. This extension will
utilize container technology, specifically Docker [7], that allows tools
involved with the workflow to be isolated, inspected, and shared easily
with the publicly available registry. Moreover, docker has been reviewed
to be an appropriate tool for distributing reproducible research, albeit
with few limitations [8]. Thus in this project, the author will create
an experimental web application for HemeLB to address the reproducible
computing aspect of the research using docker.



<!--Current problem - Open Science, Usability, Isolation-->


<!--Current situation - How GalaxyWeb address-->

<!--To showcase the proposed solution, I will develop HemeWeb.-->


<!--High Performance Computing (HPC) requires high performing infrastructures-->
<!--like supercomputers or huge clusters of compute node to be run effectively.-->
<!--This computational setup allows some complex computation,-->
<!--usually a scientific computation simulation, to be done in a high-->
<!--performing fashion that traditional consumer desktop computers cannot achieve.-->
<!--However, acquiring access to this computation resources are neither easy, nor-->
<!--cheap. To acquire access to these resources, you have to be member of a university,-->
<!--government institute, scientists group, or alternatively, build your own cluster.-->

<!--In scientific community, especially in scientific computation,-->
<!--researchers utilize these infrastructures for their research. For-->
<!--example, HemeLB that utilize Cray XT3 MPP TerraGrid Machine located on Pittsburgh,-->
<!--and Cray XT4 at University of Edinburgh [1]. These infrastructures,-->
<!--unfortunately, are not available to most people or unfeasible to-->
<!--replicate. Moreover, complex setup process, configuration and toolings further-->
<!--discourage people from replicating computations from these researches.-->

<!--Galaxy [2], a web-based reproducible research platform is developed to-->
<!--answer to these issues. It allows its user to compose, customize, run-->
<!--and share their simulations utilizing cloud computing resources.-->
<!--However, these computational models are limited to the tools provided by-->
<!--the web application, Galaxy, and the infrastructures that it rans on-->
<!--(i.e, OS) which require researches/ computational researches to-->
<!--understand/ have experience with the toolings provided or create their-->
<!--own based on the restriction. For example, most of the tools that is ran-->
<!--on Galaxy, require python script.-->

<!--Some research have tried to overcome this limitations by utilizing the-->
<!--power of cloud computing. Galaxy[2], for example tried to be-->
<!--the web-based reproducible research platform that-->
<!--allows everyon to compose, run, and share results of the research to-->
<!--everyone using the power of cloud computing. However, the degree of the-->
<!--computations configurations are limited to the resources that are available to the-->
<!--computing infrastructure and tools provided by Galaxy project.-->

<!--Limitation above is the impetus for this project. In an ideal scenario,-->
<!--researchers do not need to port their computation project to the provided toolings,-->
<!--environment of an infrastructure of a computational models provider.-->
<!--Researchers could just compose their computation project with whatever-->
<!--tools and environment they are comfortable with and run with it. And-->
<!--this is where docker [3] comes into the picture. Docker allows us to compose-->
<!--our computation environment and tools as we wanted and allow it to be-->
<!--shared easily. Our project will utilize this unique trait of docker to-->
<!--allow researchers compose their computational project as they see fit.-->

<!--There will be a web interface to set the running parameter of the computations-->
<!--and to run the project utilizing cloud computing resources. This allows-->
<!--researchers to be free from tools that they are not familiar with or-->
<!--specific implementations which is a barrier for replication of project.-->
<!--Infrastructure choic1e also become agnostic, our computational node do-->
<!--not have to install dependencies or tools that each project needs-->
<!--because it is already packaged in the containers and "clean" from each-->
<!--other's dependencies, making the computational node reusable-->
<!--for different projects without getting bogged down with tools-->
<!--and environment variables of all projects.-->




## Background

The proposed system will consists of few key technologies and concept in order to be
working as intended. These key technologies are HemeLB itself,
Cloud computing, and Containerization technology. In this section,
the author will provide a short overview of these technologies and concepts.


**HemeLB and HPC**

<!--Introduction to computational biology and HemeLB-->
Computational biology and bioinformatics are research area that use
mathematical and computational approaches in answering questions and
experiments in biology [5]. These approaches typically involves a
computational workflow which, depending on the type of work,
could varies widely in performance requirement, from normal computational process
that could be done in normal consumer desktop processor to
high-performance scneario that needs to be run on a cluster of computers
or even supercomputer. One example of this type of project is HemeLB, a
vascular blood flow simulation that is used for the study of blood flow [1].
HemeLB have different processes in the workflow that requires different computing power,
from the setup process which can be run on consumer-level computer, to the simulation process
that run on ARCHER supercomputer due to its processing power requirement [1].

This simulation require a highly paralel capabilities of the computing
resources that falls under the category of High Performance Computing.
Traditionally, large computing process could be tackled by two separate
computing paradigm depending on the type of work it needs to do. They
are High Performance Computing and High Throughput Computing. High
performance computing typically involves multiple computing nodes
connected with a high bandwidth network, performing a well-defined
computations that use message passing interface to communicate between
nodes. HPC are typically performed using computer clusters, GPUs, or
even supercomputer. High troughput computing, on the other hand, is a different
paradigm. It allows highly heteregenous computing resources,
often geographically distributed, to cooperate for common goals which
involves different independent computation that can be scheduled independently
and later aggregated on one of the nodes. [Citations on this paragraph
need to be fixed]

Both of these computing paradigm typically requires huge
computing resources available to perform its task effectively. HPC task
like HemeLB especially, are often run on supercomputers, for example ARCHER
supercomputer. This supercomputers requires you to be academics /
researchers with clear proposal, for example how epcc give access to
ARCHER [10]. Another example is PRACE [11], the Partnership for Advanced Computing in Europe,
that allows researcher to access supercomputers accross europe after a
 vetting process. This theoritically allow people with the credentials
to gain access to these resources with the correct motives. However,
reproducing research computation that already been run might not be the
top priority of these facilities when there are many other research
projects that depend on access to these limited resources.

**Cloud Computing**

In answering huge computational power required by researchers and
academics concept called grid computing is envisioned in 1990s [12].
This vision consider computing resources analogous to power grid, where
user should not care from where the resources are acquired and how it is
delivered to the user. What user should see is that there are computing
resources available and it could come from anywhere and in any form.
This paradigm is mainly developed with the interest of researchers and
academia that the business models caters to the most [13]. Grid
computing typically give CPU hours based on the proposal that is vetted
by the institutions. Example of this institution is TeraGrid which
operates until 2011 [14].

Cloud computing share similar vision with grid computing paradigm on how the
computing resources are acquired and delivered are invisible to the
users, but different on the execution of the business model. It is
massively scalable, allow abstract encapsulation of computing resources,
dynamicaly configured and delivered on-demand and most importantly,
driven by economies of scale [13]. Since it is driven by economies of
scale, it is in the interest of cloud providers to provide features
that users actually needs and want to pay for, therefore creating a
tight feedback loop between users and the providers to develop the
platform better than how grid computing handle feature developments.

This has allowed cloud vendors to grow significantly, that in 2013 it
was noted that some cloud vendors could reach more than 90% growth per annum
[15]. These growth further fuels demand and allow them to cut pricing
for their service multiple times [16][17][18] and create more demands.
This development has allowed business or institutions to offload their
computational need to the cloud vendors for a price rather than building their own
infrastructure. This scenario could also be used for our purpose of
reproducing computational research without needing to worry about
preventing other researches getting their share of computational
resource.

Cloud vendors like amazon also capitalize on the need of computing
resources for HPC application that they promote themselves for this capabilities [19].
Running HPC application on cloud vendors, while incurring performance
overhead, are a viable alternative to supercomputers as shown by
the nekkloud project [20], NASA HPC Applications [21], and few other case study [22].
HemeWeb project should also run perfectly fine on cloud infrastructures.


**Containerization technology**

Container technology originated from the virtualization technology back
in 1960. Back then IBM PC shipped with virtualization software that
allow multiple operating systems to be installed into one hardware.
Linux Kernel Container is then born to handle this virtualization but on
the kernel level, where we could have container that run its own kernel
separated from the host. Docker is the technology that pushes the
adoption of this technology to the roof. Docker encapsulate tools and
commands that allow administartion of this container much easier than
before. Making it easy for people to use container in their workflow.
More importantly, docker has a public registry where people could
publish their dockerfile, and share it with the public. Interested
people could just get the file and create their own docker image based
on the published file. This is a huge boon in helping docker become
popular currently.


In reproducing computing researchm docker is deeemed fit to the task,
since it allows computing workflow to be documented, published, and
re-run easily because everyone has the ability to scrutinize it. This
process however, involve an overhead that the author needs to write a
dockerfile instead of doing whatever they are doing currently. However,
this is a small price to pay in order to make compting reproducible
easily. On our case, using docker is a necessary tools. Because with
docker, people could scrutinize the tools and commands used to reproduce
the research done with HemeLB. More importantly, the tools also will
allow us to expand not only handling HemeLB, but also to a more general
case of any other HPC applications to be run on the cloud indepenedent
of what the infrastructure might be.




Work in progress


<!--In dealing with High Performance Computing, infrastructures are-->
<!--typically required to be able to handle multi-core operations easily [4].-->
<!--Be it parallel workload or distributed system workload. This has lead to-->
<!--two separate computing paradigm we know as grid and cluster computing.-->

<!--Cluster computing is a paradigm where two or more computing resources-->
<!--are connected and used concurrently to run a single applications, often-->
<!--the computing resources are made of highly homogenous or similar-->
<!--computing unit mounted in a rack. The type of application run on cluster typically require highly parallel-->
<!--computation like modelling and simulation. This type of application benefits-->
<!--from having a highly interconnected node and data locality that clusters-->
<!--provide [4].-->

<!--On the other hand, Grid computing is a different beast altogether. It-->
<!--allows heterogeneous computing resources, often geographically-->
<!--distributed, to cooperate for a common goals. It is highly dynamic and-->
<!--promis scaling infinitely without regards of physical location of the-->
<!--computing resources [6]. In the UK, grid computing often utilized under-->
<!--the banner of e-science [7], where they provide common middleware,-->
<!--software, and services for scientists to collaborate on their project regardless of physical-->
<!--locations.-->

<!--Both of this type of HPC computing are traditionally done in an in-house-->
<!--manner. Where Universities or government institutions set up a cluster of-->
<!--computing resources or even a supercomputer to do HPC task. Grid-->
<!--computations are also done on in house manner or even utilize public's-->
<!--desktop computer for computational resources, example are the-->
<!--folding@ home and genome@ home projects [8]. Currently however, computing-->
<!--resources are available in the cheap. Cloud computing has entered into-->
<!--the pictures and allow computing resources to be available with a-->
<!--price tag attached to it. It is massively scalable, allow abstract-->
<!--encapsulation of computing resources, dynamically configured,-->
<!--delivered on-demand and driven by economies of scale [5].-->

<!--Cloud computing allowed institutions to offload their pain in procuring-->
<!--and maintaining computing resources to the vendors like Amazon, Google,-->
<!--Microsoft and etc for a price. This price also been reduced multiple times [9][10][11]-->
<!--that comes with economies of scale, making it financially less demanding to-->
<!--run HPC applications without in-house resources. In fact, few HPC-->
<!--applications has been run on the cloud, such as the nekkloud-->
<!--project [12], NASA HPC Applications [13], and few other case study [14]-->
<!--that shows that it is feasible to run HPC applications on the cloud,-->
<!--albeit with performance overhead.-->

<!--This development have make it possible for people or institutions with-->
<!--enough financial means to do some heavy computations without having-->
<!--access to this traditionally expensive in-house computing resources.-->

<!--[need better transition from cloud computing HPC to the push for-->
<!--reproducibility]-->
<!--In scientific computing, there has been a push to make a computational-->
<!--results reproducible even if it is complex [15]. This push make sures that-->
<!--research results adhere to scientific method, that is reproducible by-->
<!--our peers. As traditionally, HPC resources are in-house, this hinders-->
<!--the reproducibility aspect of the research. However, with cloud, this-->
<!--enable people to access this resources more easily, for example:-->
<!--Galaxy [2] that enable people to compose, run, and share their-->
<!--modelling simulation.-->





<!--* History of Research Computing-->
<!--* - Grid Computing-->
<!--* - Cloud Computing-->

<!--* Scientific Computing-->
<!--* - Reproducible research-->
<!--* - Science code manifesto-->
<!--* - Example of scientific computing-->



<!--This has been the condition for past decades [?] because access of-->
<!--computational power is hard to acquire back then [?]. Currently, with-->
<!--the introduction of new computational service such as Infrastructure as-->
<!--A Service, Hardware as a Service, cloud computing has allowed people to-->
<!--acquire this resources easily and dynamically.-->

## Main Claim

This paper will argue that the current HemeLB workflow can be improved
by using a container based HPC in cloud infrastructure approach. This
approach will be better for HemeLB project because it is better in
reproducibility, isolation, openness, and usability.

* **Reproducibility**

  The proposed approach will be better for reproducibility, allowing a
computing process and scenario to be duplicated more easily than status quo.
Currently, to reproduce the computational process, one must get their
hands on the simulation configuration and run the simulation on a similar computing
resources like ARCHER supercomputer which is not easy to replicate nor
cheap. The proposed approach, on the other hand, will store every simulation scenario and
configurations that are run via the web application. These scenarios can be shared
and re-run easily, offering reproducibility to HemeLB computation. In a
more general situation, using container technology also allows reproducibility in
the tools used by any computational workflow. This allow computation
workflow to be reproduced in any computing resources, not only tied into
the implementation this paper will create.

* **Isolation** [Need further discussion]

  Second, proposed approach will be better for isolation issue in HemeLB
computation. Container approach will allow better isolation between
simulation and isolation with the computing environment. This also
demonstrate benefits of using container technology toward the
reproducible computation research in general [8], although with limitation as
complete isolation is not possible without hardware virtualization.

* **Openness**

  Third, proposed approach will allow open development of HemeLB
simulation workflow. In developing the blood flow scenario, configuration for the
computation process, everything will be logged and can be scrutinized by
interested parties. Container also allow anyone to inspect the
tools used in the simulation.

* **Usability**

  Lastly, HemeWeb will allow better usability in running blood flow
simulation. Currently, to run the simulation, one have to configure and
install many dependencies which requires technical dependencies that not everyone have.
Having the workflow moved into its own web application will allow people
to focus more on the simulation parameters and results rather than
worrying about configurations of the resources.


To support the claim, the author will develop an experimental system for
HemeLB called HemeWeb which will use container technology in cloud
infrastructure to run HPC workflow. The implementation will be a proof of concept that
container based HPC workflow is viable, specifically in the context of
blood flow simulation with HemeLB, docker as the containerization technology
and AWS as the cloud provider.


## Methodology
Work in progress




## Expected Outcome/ Success Criteria
Work in progress

Working prototype that enable docker based HPC computing to be done in the cloud,
that enable the computations to be done easily (usable), shared
(replicable), and inspected (openness).

On this project, the main example of the application to be used is
HemeLB.

## References

<!--[1] Mazzeo, Marco D., and Peter V. Coveney. "HemeLB: A high performance parallel lattice-Boltzmann code for large scale fluid flow in complex geometries." Computer Physics Communications 178.12 (2008): 894-914.-->

<!--[2] Goecks et al.: Galaxy: a comprehensive approach for supporting accessible, reproducible, and transparent computational research in the life sciences. Genome Biology 2010 11:R86.-->

<!--[3] Docker - http://www.docker.com/-->


<!--[5] Cloud Computing and Grid Computing 360-Degree Compared  - I. Foster, Y. Zhao, I. Raicu and S. Lu, "Cloud Computing and Grid Computing 360-Degree Compared," Grid Computing Environments Workshop, 2008. GCE '08, Austin, TX, 2008, pp. 1-10.  doi: 10.1109/GCE.2008.4738445-->


<!--[7] Hey, Tony, and Anne E. Trefethen. "Cyberinfrastructure for e-Science." Science 308.5723 (2005): 817-821.-->

<!--[8] Larson, Stefan M., et al. "Folding@ Home and Genome@ Home: Using distributed computing to tackle previously intractable problems in computational biology." arXiv preprint arXiv:0901.0866 (2009).-->




<!--[15] Marwick, Ben. "Computational Reproducibility in Archaeological Research: Basic Principles and a Case Study of Their Implementation." Journal of Archaeological Method and Theory (2016): 1-27.-->


[1] Itani, M. A., Schiller, U. D., Schmieschek, S., Hetherington, J., Bernabeu, M. O., Chandrashekar, H., ... & Groen, D. (2015). An automated multiscale ensemble simulation approach for vascular blood flow. Journal of Computational Science, 9, 150-155.

[2] Donoho, D. L. (2010). An invitation to reproducible computational research. Biostatistics, 11(3), 385-388.

[3] Sandve, G. K., Nekrutenko, A., Taylor, J., & Hovig, E. (2013). Ten simple rules for reproducible computational research. PLoS Comput Biol, 9(10), e1003285.

[4] Peng, R. D. (2011). Reproducible research in computational science. Science (New York, Ny), 334(6060), 1226.

[5] Huerta, M., Downing, G., Haseltine, F., Seto, B., & Liu, Y. (2000). NIH working definition of bioinformatics and computational biology. US National Institute of Health.

[6] http://www.independent.co.uk/news/science/computer-simulation-could-become-integral-in-the-diagnosis-treatment-or-prevention-of-disease-by-the-9537730.html

[7] Merkel, D. (2014). Docker: lightweight linux containers for consistent development and deployment. Linux Journal, 2014(239), 2.

[8] Boettiger, C. (2015). An introduction to Docker for reproducible research. ACM SIGOPS Operating Systems Review, 49(1), 71-79.

[9] Berman, Fran, Geoffrey Fox, and Anthony JG Hey. Grid computing: making the global infrastructure a reality. Vol. 2. John Wiley and sons, 2003.

[10] http://www.archer.ac.uk/access/

[11] http://www.prace-project.eu/

[12] Foster, I., & Kesselman, C. (Eds.). (2003). The Grid 2: Blueprint for a new computing infrastructure. Elsevier.

[13] Foster, I., Zhao, Y., Raicu, I., & Lu, S. (2008, November). Cloud computing and grid computing 360-degree compared. In Grid Computing Environments Workshop, 2008. GCE'08 (pp. 1-10). Ieee.

[14] TeraGrid Archive https://www.xsede.org/tg-archives

[15] http://www.fsn.co.uk/channel_outsourcing/the_economy_is_flat_so_why_are_financials_cloud_vendors_growing_at_more_than_90_percent_per_annum#.UbmtsPlJPGA/

[16] https://aws.amazon.com/blogs/aws/aws-price-reduction-42-ec2-s3-rds-elasticache-and-elastic-mapreduce/

[17] https://azure.microsoft.com/en-us/blog/storage-price-match/

[18] http://techcrunch.com/2014/03/25/google-drops-prices-for-compute-and-app-engine-by-over-30-cloud-storage-by-68-introduces-sustained-use-discounts/

[19] Whitepaper: Intro to HPC on AWS - https://d0.awsstatic.com/whitepapers/Intro_to_HPC_on_AWS.pdf

[20] Cohen, Johanne, et al. "Nekkloud: A software environment for high-order finite element analysis on clusters and clouds." Cluster Computing (CLUSTER), 2013 IEEE International Conference on. IEEE, 2013.

[21] Mehrotra, Piyush, et al. "Performance evaluation of Amazon EC2 for NASA HPC applications." Proceedings of the 3rd workshop on Scientific Cloud Computing Date. ACM, 2012.

[22] He, Qiming, et al. "Case study for running HPC applications in public clouds." Proceedings of the 19th ACM International Symposium on High Performance Distributed Computing. ACM, 2010.
