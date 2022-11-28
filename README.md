# Graph_Colouring_python_code_using_greedy_algorithm_and_welsh_powell_algorithm
Graph colouring problem is a problem of assigning colours to nodes (subjects) in the graph (network) such that no two adjacent vertices have same colour.\
Graph colouring problem can be solved using :
1) **Greedy Algorithm** : Start assigning a colour to some random vertex and then check which vertices are not adjacent to that vertex , colour those with the same colour. And then colour the next uncoloured vertex chosen with different colour. Continue the process till all the nodes are coloured.\
2) **Welsh-Powell Algorithm** : Calculate the degrees of all vertices and sort the vertices in descending order of degrees. Colour the first vertex with some colour. Move down the list and colour all the vertices not connected to the coloured vertex, with the same color. Repeat the process for the next uncoloured vertex in the list with diffrent colour.
\
**Graph_colouring.py** contains python implementation of above algorithms defined in different functions  :\
**greedy(g,n)** : takes graph adjacency matrix and number of nodes in the graph as inputs\
**welsh_powell(g,n)** : same goes with this, takes graph adjacency matrix and number of nodes in the graph as inputs\
Two modules are imported :\
**numpy** for generating random square matrix of size 27 to 30 representing the graph. This is used for comparison purpose.\
**time** for comparison purpose.\
There are also two examples of matrices(graph) of small size (5 and 8) which are commented. Can be run for understanding the code.
 
### Comparison between both algorithms : 

Two metrics/criterion taken into account for comparison :\
**Chromatic number :** The minimum number of colours used in order to colour the vertices.\
**Time :** Time taken for execution.
 
**Conclusion after comparison :** \
**Output_Screenshots.pdf** contains ss of execution on different graphs for better understanding.\
Greedy Approach is fast, takes less time compared to Welsh Powell\
since welsh powell must calculate degree of all vertices\
and sort in descending order.

There are Two example cases where, in first example containing 5 vertices,\
both algoithms give same chromatic number and distribution of colours,\
Whereas in second example containing 8 vertices, greedy algo gave Chromatic\
number as 3 while welsh powell gave chromatic number as 4.

Greedy approach depends on ordering of vertices, so if instead the order in \
2nd example was 0,6,2,3,1,5,4,7 then chromatic number would be 4.

Both approaches does'nt give the optimal solution **always** and can depend on other factors like the 'order' in case of greedy algorithm.
 
 
 
 
 
 
