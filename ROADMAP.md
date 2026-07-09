# 🗺️ Data Structures and Algorithms (DSA) Study Roadmap

This roadmap tracks the learning progress, core concepts, and key problem types for mastering Data Structures and Algorithms. Use this checklist as a guide to prepare for technical interviews and build solid problem-solving foundations.

---

## 📅 Roadmap Overview

### 1. 数组 & 字符串 (Arrays & Strings)
*Core of 70% of problems. Focus on pointer manipulations and sliding windows.*
- [x] **Data Structures**: Static Arrays, Dynamic Arrays, Strings
- [x] **Algorithms & Patterns**:
  - Two Pointers (Opposite direction, same direction, fast & slow)
  - Sliding Window (Fixed-size, variable-size)
  - Prefix Sum
  - Kadane's Algorithm
  - Hashing Basics
- [x] **Common Problems**: Subarray/substring, frequency counting, rotation, anagrams
- *📌 Industry Relevance*: Logs, streams, metrics, and text processing.

### 2. 哈希表 (Hashing)
*Very high Return on Investment (ROI) for interviews.*
- [x] **Data Structures**: Hash Tables / Maps, Sets
- [x] **Core Concepts**: Collision handling, hash functions
- [x] **Patterns**:
  - Frequency Maps
  - Lookup Optimization (O(1) search)
  - Deduplication
- [x] **Must-Know Problems**: Two Sum, Longest Substring Without Repeating Characters, First Unique Element
- *📌 Industry Relevance*: Used everywhere in databases, caching, and backend systems.

### 3. 链表 (Linked Lists)
*Teaches pointer thinking and memory discipline.*
- [x] **Data Structures**: Singly Linked List, Doubly Linked List
- [x] **Core Concepts**: Reversal, fast & slow pointers (Floyd's Cycle Detection), sentinel nodes
- [x] **Key Algorithms**: Merge lists, reverse in groups, detect cycle, find intersection
- *📌 Industry Relevance*: Low-level memory management, LRU Cache.

### 4. 栈 & 队列 (Stacks & Queues)
*Control flow data structures.*
- [x] **Data Structures**: Stack, Queue, Deque (Double-Ended Queue)
- [x] **Patterns & Variants**: Monotonic Stack (for next greater/smaller element)
- [x] **Classic Problems**: Valid Parentheses, Next Greater Element, Min Stack, Sliding Window Maximum
- *📌 Industry Relevance*: Compilers, expression parsing, job scheduling.

### 5. 递归 & 回溯 (Recursion & Backtracking)
*Tests thinking clarity and decision tree exploration.*
- [x] **Core Concepts**: Call stack, base case design, decision trees
- [x] **Classic Problems**:
  - Subsets & Power Set
  - Permutations & Combinations
  - N-Queens Problem
  - Sudoku Solver
- *⚠️ Interview Tip*: Focus on code cleaness and drawing decision trees before coding.

### 6. 树 (Trees)
*Highly important for technical interviews.*
- [x] **Data Structures**: Binary Tree, Binary Search Tree (BST), Balanced Trees (AVL, Red-Black - conceptual)
- [x] **Algorithms**:
  - DFS (In-order, Pre-order, Post-order traversals)
  - BFS (Level-order traversal)
  - Height & Diameter of Tree
  - Lowest Common Ancestor (LCA)
  - Serialization / Deserialization
- *📌 Industry Relevance*: File systems, database indexing (B-Trees), search engines.

### 7. 堆 & 优先队列 (Heaps & Priority Queues)
*Optimizing search for minimum or maximum values.*
- [ ] **Data Structures**: Min-Heap, Max-Heap
- [ ] **Core Concepts**: Heapify, binary heap representation in arrays
- [ ] **Key Problems**:
  - Kth Largest/Smallest Element
  - Merge K Sorted Lists
  - Task Scheduling
- *📌 Industry Relevance*: Job schedulers, resource allocation.

### 8. 贪心算法 (Greedy Algorithms)
*Making locally optimal choices.*
- [ ] **Core Concepts**: Greedy choice property, optimal substructure, when greedy fails
- [ ] **Classic Problems**:
  - Activity Selection / Interval Scheduling
  - Minimum Platforms / Meeting Rooms
  - Huffman Encoding
- *📌 Industry Relevance*: Compression algorithms, network optimization.

### 9. 图论 (Graphs)
*Industry-critical topic for networking and relational data.*
- [ ] **Representations**: Adjacency List, Adjacency Matrix
- [ ] **Algorithms**:
  - Breadth-First Search (BFS) & Depth-First Search (DFS)
  - Topological Sort (Kahn's Algorithm)
  - Shortest Path (Dijkstra, Bellman-Ford)
  - Disjoint Set Union (Union-Find)
  - Cycle Detection (Directed & Undirected graphs)
- *📌 Industry Relevance*: Social networks, dependency resolution, network routing.

### 10. 动态规划 (Dynamic Programming)
*Most interview-heavy topic. Focus on recognizing patterns.*
- [ ] **Framework**: Recursion ➔ Memoization (Top-down) ➔ Tabulation (Bottom-up) ➔ Space Optimization
- [ ] **Common Patterns**:
  - 0/1 Knapsack & Unbounded Knapsack
  - Longest Common Subsequence (LCS)
  - Longest Increasing Subsequence (LIS)
  - Matrix DP (Grid paths, Min path sum)
  - DP on Trees
- *⚠️ Interview Expectation*: You must explain your DP state and transition relation clearly.

### 11. 高级主题 (Advanced / Optional)
*Good to know for senior, system design, or specialized roles.*
- [ ] **Tries** (Prefix Trees for auto-complete)
- [ ] **Segment Trees & Fenwick Trees** (Range queries)
- [ ] **String Search**: KMP Algorithm, Z-Algorithm
- [ ] **Bit Manipulation** (Bitwise hacks)
- [ ] **LRU Cache Design** (Combined Double LinkedList + HashMap)
