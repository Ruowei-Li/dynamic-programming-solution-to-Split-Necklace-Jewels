# Dynamic Programming solution to Split Necklace Jewels


We have a Queen with several Necklaces that she wants to split-up and divide the jewel stones to his two daughters as fairly as possible. Each jewel on an necklace has a fixed value and she has decided to let one daughter pick a subset of the jewels then the other daughter take the remaining. The “fairness idea’ that the Queen decides to use is to restrict the first daughter to pick only a subset of jewels that are not adjacent to any others in that set. The jewels are in a circular pattern in index positions 0, 1, 2, . . . , n − 1. Where if the first daughter selects jewel at position i then she can not take jewel at position i − 1 or i + 1 (modulo n). The maximum number of jewels per necklace is one million.

An input is a sequence of necklaces, one per line. Each necklaces is a sequence of positive integers separated by white spaces denoting the values of each jewel.

The printed output of the program, one line per each scenario, is the maximum value daughter one can obtain and the remaining value the other daughter receives for each necklace.

## Sample Input:
```
4 10 8
10 4 8 5
3 2 10 2 3 7 
1 1 1 1 1
```

## Sample Output:
```
10 12
18 9
17 10
2 3
```
