# DeepRL4FL: Improving Fault Localization via Representation Learning

In this paper, we propose DEEPRL4FL, a deep learning fault localization (FL) approach that locates the buggy code at the statement and method levels by treating FL as an image pattern recognition problem. DEEPRL4FL does so via novel code coverage representation learning (RL) and data dependencies RL for program statements. Those two types of RL on the dynamic information in a code coverage matrix are also combined with the code representation learning on the static information of the usual suspicious source code. This combination is inspired by crime scene investigation in which investigators analyze the crime scene (failed test cases and statements) and related persons (statements with dependencies), and at the same time, examine the usual suspects who have committed a similar crime in the past (similar buggy code in the training data). For the code coverage information, DEEPRL4FL first orders the test cases and marks error-exhibiting code statements, expecting that a model can recognize patterns discriminating between faulty and non-faulty statements/methods easily. For dependencies among statements, the suspiciousness of a statement is seen taking into account the data dependencies to other statements in execution and data flows, in addition to the statement by itself. Finally, the vector representations for code coverage matrix, data dependencies among statements, and source code are combined and used as the input of a classifier built from a Convolution Neural Network to detect buggy statements/methods. Our empirical evaluation shows that DEEPRL4FL outperforms the baseline models and localizes 245 bugs from Defects4J. It improves the top-1 results of baselines from 15.0%–206.3%.

----------
# This repository is still under clearing and re-formating. 

# The Dataset we used in the paper

Defects4J: https://github.com/rjust/defects4j

ManyBugs: https://repairbenchmarks.cs.umass.edu/ 

----------

# The Code for this paper:

https://github.com/deeprl4fl2021icse/deeprl4fl-2021-icse/DeepRL4FL

