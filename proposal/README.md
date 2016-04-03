# HemeWeb: Container based high performance computing scenario for HemeLB


## Purpose


<!-- HemeLB simulation is hard to use, especially to doctors and
scientists  -->
HemeLB [1], a fluid dynamic simulation software that is used for the study of
blood flow, have complex workflow that makes it challenging for doctors
and scientists to use. To run a simulation, one has to configure a range of
tools that are needed for each steps of the workflow with the correct
parameters and inputs. Moreover, each steps require highly varying computing
resources, from personal PC to supercomputer that is non-trivial to
acquire access to. These facts, coupled with
doctors and scientists who might not have the technological expertise to
begin with, render HemeLB only accessible to few people.


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

<!-- To embrace open science, HemeLB needs to improve its auditability  -->
In addition to being usable, HemeLB simulation, which is described as an integral part of
clinical decision in the future [6], also needs to be trustworthy by
being auditable and easily reproducible. Auditable as in the software
can be peer-reviewed and audited to make sure it produce the correct
result, while easily reproducible mean that the software can be easily
re-run to make sure it produce consistent result in different
infrastructure. These aspects are
important for the users, especially when HemeLB will be used to
determine health and well-being of patients. Currently, HemeLB project have taken steps to be open
and auditable by being developed openly in the public, and making
manually recorded resources for simulation available upon request.
However, with recent pushes of open science and more specifically,
reproducible computing research [2][3][4], there are extra
steps that HemeLB project can take in order to further improve its
trustworthiness, especially on automatic record of resources needed for simulation
leading to easier reproduction of simulation.


<!--this is the case. All simulations configurations, input files, and-->
<!--results are manually recorded for the purpose of reproduction. However,-->
<!--with recent pushes for reproducible computing research [2][3][4], HemeLB-->
<!--needs to improve its reproducible aspect to make sure it adhere to the-->
<!--open science standard of being open and auditable. This is even more-->
<!--important when this research area is described in media as an integral-->
<!--part of clinical decision in the future[6]-->


<!--With pushes for reproducible computing research in general [2][3][4], HemeLB-->
<!--needs to improve its reproducible computing aspect for the benefit of-->
<!--the simulations that run with it. HemeLB Simulations should  adhere to a higher-->
<!--standard of validation from the community, making it more transparent-->
<!--and trustworthy. This trustworthiness is especially more important-->
<!--when this research area is described in media as an "integral" part in-->
<!--clinicial decision in the future [6].-->

<!-- Above reasons is the impetus for my proposal -->
For reasons above, I propose to create an extension to HemeLB called
HemeWeb. HemeWeb will be a web application for HemeLB simulation
workflow that hide the configuration complexity from the users. Doctors
and Scientists, will deal with an easier to use web interface and have to
worry about the simulation input and result  instead of worrying about
configuration of the tools. Moreover, with the help
of containerization technology, all tools that are used in the
simulations are going to be packaged in such a way that makes reusing
computing resources easy. Configured cluster can be reused by simply
swapping the container image of the tools, instead of reconfiguring the
whole cluster from the start. Furthermore, containerization tool will
also help with the project being open and auditable since it will require the
development of the tools to be publicly shared on its registry for
others to inspect and audit. Ultimately, The proposed extension will aim to make HemeLB
more trustworthy.


<!--In adhering to the reproducible aspect,-->
<!--the author propose on creating an "extension" to HemeLB called HemeWeb.-->
<!--HemeWeb will be a web application for HemeLB simulation workflow that-->
<!--allows interested party to configure and run blood flow simulation on-->
<!--the cloud, or even, their own computing resources. This extension will-->
<!--utilize container technology, specifically Docker [7], that allows tools-->
<!--involved with the workflow to be isolated, inspected, and shared easily-->
<!--with the publicly available registry. Moreover, docker has been reviewed-->
<!--to be an appropriate tool for distributing reproducible research, albeit-->
<!--with few limitations [8]. Thus in this project, the author will create-->
<!--an experimental web application for HemeLB to address the reproducible-->
<!--computing aspect of the research using docker.-->



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


In order to develop HemeWeb, few key technologies and concepts have to
be made clear. These key technologies consists of HemeLB as an HPC
application, Cloud Computing, and Containerization technology. In this
section, I will provide a short overview of these technologies and
concepts before continuing with the proposed system.


**HemeLB Workflow**




![alt text](../resources/images/HemeLB-workflow.png "HemeLB current workflow")

Above image illustrate the workflow of HemeLB simulation that require
multiple steps before results can be produced. First, a 2D image of a blood
vessel is needed to be piped into a geometrical model
reconstruction script to construct a 3D model of the blood vessel. This
3D model will then need more information like blood viscocity, and inlet
outlet placement to be used as the simulation parameter. These information are
going to be added by the user in domain definition step. Next, the 3D
model and the information about the simulation need to be converted into
a file format that HemeLB can understand. After conversion, simulation
can be finally run that eventually will output a simulation result that
will need further pre-processing script to convert the output into a
file format that can be viewed easily.

<!--Currently HemeLB workflow is complex-->
Not only understanding the workflow of the process, domain experts also
need to configure tools required on each steps, making it really complex
to use the software, especially if they don't have the expertise.
This is not an ideal situation for the project where users are required
to understand their non-domain expertise to use the software. A better
condition will be where domain-experts only need to deal with their
respective domain concern of the project. All other concern which are
not related to their domain, in this case configuration of the tools
needed, should be hidden from them.


Hiding this complexity from the users is the reason why I think web
application is the correct approach. Web application requires the user
to interface with them using the web browser, which is currently a
standard tools in everyday's life. Doctors and biologists could easily
treat the simulation tools as a black box, not having to worry about
configurations, environment, and the infrastructure the software lives
on. The only things that they have to worry is the input file, their
knowledge of the domain, and the simulation result.

However, I have to underscore that this project scope will be limited
due to the available time. Originally, only the simulation part of the
workflow will be included in the web application and this is the first
step to improve the usability of the project by hiding the complexity
on that particular steps. With more integrations, more complexity will
be hidden in the process, paving way for an ideal condition where
domain-experts can do all part of the workflow from the browser.


![alt text](../resources/images/HemeLB-scope-1.png "HemeWeb scope 1st Phase")


On top of having a web application to hide technical complexity from the
domain-experts, I also propose the usage of containerization technology
to hide the complexity of reproducing simulation results. As HemeLB is
actively developed, simulation results might be affected by the changes
in the components. This is why simulation needs to be tied down to a
specific version of the tools used for the simulation. Currently, it is
done manually and available upon requests, but with the usage of
containerization technology, this could be improved. All associated
tools will be documented on the container image and each version of the
tools will have its own image. Tying down the simulation execution on
the web application to these image is trivial and allow users to
reproduce it easily.

On top of making it easy to reproduce, containerization technology also
allows the re-use of the resource from the infrastructure. Currently, if
one wants to rerun simulations with different version of the tools, said
tools need to be reconfigured to the exact version. This is not
practical for domain-experts because now we have another concern of
making sure the right tools are used. Container image could help in this
aspect because all the tools are containerized already, and what the web
application will need to do is to swap the image and we have the correct
tools on our disposal.


<!--HemeLB workflow currently involve a number of steps that requires-->
<!--some expertise in configuring software that doctors and biologists might-->
<!--not have. These steps are a necessary part of the current workflow to-->
<!--prepare the input files into an intermediary representation that each-->
<!--steps of the workflow needed.-->

<!--Non-expert users are overwhelmed with the range of tasks needed to use it-->


<!--Ideally users only need to deal with the task that is related to their job-->



<!--This is why web application make sense for this particular use case-->


<!--and Containerization technology can help this as well-->



**HemeLB and HPC**


<!--Introduction to HemeLB-->
<!--HemeLB is a vascular blood flow simulation that is used for the study of-->
<!--blood flow simulation [1]. It is currently being developed in the open-->
<!--on github repository where the public can easily observe the development-->
<!--and audit it. To use HemeLB however requires technical expertise that-->
<!--not everyone might have. One should acquire access to -->



<!--Introduction to computational biology and HemeLB-->
Computational biology and bioinformatics are research area that use
mathematical and often highly-parallel computational approaches in answering questions and
experiments in biology [5]. In order for these computational approaches
to run efficiently, a highly parallel computating resources like
a computer cluster or even a super computer are needed. These resources
are needed because the consumer-grade one are not yet capable to do huge
amount of computation that are needed for this kind of work. HemeLB [1],
a vascular blood flow simulation software, require these highly parallel
computing capability in order to run efficiently. Currently it ran the
simulation on ARCHER supercomputer, while some part of the workflow like
the configuration process can be done on consumer-grade personal
computer.


<!--These approaches typically involves a-->
<!--computational workflow which, depending on the type of work,-->
<!--could varies widely in performance requirement, from normal computational process-->
<!--that could be done in normal consumer desktop processor to-->
<!--high-performance scneario that needs to be run on a cluster of computers-->
<!--or even supercomputer. One example of this type of project is HemeLB, a-->
<!--vascular blood flow simulation that is used for the study of blood flow [1].-->
<!--HemeLB have different processes in the workflow that requires different computing power,-->
<!--from the setup process which can be run on consumer-level computer, to the simulation process-->
<!--that run on ARCHER supercomputer due to its processing power requirement [1].-->

<!-- HPC vs HTC !! CITATION NEEDS TO BE FIXED -->
The HemeLB simulation part require a highly paralel capabilities of the computing
resources that falls under the category of High Performance Computing.
Traditionally, large computing process could be handled by two separate
computing paradigm depending on the type of work it needs to do. These
are High Performance Computing and High Throughput Computing. High
performance computing typically involves multiple computing nodes
connected with a high bandwidth network, performing a well-defined
computations that use message passing interface to communicate between
nodes. HPC are typically performed using computer clusters, GPUs, or
even supercomputer. High troughput computing, on the other hand, is a different
paradigm. It allows highly heteregenous computing resources,
often geographically distributed, to cooperate for common goals which
involves different independent computation that can be scheduled independently
and later aggregated on one of the nodes. Based on these distinction,
HemeLB simulations can be categorized as a HPC application because it performs
a well-defined computations that are spread over multiple computing nodes with MPI.


<!-- Acquriing access to HPC infrastructure is possible but non-trivial, and maybe not a top priority for these institutes  -->
However, running these simulations require access to HPC infrastructures that
might not have reproducibility of a research as a priority. Facilities
that administer these infrastructure often give out computing hour usage
to projects based on the merit of their peer-reviewed proposal, for
example how PRACE [11], the Partnership for Advanced Computing in
Europe, and how EPSRC [10] give access to their infrastructure to
researcher. This means that reproducing computing research, if anyone
are interested, have to compete with other projects for the limited
computing hour that is given out by these institutions. Most likely, it
will not be the top priority, hence creating barrier for reproducing
computational research, in our case HemeLB simulation.


Not being prioritized in these facilities create a barrier for HemeLB to
become more trustworthy because reproduction of simulation is non-trivial.
As iterated on the previous section, HemeLB project have taken the steps
to address reproducibility of the simulation by manually recording all
the configurationns, tools version, input files, parameters and result of the
simulation. Anyone theoritically could request these documentation and
reproduce the result with the appropriate computing resource.
However, research facility that will prioritize more important research
inherently will limit people that want to reproduce the computation
result significantly.

<!-- This is why cloud computing is a perfect match  -->

<!-- Cloud computing is originaly envisioned as computing resource  -->


<!--Running HPC application like HemeLB require  access to HPC-->
<!--infrastructure, which are non-trivial to acquire.-->


<!--Both of these computing paradigm typically requires huge-->
<!--computing resources available to perform its task effectively. HPC task-->
<!--like HemeLB especially, are often run on supercomputers, for example ARCHER-->
<!--supercomputer. This supercomputers requires you to be academics /-->
<!--researchers with clear proposal, for example how epcc give access to-->
<!--ARCHER [10]. Another example is PRACE [11], the Partnership for Advanced Computing in Europe,-->
<!--that allows researcher to access supercomputers accross europe after a-->
<!--vetting process. This theoritically allow people with the credentials-->
<!--to gain access to these resources with the correct motives. However,-->
<!--reproducing research computation that already been run might not be the-->
<!--top priority of these facilities when there are many other research-->
<!--projects that depend on access to these limited resources.-->

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


<!--**Containerization technology**-->

<!--Container technology originated from the virtualization technology back-->
<!--in 1960. Back then IBM PC shipped with virtualization software that-->
<!--allow multiple operating systems to be installed into one hardware.-->
<!--Linux Kernel Container is then born to handle this virtualization but on-->
<!--the kernel level, where we could have container that run its own kernel-->
<!--separated from the host. Docker is the technology that pushes the-->
<!--adoption of this technology to the roof. Docker encapsulate tools and-->
<!--commands that allow administartion of this container much easier than-->
<!--before. Making it easy for people to use container in their workflow.-->
<!--More importantly, docker has a public registry where people could-->
<!--publish their dockerfile, and share it with the public. Interested-->
<!--people could just get the file and create their own docker image based-->
<!--on the published file. This is a huge boon in helping docker become-->
<!--popular currently.-->


<!--In reproducing computing researchm docker is deeemed fit to the task,-->
<!--since it allows computing workflow to be documented, published, and-->
<!--re-run easily because everyone has the ability to scrutinize it. This-->
<!--process however, involve an overhead that the author needs to write a-->
<!--dockerfile instead of doing whatever they are doing currently. However,-->
<!--this is a small price to pay in order to make compting reproducible-->
<!--easily. On our case, using docker is a necessary tools. Because with-->
<!--docker, people could scrutinize the tools and commands used to reproduce-->
<!--the research done with HemeLB. More importantly, the tools also will-->
<!--allow us to expand not only handling HemeLB, but also to a more general-->
<!--case of any other HPC applications to be run on the cloud indepenedent-->
<!--of what the infrastructure might be.-->




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

This project will demonstrate that by using container based approach in
cloud infrastructure, HPC application like HemeLB will be better in
usability, auditability, and reproducibility. In this section, I will
formally defined what I mean by these terms.


* **Usability**

  Usability, in this project, will be formally defined as a binary
choice of preference to use the software. Since this is the first
initial implementation of the web application for HemeLB, it is more
important to consider the improvement as people wanting to use the
software instead of the degree of comfort in using it. Therefore, this
project will demonstrate that more people will consider to use the
software than before.

  <!--Lastly, HemeWeb will allow better usability in running blood flow-->
<!--simulation. Currently, to run the simulation, one have to configure and-->
<!--install many dependencies which requires technical dependencies that not everyone have.-->
<!--Having the workflow moved into its own web application will allow people-->
<!--to focus more on the simulation parameters and results rather than-->
<!--worrying about configurations of the resources.-->

<!--the current HemeLB workflow can be improved-->
<!--by using a container based HPC in cloud infrastructure approach. This-->
<!--approach will be better for HemeLB project because it is better in-->
<!--reproducibility, isolation, openness, and usability.-->

* **Reproducibility**

  Reproducibility, will be defined as the ease of reproducing of simulation
result. In order for HemeLB to become more trustworthy, one should be
able to consistently reproduce the correct simulation results everytime,
this include the capability of even reproducing the results and the
easiness of running wanted simulation. Since HemeLB have taken steps to
make sure reproducing results are possible, HemeWeb will improve it even
further by using cloud computing infrastructure and automatically record
every simulation configurations for easy re-run.

  This project will also demonstrate that the work done here, with
modificaltion, can be applied in any infrastructures, not specific to
the implementation of the infrastructure I choose. This is important,
because reproducibility will improve the trust over the simulation
result to provide the consistent and predictable result that allow
people to trust it.


<!--The proposed approach will be better for reproducibility, allowing a-->
<!--computing process and scenario to be duplicated more easily than status quo.-->
<!--Currently, to reproduce the computational process, one must get their-->
<!--hands on the simulation configuration and run the simulation on a similar computing-->
<!--resources like ARCHER supercomputer which is not easy to replicate nor-->
<!--cheap. The proposed approach, on the other hand, will store every simulation scenario and-->
<!--configurations that are run via the web application. These scenarios can be shared-->
<!--and re-run easily, offering reproducibility to HemeLB computation. In a-->
<!--more general situation, using container technology also allows reproducibility in-->
<!--the tools used by any computational workflow. This allow computation-->
<!--workflow to be reproduced in any computing resources, not only tied into-->
<!--the implementation this paper will create.-->


* **Auditability**

  Audibility means that the tools that are used for simulations are
developed in the open and are available for audit. By having the tools
available for audit, these tools can be peer-revied or even fixed by the
public, creating more trusts with the correctness of the software used
in the simulation. Currently, HemeLB have been developed in the open,
but the use of containerization technology will further improve this
auditability. This improvement come from the automatic association of
the simulation with the version of the tools that are packaged in the
container image. These images are also going to be published publicly in
the public registry, making it not only the software involved that can
be audited, but the execution of the simulation to be auditable as well.

  This auditability is even more important when considering that the
simulation result will be used as a basis of medical decision or medical
development. Simulation result needs to be auditable so that the usage
of HemeLB can be trusted by the user and general public.


<!--Third, proposed approach will allow open development of HemeLB-->
<!--simulation workflow. In developing the blood flow scenario, configuration for the-->
<!--computation process, everything will be logged and can be scrutinized by-->
<!--interested parties. Container also allow anyone to inspect the-->
<!--tools used in the simulation.-->

<!--* **Isolation** [Need further discussion]-->

<!--Second, proposed approach will be better for isolation issue in HemeLB-->
<!--computation. Container approach will allow better isolation between-->
<!--simulation and isolation with the computing environment. This also-->
<!--demonstrate benefits of using container technology toward the-->
<!--reproducible computation research in general [8], although with limitation as-->
<!--complete isolation is not possible without hardware virtualization.-->




To support these claim, I will develop an experimental web application for
HemeLB called HemeWeb which will use container technology in cloud
infrastructure to run blood flow simulation. The implementation will be
a proof of concept that HemeLB simulation can be done in cloud
infrastructure, paving way for other infrastructures that might be used
in the future where it is used in the hospital. Not only that, it will
also improve the usability of the simulation.



## Methods
Work in progress


## Evaluation

This project will be evaluated on how it can improve the usability and
trustworthiness of the project. To accomplish this, the usability aspect will be
measured by how many scientists or doctors prefer to run simulation
using the current approach or the proposed approach. This binary
measurement is needed because as it stands currently, HemeLB project are
concerned about whether user will run simulation, not how efficient it
could be for user to run simulation.

Secondly, trustworthiness should be measured by whether user can
reproduce simulation result at all using the proposed approach. As
currently there are no alternatives for reproducing the simulation, we
should also binarily measure this capability.


Lastly, auditable is another aspect of trustworthiness that should be
measured. Since HemeLB currently has taken steps to make sure that all
simulation are documented manually. I will claim that by the existence
of the project that can automatically document the simulation, the
auditable aspect are improved inherently because it take shorter time to
look up for this documentation.


## Output

This project will create a working prototype that enable HemeLB
simulation to be run on the cloud infrastructure. This web application
will be used by the HemeLB project to introduce HemeLB workflow to their
peers, scientists and doctors. In addition, if time permit, this web
application will be extended to handle more use case from the workflow,
starting from the domain definition step to post-processing step. This
prototype development will be used as the basis of future improvement on
HemeLB workflow for eventual medical use.



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
