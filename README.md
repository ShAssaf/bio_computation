# bio_computation

## Authors: Shlomo Assaf & Tomer Bahar

This project focuses on exploring bio-computational concepts through graph theory. It includes two main exercises, each implemented as a separate function: EX1 and EX2. To provide a user-friendly experience, we have created a main function that runs both exercises.

### Usage
To run the project, simply execute the main function. It will generate and analyze a directed multigraph with a specified number of nodes.

### Exercise 1

a) This program utilizes two main methods and a function to write the motifs to a text file. Firstly, the function get_multigraph_with_connected_n_nodes generates and returns a directed multigraph with n nodes. Secondly, the function get_all_subgraphs identifies all weakly connected and non-isomorphic subgraphs. Finally, the function write_subgraphs_to_file writes the discovered motifs to a file.

b) The output can be found in the GIT repository.

c) Our program takes more than an hour to complete for values of n greater than 4. 

d) After running the code for more than 5 hours with a value of n = 5, we decided to stop the execution due to the significant increase in computation time compared to n = 4.
The is_isomorphic function utilized in the code has a worst-case time complexity of O((n+m) * n! * n^2),
where n is the number of nodes and m is the number of edges in the graphs being compared.
The exponential growth in time complexity with respect to n, particularly the factorial term n!, 
indicates that the computation time increases rapidly as the size of the graphs grows. 
This resulted in a substantial difference in execution time between n = 4 and n = 5. 
The computation for n = 5 was taking too long to complete, necessitating termination.

It's important to note that graph isomorphism is a challenging problem, 
and the computational complexity of determining isomorphism between large graphs is an active area of research. 
The specific characteristics of the graphs being compared, such as size and structure, 
greatly influence the execution time of the is_isomorphic function. Therefore, for larger values of n, 
it may not be feasible to run this code within a reasonable amount of time due to the exponential increase in computation.

### Exercise 2
Coming soon...

Please refer to the code and comments within the source files for a detailed understanding of the implementation and algorithmic approach.
