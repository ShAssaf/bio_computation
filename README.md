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

According to the documents of nx.is_isomorphic the vf2-algorithm is implemented and even the original scientific reference is given.
The boost library states for the vf2-algorithm the following complexity:

"The spatial complexity of VF2 is of order O(V), where V is the (maximum) number of vertices of the two graphs. Time complexity is O(V^2) in the best case and O(V!·V) in the worst case."

The whole EX1 code inclouding the is_isomorphic has a worst-case time complexity of O((n+m) * n! * n^2),
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
is called from the main as we explained, its input is graph (come from a file) and the output are the motifs that can be generated from the graph
for the input :
1 2
2 3
1 4
the output is:
count=214
#0
0 1
1 0
#6
1 0
#0
0 1
0 2
1 0
1 2
2 0
2 1
#0
0 2
1 0
1 2
2 0
2 1
#0
1 0
1 2
2 0
2 1
#0
1 2
2 0
2 1
#1
2 0
2 1
#1
1 2
2 0
#0
1 0
2 0
2 1
#0
1 0
2 0
#0
0 2
1 2
2 0
2 1
#0
0 2
1 2
2 1
#0
0 2
1 0
2 0
2 1
#0
0 2
1 0
2 1
#0
0 2
1 0
1 2
2 0
#0
0 1
0 2
0 3
1 0
1 2
1 3
2 0
2 1
2 3
3 0
3 1
3 2
#0
0 2
0 3
1 0
1 2
1 3
2 0
2 1
2 3
3 0
3 1
3 2
#0
0 3
1 0
1 2
1 3
2 0
2 1
2 3
3 0
3 1
3 2
#0
1 0
1 2
1 3
2 0
2 1
2 3
3 0
3 1
3 2
#0
1 2
1 3
2 0
2 1
2 3
3 0
3 1
3 2
#0
1 3
2 0
2 1
2 3
3 0
3 1
3 2
#0
2 0
2 1
2 3
3 0
3 1
3 2
#0
2 1
2 3
3 0
3 1
3 2
#0
2 3
3 0
3 1
3 2
#0
3 0
3 1
3 2
#0
2 3
3 0
3 1
#0
2 1
3 0
3 1
3 2
#1
2 1
3 0
3 2
#0
2 1
3 0
3 1
#0
2 1
2 3
3 0
3 2
#0
2 1
2 3
3 0
3 1
#0
2 0
2 1
3 0
3 1
3 2
#0
2 0
2 1
3 0
3 1
#0
1 3
2 1
2 3
3 0
3 1
3 2
#0
1 3
2 3
3 0
3 1
3 2
#0
1 3
2 3
3 0
3 2
#0
1 3
2 3
3 0
#0
1 3
2 1
3 0
3 1
3 2
#0
1 3
2 1
3 0
3 2
#0
1 3
2 1
3 0
#0
1 3
2 1
3 0
3 1
#0
1 3
2 1
2 3
3 0
3 2
#0
1 3
2 1
2 3
3 0
#0
1 3
2 1
2 3
3 0
3 1
#0
1 3
2 0
2 3
3 0
3 1
3 2
#0
1 3
2 0
3 0
3 1
3 2
#0
1 3
2 0
3 1
3 2
#0
1 3
2 0
3 0
3 2
#0
1 3
2 0
3 0
#0
1 3
2 0
3 0
3 1
#0
1 3
2 0
2 3
3 1
3 2
#0
1 3
2 0
2 3
3 1
#0
1 3
2 0
2 3
3 0
3 2
#0
1 3
2 0
2 3
3 0
#0
1 3
2 0
2 3
3 0
3 1
#0
1 3
2 0
2 1
3 0
3 1
3 2
#0
1 3
2 0
2 1
3 1
3 2
#0
1 3
2 0
2 1
3 0
3 2
#0
1 3
2 0
2 1
3 0
#0
1 3
2 0
2 1
3 0
3 1
#0
1 3
2 0
2 1
2 3
3 1
3 2
#0
1 3
2 0
2 1
2 3
3 1
#0
1 3
2 0
2 1
2 3
3 0
3 2
#0
1 3
2 0
2 1
2 3
3 0
#0
1 3
2 0
2 1
2 3
3 0
3 1
#0
1 2
1 3
2 1
2 3
3 0
3 1
3 2
#0
1 2
1 3
2 1
2 3
3 0
3 2
#0
1 2
1 3
2 1
2 3
3 0
#0
1 2
1 3
2 0
2 3
3 0
3 1
3 2
#0
1 2
1 3
2 0
3 0
3 1
3 2
#0
1 2
1 3
2 0
3 0
3 2
#0
1 2
1 3
2 0
3 0
#0
1 2
1 3
2 0
3 0
3 1
#0
1 2
1 3
2 0
2 3
3 0
3 2
#0
1 2
1 3
2 0
2 3
3 0
3 1
#0
1 2
1 3
2 0
2 1
3 0
3 1
3 2
#0
1 2
1 3
2 0
2 1
3 0
3 1
#0
1 0
1 3
2 0
2 1
2 3
3 0
3 1
3 2
#0
1 0
2 0
2 1
2 3
3 0
3 1
3 2
#0
1 0
2 0
2 3
3 0
3 1
3 2
#0
1 0
2 0
3 0
3 1
3 2
#0
1 0
2 0
3 0
3 2
#0
1 0
2 0
3 0
#0
1 0
2 0
2 3
3 0
3 2
#0
1 0
2 0
2 3
3 0
3 1
#0
1 0
2 0
2 1
3 0
3 1
3 2
#0
1 0
2 0
2 1
3 0
3 1
#0
1 0
1 3
2 0
2 3
3 0
3 1
3 2
#0
1 0
1 3
2 0
2 3
3 0
3 2
#0
1 0
1 3
2 0
2 1
3 0
3 1
3 2
#0
1 0
1 3
2 0
2 1
3 0
3 2
#0
1 0
1 3
2 0
2 1
2 3
3 0
3 1
#0
0 3
1 2
1 3
2 0
2 1
2 3
3 0
3 1
3 2
#0
0 3
1 3
2 0
2 1
2 3
3 0
3 1
3 2
#0
0 3
1 3
2 1
2 3
3 0
3 1
3 2
#0
0 3
1 3
2 3
3 0
3 1
3 2
#0
0 3
1 3
2 3
3 1
3 2
#0
0 3
1 3
2 3
3 2
#0
0 3
1 3
2 1
3 0
3 1
3 2
#0
0 3
1 3
2 1
3 1
3 2
#0
0 3
1 3
2 1
3 2
#0
0 3
1 3
2 1
3 1
#0
0 3
1 3
2 1
3 0
3 2
#0
0 3
1 3
2 1
3 0
#0
0 3
1 3
2 1
3 0
3 1
#0
0 3
1 3
2 1
2 3
3 1
3 2
#0
0 3
1 3
2 1
2 3
3 2
#0
0 3
1 3
2 1
2 3
3 1
#0
0 3
1 3
2 1
2 3
3 0
3 2
#0
0 3
1 3
2 1
2 3
3 0
#0
0 3
1 3
2 1
2 3
3 0
3 1
#0
0 3
1 3
2 0
2 1
3 0
3 1
3 2
#0
0 3
1 3
2 0
2 1
3 1
3 2
#0
0 3
1 3
2 0
2 1
3 2
#0
0 3
1 3
2 0
2 1
3 1
#0
0 3
1 3
2 0
2 1
3 0
3 1
#0
0 3
1 3
2 0
2 1
2 3
3 1
3 2
#0
0 3
1 3
2 0
2 1
2 3
3 2
#0
0 3
1 3
2 0
2 1
2 3
3 1
#0
0 3
1 3
2 0
2 1
2 3
3 0
3 1
#0
0 3
1 2
2 0
2 1
2 3
3 0
3 1
3 2
#0
0 3
1 2
2 1
2 3
3 0
3 1
3 2
#0
0 3
1 2
2 1
3 0
3 1
3 2
#0
0 3
1 2
2 1
3 1
3 2
#0
0 3
1 2
2 1
3 0
3 2
#0
0 3
1 2
2 1
2 3
3 1
3 2
#0
0 3
1 2
2 1
2 3
3 1
#0
0 3
1 2
2 1
2 3
3 0
3 2
#0
0 3
1 2
2 1
2 3
3 0
3 1
#0
0 3
1 2
2 0
2 3
3 0
3 1
3 2
#0
0 3
1 2
2 0
3 0
3 1
3 2
#0
0 3
1 2
2 0
3 1
3 2
#0
0 3
1 2
2 0
3 1
#0
0 3
1 2
2 0
3 0
3 1
#0
0 3
1 2
2 0
2 3
3 1
3 2
#0
0 3
1 2
2 0
2 3
3 0
3 1
#0
0 3
1 2
2 0
2 1
3 0
3 1
3 2
#0
0 3
1 2
2 0
2 1
3 0
3 1
#0
0 3
1 2
1 3
2 1
2 3
3 0
3 1
3 2
#0
0 3
1 2
1 3
2 1
2 3
3 1
3 2
#0
0 3
1 2
1 3
2 1
2 3
3 2
#0
0 3
1 2
1 3
2 1
2 3
3 0
3 2
#0
0 3
1 2
1 3
2 1
2 3
3 0
#0
0 3
1 2
1 3
2 0
2 3
3 0
3 1
3 2
#0
0 3
1 2
1 3
2 0
3 0
3 1
3 2
#0
0 3
1 2
1 3
2 0
3 1
3 2
#0
0 3
1 2
1 3
2 0
3 2
#0
0 3
1 2
1 3
2 0
3 0
3 2
#0
0 3
1 2
1 3
2 0
3 0
3 1
#0
0 3
1 2
1 3
2 0
2 3
3 1
3 2
#0
0 3
1 2
1 3
2 0
2 3
3 2
#0
0 3
1 2
1 3
2 0
2 3
3 1
#0
0 3
1 2
1 3
2 0
2 3
3 0
3 2
#0
0 3
1 2
1 3
2 0
2 3
3 0
#0
0 3
1 2
1 3
2 0
2 3
3 0
3 1
#0
0 3
1 2
1 3
2 0
2 1
3 0
3 1
3 2
#0
0 3
1 2
1 3
2 0
2 1
3 1
3 2
#0
0 3
1 2
1 3
2 0
2 1
3 2
#0
0 3
1 2
1 3
2 0
2 1
3 0
3 2
#0
0 3
1 2
1 3
2 0
2 1
3 0
#0
0 3
1 2
1 3
2 0
2 1
3 0
3 1
#0
0 3
1 2
1 3
2 0
2 1
2 3
3 1
3 2
#0
0 3
1 2
1 3
2 0
2 1
2 3
3 2
#0
0 3
1 2
1 3
2 0
2 1
2 3
3 1
#0
0 3
1 2
1 3
2 0
2 1
2 3
3 0
3 2
#0
0 3
1 2
1 3
2 0
2 1
2 3
3 0
#0
0 3
1 2
1 3
2 0
2 1
2 3
3 0
3 1
#0
0 3
1 0
1 3
2 0
2 1
2 3
3 0
3 1
3 2
#0
0 3
1 0
2 0
2 1
2 3
3 0
3 1
3 2
#0
0 3
1 0
2 0
2 1
3 0
3 1
3 2
#0
0 3
1 0
2 0
2 1
3 1
3 2
#0
0 3
1 0
2 0
2 1
3 0
3 1
#0
0 3
1 0
2 0
2 1
2 3
3 1
3 2
#0
0 3
1 0
2 0
2 1
2 3
3 1
#0
0 3
1 0
2 0
2 1
2 3
3 0
3 1
#0
0 3
1 0
1 3
2 0
2 3
3 0
3 1
3 2
#0
0 3
1 0
1 3
2 0
2 3
3 1
3 2
#0
0 3
1 0
1 3
2 0
2 3
3 0
3 2
#0
0 3
1 0
1 3
2 0
2 3
3 0
#0
0 3
1 0
1 3
2 0
2 1
3 0
3 1
3 2
#0
0 3
1 0
1 3
2 0
2 1
3 1
3 2
#0
0 3
1 0
1 3
2 0
2 1
3 0
3 2
#0
0 3
1 0
1 3
2 0
2 1
3 0
3 1
#0
0 3
1 0
1 3
2 0
2 1
2 3
3 1
3 2
#0
0 3
1 0
1 3
2 0
2 1
2 3
3 0
3 2
#0
0 3
1 0
1 3
2 0
2 1
2 3
3 0
#0
0 3
1 0
1 3
2 0
2 1
2 3
3 0
3 1
#0
0 3
1 0
1 2
2 0
2 1
2 3
3 0
3 1
3 2
#0
0 3
1 0
1 2
2 0
2 1
3 0
3 1
3 2
#0
0 3
1 0
1 2
2 0
2 1
3 1
3 2
#0
0 3
1 0
1 2
2 0
2 1
3 0
3 2
#0
0 3
1 0
1 2
2 0
2 1
2 3
3 1
3 2
#0
0 3
1 0
1 2
2 0
2 1
2 3
3 0
3 2
#0
0 3
1 0
1 2
2 0
2 1
2 3
3 0
3 1
#0
0 3
1 0
1 2
1 3
2 0
2 1
2 3
3 1
3 2
#0
0 3
1 0
1 2
1 3
2 0
2 1
2 3
3 0
3 2
#0
0 3
1 0
1 2
1 3
2 0
2 1
2 3
3 0
#0
0 2
0 3
1 2
1 3
2 0
2 1
2 3
3 0
3 1
3 2
#0
0 2
0 3
1 2
1 3
2 1
2 3
3 0
3 1
3 2
#0
0 2
0 3
1 2
1 3
2 1
2 3
3 1
3 2
#0
0 2
0 3
1 2
1 3
2 1
2 3
3 0
3 2
#0
0 2
0 3
1 2
1 3
2 1
2 3
3 0
3 1
#0
0 2
0 3
1 2
1 3
2 0
2 1
3 0
3 1
3 2
#0
0 2
0 3
1 2
1 3
2 0
2 1
3 0
3 1
#0
0 2
0 3
1 0
1 3
2 0
2 1
2 3
3 0
3 1
3 2
#0
0 2
0 3
1 0
1 3
2 1
2 3
3 0
3 1
3 2
#0
0 2
0 3
1 0
1 3
2 1
2 3
3 1
3 2
#0
0 2
0 3
1 0
1 3
2 0
2 1
3 0
3 1
3 2
#0
0 2
0 3
1 0
1 3
2 0
2 1
3 1
3 2
#0
0 2
0 3
1 0
1 3
2 0
2 1
2 3
3 0
3 2
#0
0 2
0 3
1 0
1 3
2 0
2 1
2 3
3 0
3 1
#0
0 2
0 3
1 0
1 2
1 3
2 0
2 3
3 0
3 1
3 2
#0
0 2
0 3
1 0
1 2
1 3
2 0
2 3
3 0
3 2
#0
0 2
0 3
1 0
1 2
1 3
2 0
2 1
3 0
3 1
3 2

Please refer to the code and comments within the source files for a detailed understanding of the implementation and algorithmic approach.