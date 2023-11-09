The goal of this project is to create a generalizable method for maximizing profit in one-dimensional Knapsack problems. 

Problem: Imagine robbing a bank, vault (later reserve) full of valuables of different volumes and weights. You're carrying a knapsack with you, with a limited volume capacity, smaller than the total volume of all the jewelry in the vault. Which items should you pick in order to maximize the profit?

Solution 1: Try all different item arrangements (i.e., permutations). This yields the best solution every time, but gets computationally very hard very fast (e.g., 30! already has more than 30 zeros...), so is suitable for small item counts.

Solution 2: Try as many arrangements as you possibly can and pick the best. This is relatively easy to implement and generally brings better results than a random pick. This is still far from perfect as, in general, the set of tested permutations are limited to an insignificantly small portion, once again, compared to the factorials of some bigger item counts.

Solution 3: Try as many arrangements as you possibly can and pick the items which in general performed well in the trials. This was more laboursome to design and implement. However, the results are increasingly promising compared to Solution 2 best picks, as dealing with greater item counts. When drawn a graph, Solution 3 tends to cross Solution 2 max scores as increasing the sample pool size. Moreover, the general trend when comparing the two methods turns out be that, with a fixed number of samples, the difference of Solution 2 and 3 optimal solution scores increases as the reserve item count grows. Please refer to the graphs for better picture.
