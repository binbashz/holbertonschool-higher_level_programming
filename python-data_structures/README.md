[**Lists:**](https://www.geeksforgeeks.org/python-list/) are just like [dynamic sized arrays](https://www.geeksforgeeks.org/how-do-dynamic-arrays-work/), declared in other languages ([vector in C++](https://www.geeksforgeeks.org/vector-in-cpp-stl/) and [ArrayList in Java](https://www.geeksforgeeks.org/arraylist-in-java/)). Lists need not be homogeneous always which makes it the most powerful tool in [Python](https://www.geeksforgeeks.org/python-programming-language/).

[**Tuple:**](https://www.geeksforgeeks.org/tuples-in-python/) A Tuple is a collection of Python objects separated by commas. In some ways, a tuple is similar to a list in terms of indexing, nested objects, and repetition but a tuple is immutable, unlike lists that are mutable.

[**Set:**](https://www.geeksforgeeks.org/sets-in-python/) A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements. Python’s set class represents the mathematical notion of a set.

[**Dictionary:**](https://www.geeksforgeeks.org/python-dictionary/) in Python is an ordered (since Py 3.7) \[unordered (Py 3.6 & prior)\] collection of data values, used to store data values like a map, which, unlike other Data Types that hold only a single value as an element, Dictionary holds **key:value** pair. Key-value is provided in the dictionary to make it more optimized.



List, Tuple, Set, and Dictionary are the data structures in python that are used to store and organize the data in an efficient manner.

<table><tbody><tr><td><strong>List</strong></td><td><strong>Tuple</strong></td><td><strong>Set</strong></td><td><strong>Dictionary</strong></td></tr><tr><td>List is a non-homogeneous data structure that stores the elements in single row and multiple rows and columns</td><td>Tuple is also a non-homogeneous data structure that stores single row and multiple rows and columns</td><td>Set data structure is also non-homogeneous data structure but stores in single row</td><td>Dictionary is also a non-homogeneous data structure which stores key value pairs</td></tr><tr><td>List can be represented by [ ]</td><td><p>Tuple can be represented by &nbsp;</p><p>( )</p></td><td>Set can be represented by { }</td><td>Dictionary &nbsp;can be represented by { }</td></tr><tr><td>List allows duplicate elements</td><td>Tuple allows duplicate elements</td><td>Set will not allow duplicate elements</td><td>Dictionary doesn’t allow duplicate keys.</td></tr><tr><td>List can use nested among all</td><td>Tuple can use nested among all</td><td>Set can use nested among all</td><td>Dictionary can use nested among all</td></tr><tr><td>Example: [1, 2, 3, 4, 5]</td><td>Example: (1, 2, 3, 4, 5)</td><td>Example: {1, 2, 3, 4, 5}</td><td>Example: {1: “a”, 2: “b”, 3: “c”, 4: “d”, 5: “e”}</td></tr><tr><td>List can be created using <strong>list() </strong>function</td><td>Tuple can be created using <strong>tuple()</strong> function.</td><td>Set can be created using <strong>set()</strong> function</td><td>Dictionary can be created using <strong>dict() </strong>function.</td></tr><tr><td>List is mutable i.e we can make any changes in list.</td><td>Tuple &nbsp;is immutable i.e we can not make any changes in tuple</td><td>Set is mutable i.e we can make any changes in set. But elements are not duplicated.</td><td>Dictionary is mutable. But Keys are not duplicated.</td></tr><tr><td>List is ordered</td><td>Tuple is ordered</td><td>Set is unordered</td><td>Dictionary is ordered (Python 3.7 and above)</td></tr><tr><td><p>Creating an empty list</p><p>l=[]</p></td><td><p>Creating an empty Tuple</p><p>t=()</p></td><td><p>Creating a set</p><p>a=set()</p><div id="GFG_AD_gfg_outstream_incontent"></div><p>b=set(a)</p></td><td><p>Creating an empty dictionary</p><p>d={}</p></td></tr></tbody></table>

Below is the program for implementation of List, tuple, set, and dictionary:

-   Python3

## Python3

  

  
  

<table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="comments"># Python3 program for explaining</code></div><div class="line number2 index1 alt1"><code class="comments"># use of list, tuple, set and</code></div><div class="line number3 index2 alt2"><code class="comments"># dictionary</code></div><div class="line number4 index3 alt1">&nbsp;</div><div class="line number5 index4 alt2"><code class="comments"># Lists</code></div><div class="line number6 index5 alt1"><code class="plain">l </code><code class="keyword">=</code> <code class="plain">[]</code></div><div class="line number7 index6 alt2">&nbsp;</div><div class="line number8 index7 alt1"><code class="comments"># Adding Element into list</code></div><div class="line number9 index8 alt2"><code class="plain">l.append(</code><code class="value">5</code><code class="plain">)</code></div><div class="line number10 index9 alt1"><code class="plain">l.append(</code><code class="value">10</code><code class="plain">)</code></div><div class="line number11 index10 alt2"><code class="keyword">print</code><code class="plain">(</code><code class="string">"Adding 5 and 10 in list"</code><code class="plain">, l)</code></div><div class="line number12 index11 alt1">&nbsp;</div><div class="line number13 index12 alt2"><code class="comments"># Popping Elements from list</code></div><div class="line number14 index13 alt1"><code class="plain">l.pop()</code></div><div class="line number15 index14 alt2"><code class="functions">print</code><code class="plain">(</code><code class="string">"Popped one element from list"</code><code class="plain">, l)</code></div><div class="line number16 index15 alt1"><code class="keyword">print</code><code class="plain">()</code></div><div class="line number17 index16 alt2">&nbsp;</div><div class="line number18 index17 alt1"><code class="comments"># Set</code></div><div class="line number19 index18 alt2"><code class="plain">s </code><code class="keyword">=</code> <code class="functions">set</code><code class="plain">()</code></div><div class="line number20 index19 alt1">&nbsp;</div><div class="line number21 index20 alt2"><code class="comments"># Adding element into set</code></div><div class="line number22 index21 alt1"><code class="plain">s.add(</code><code class="value">5</code><code class="plain">)</code></div><div class="line number23 index22 alt2"><code class="plain">s.add(</code><code class="value">10</code><code class="plain">)</code></div><div class="line number24 index23 alt1"><code class="keyword">print</code><code class="plain">(</code><code class="string">"Adding 5 and 10 in set"</code><code class="plain">, s)</code></div><div class="line number25 index24 alt2">&nbsp;</div><div class="line number26 index25 alt1"><code class="comments"># Removing element from set</code></div><div class="line number27 index26 alt2"><code class="plain">s.remove(</code><code class="value">5</code><code class="plain">)</code></div><div class="line number28 index27 alt1"><code class="keyword">print</code><code class="plain">(</code><code class="string">"Removing 5 from set"</code><code class="plain">, s)</code></div><div class="line number29 index28 alt2"><code class="functions">print</code><code class="plain">()</code></div><div class="line number30 index29 alt1">&nbsp;</div><div class="line number31 index30 alt2"><code class="comments"># Tuple</code></div><div class="line number32 index31 alt1"><code class="plain">t </code><code class="keyword">=</code> <code class="functions">tuple</code><code class="plain">(l)</code></div><div class="line number33 index32 alt2">&nbsp;</div><div class="line number34 index33 alt1"><code class="comments"># Tuples are immutable</code></div><div class="line number35 index34 alt2"><code class="keyword">print</code><code class="plain">(</code><code class="string">"Tuple"</code><code class="plain">, t)</code></div><div class="line number36 index35 alt1"><code class="functions">print</code><code class="plain">()</code></div><div class="line number37 index36 alt2">&nbsp;</div><div class="line number38 index37 alt1"><code class="comments"># Dictionary</code></div><div class="line number39 index38 alt2"><code class="plain">d </code><code class="keyword">=</code> <code class="plain">{}</code></div><div class="line number40 index39 alt1">&nbsp;</div><div class="line number41 index40 alt2"><code class="comments"># Adding the key value pair</code></div><div class="line number42 index41 alt1"><code class="plain">d[</code><code class="value">5</code><code class="plain">] </code><code class="keyword">=</code> <code class="string">"Five"</code></div><div class="line number43 index42 alt2"><code class="plain">d[</code><code class="value">10</code><code class="plain">] </code><code class="keyword">=</code> <code class="string">"Ten"</code></div><div class="line number44 index43 alt1"><code class="keyword">print</code><code class="plain">(</code><code class="string">"Dictionary"</code><code class="plain">, d)</code></div><div class="line number45 index44 alt2">&nbsp;</div><div class="line number46 index45 alt1"><code class="comments"># Removing key-value pair</code></div><div class="line number47 index46 alt2"><code class="keyword">del</code> <code class="plain">d[</code><code class="value">10</code><code class="plain">]</code></div><div class="line number48 index47 alt1"><code class="functions">print</code><code class="plain">(</code><code class="string">"Dictionary"</code><code class="plain">, d)</code></div></div></td></tr></tbody></table>

**Output**

```
Adding 5 and 10 in list [5, 10]
Popped one element from list [5]

Adding 5 and 10 in set {10, 5}
Removing 5 from set {10}

Tuple (5,)

Dictionary {5: 'Five', 10: 'Ten'}
Dictionary {5: 'Five'}
```

### Applications of List, Set, Tuple, and Dictionary

**List:**

-   Used in JSON format
-   Useful for Array operations
-   Used in Databases

**Tuple:**

-   Used to insert records in the database through SQL query at a time.Ex: (1.’sravan’, 34).(2.’geek’, 35)
-   Used in parentheses checker

**Set:**

-   Finding unique elements
-   Join operations

**Dictionary:**

-   Used to create a data frame with lists
-   Used in JSON
