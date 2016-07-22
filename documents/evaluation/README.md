![University of Edinburgh logo](../resources/images/edinburgh-logo.png "University of Edinburgh logo")

## Introduction

Hi there,

I, Steven, am writing dissertation for my MSc of Computer Science titled "HemeWeb: Blood flow simulation on the cloud". Today, I will be conducting an evaluation on my project to measure the usability of the project compared with the original approach to run blood flow simulations using HemeLB.

In this evaluation, I will need your help to run two different approach to run same blood flow simulation, followed by a short interview to measure your experience. These sessions will be recorded for evaluation purpose. It is to be noted that there are no right or wrong in running this simulation, so you do not have to worry. If in any of the process, you become uncomfortable, we will stop the session and you are free to leave.

Once again, thank you for helping me with my work.


Steven


## About the blood flow simulation

In this evaluation, you will run a blood flow simulation using
tools named HemeLB. The software will take sets of input and run
simulation to produce specific outputs from it.


We will compare the usability aspect of the simulation process using two
different approach, using command line and using web interface. You will
be given instruction on how to do both approach.



## Demographic questions

1. Age
  * [ ] 11 - 15
  * [ ] 16 - 20
  * [ ] 21 - 25
  * [ ] 26 - 30
  * [ ] 31 - 35
  * [ ] over 36
  * [ ] Prefer not to say

2. Gender
  * [ ] Male
  * [ ] Female
  * [ ] Prefer not to say

3. Familiar with operating command line interface ?
  * [ ] Yes
  * [ ] No

4. Familiar with blood flow simulation tools ?
  * [ ] Yes
  * [ ] No

5. Familiar with operating web browser (Chrome / Safari / IE / Opera)?
  * [ ] Yes
  * [ ] No

6. Profession?
  * [ ] Student
  * [ ] Biologist
  * [ ] Doctor
  * [ ] Lecturer
  * [ ] Other ..................


## Simulation A

1. Open web browser, go to http://53.12.13.14

2. Click on add new job

3. Use the provided input files on the desktop for "New job config" form

4. Configure the simulation with these parameters

   ```
      HemeLB config: No change
      Container Image: SeiryuZ/hemelb-core:0.0.2
      Image type: 8 core
      Instance count: 2
   ```

5. Go to the overview tab and review the parameters one final time

6. Click on run simulation


## Simulation B

1. Open terminal (cmd shift t)

2. Run HemeLB simulation using this command

   ```bash
     openmpi.mpirun --mca btl_tcp_if_include eth0 -np 4 hemelb -in $HEMELB_INPUT -out $HEMELB_OUTPUT 1> $LOG_FILE 2>&1
   ```


## Evaluation

1. Which one do you prefer to use ?
  * [ ] Command line interface
  * [ ] Web browser

2. If you choose command line, why do you prefer it?
  * [ ] It is faster
  * [ ] It is more flexible
  * [ ] Others .....

3. If you choose web browser, why do you prefer it ?
  * [ ] It is faster
  * [ ] It is easier
  * [ ] Others .......

