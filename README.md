# Assignments from Algorithmic Design and Development (COP4533) 2024
This course exposes the student to the topics of data structures, algorithms, algorithm design and analysis by focusing on design methods and efficiency analysis. Methods start with brute force, divide-and-conquer and then move on to more difficult ideas like dynamic programming and greedy technique. Popular puzzles are used to motivate students' interest and strengthen their skills in algorithmic problem solving. This is an advanced level programming course and it is recommended that students have completed a lower level programming language.

# Assignment 1 - Euclid GCD vs Math GCD Performance Test
### euclidgcd.py and mathgcd.py  
![gcdmath and gcdeuclid](https://github.com/user-attachments/assets/90c5efff-edc1-45a3-82a9-d7ffa0a016f5)

## mathgcdtest.py  
![gcdeuclidtest](https://github.com/user-attachments/assets/da967d54-ff12-422e-97d8-29de99bcb521)

## euclidgcdtest.py  
![gcdmathtest](https://github.com/user-attachments/assets/2a06c672-0814-4bb5-aa20-5619267e79a4)

# Assignment 2 - Time Complexities of Different Algorithms

### check_html.py  
![check_html](https://github.com/user-attachments/assets/fb1db76c-cbd1-4090-86bb-820eee7c8865)

### list_tests.py  
![list_tests](https://github.com/user-attachments/assets/f32a536c-21aa-443c-a2af-03220498e66a)

### recursion_max.py  
![recursion_max](https://github.com/user-attachments/assets/a93dcc7b-0652-4d25-94d5-a6f73d829863)

## Time Complexity Analysis:  
- Check_html.py has a time complexity of O(n)
- List_tests.py has a time complexity of O(n log n)
- Recursion_max.py has a time complexity of O(log n)

## Discussion:  
- Check_html.py has a time complexity of O(n) because there are no nested loops, just a single for loop that will iterate for the number of tags found in the file.  It also does not recursively call itself in the loop.
- List_tests.py has a time complexity of O(n log n) because it is complex containing multiple nested loops that run an uncertain number of times.  There is half of the code that creates the tests and formatting, and the other half iterates through a loop hundreds of times.
- Recursion_max.py has a time complexity of O(log n) because the number of iterations is variable and will depend on the input provided.  If the input is very large, the number of iterations will change, however, not at a constant rate.  I figure it will either be O(n log n) or O(log n) because the number of iterations will not evenly “square” the more elements are added to the array, and I know it is not O(n log n) because there is no outer loop that runs “n” times, so it must be O(log n)

# Assignment 3 - Sorting Algorithms and Analysis
## Searching Time Analysis  
After taking a quick glance at the results, sequential search is faster than binary, but this is dependent on the size of the array.  These tests only sort arrays with 20 elements in them, but when the array is much larger, binary sort is better suited.  Sequential search has a time complexity of O(n), meaning it may be more effective when the element is in the beginning of the array, however this is not efficient for large data sets.  Binary search has a time complexity of O(logn) because it splits the array in half through each iteration, making it a logarithmic algorithm.  This is much better for larger data sets compared to sequential search.  

![binary_sequential_test](https://github.com/user-attachments/assets/bda6543d-940e-4643-a034-eba2e760ae79)

## Sorting Time Analysis  
Bubble sort has a time complexity of O(n) because it will iterate once for each element.  Bubble sort is best suited for smaller arrays.  Quick sort has a time complexity of O(n*log(n)) and it best used for sorting arrays out of the three studied, as it can scale to large array sizes.  The worst-case scenario for quick sort is an array that partitions the sub arrays unevenly each time.  Lastly, merge sort has a time complexity of O(n*log n) because it depends on the size of the overarching array, and may take a long time for small arrays, but much faster for larger arrays.  

![bubble_quick_merge_test](https://github.com/user-attachments/assets/a2cbc82b-d2f9-4570-a281-7876262f7b65)

## Binary Tree Time Analysis  
Binary Tree has a time complexity of O(logn) because it will scale depending on the size of the array.  This has a different time complexity that the other three, and this search is much faster than the other three as well.  

![binarytree_test](https://github.com/user-attachments/assets/7ffab89b-5688-4800-83f0-d964b5efa0ec)

# Assignment 4 - Dijkstra's vs Bellman Ford Algorithm

## program_a.py  

![program_a](https://github.com/user-attachments/assets/8cf33398-d166-4df1-a0c0-a1fe5aef0bcb)  
This program utilizes Dijkstra’s Algorithm and locates the shortest distance between A and I.  This algorithm has a time complexity of O(ElogV) where V is the number of vertices and E is the number of edges.  It has a special time complexity, not like O(n) or O(logn) because this algorithm traverses through a bubble graph where nodes are connected to each other at varying distances.  

## program_b.py
I was unable to complete program_b.py because I was unable to implement my graph class with the Bellman Ford algorithm.  I completed the algorithm, but I didn’t fully understand the values it needed to be passed, and how I should change my graph class to match the algorithm.  Bellman Ford’s algorithm has a time complexity of O(V*E), where V and E are the same as in the previous algorithms time complexity.  This means that this algorithm is less efficient than Dijkstra’s because O(ElogV) will rapidly scale when more vertices are introduced.  However, O(V*E)’s time complexity is faster to calculate, due to the lack of a logarithm, so it will be faster at smaller scale.  

