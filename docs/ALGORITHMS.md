# 🧠 Algorithmic Patterns Study Notes

This document contains key concepts, patterns, and strategies for solving common Data Structures and Algorithms problems.

---

## 1. (Sliding Window Algorithm)

The **Sliding Window** technique is used to process a contiguous block of elements in a sequence (array, list, string) efficiently. It avoids redundant computations by reusing results of the overlapping parts of the window.

### Core Concept
Instead of recalculating results from scratch for every subarray/substring, we maintain a "window" of elements. As we slide the window forward, we add the new element entering the window and remove the old element leaving the window.

* **Time Complexity**: $\mathcal{O}(N)$ (since each element is visited at most twice: once entering and once leaving the window)
* **Space Complexity**: $\mathcal{O}(1)$ or $\mathcal{O}(K)$ depending on whether we store window elements.

### Types of Sliding Window
1. **Fixed-Size Sliding Window**: The size of the window $K$ is constant.
   * *Example*: Find the maximum sum of any contiguous subarray of size $K$.
2. **Variable-Size Sliding Window**: The window size expands or contracts based on constraints.
   * *Example*: Find the longest substring without repeating characters.

---

## 2. (Two Pointer Technique)

The **Two Pointer** technique uses two reference pointers traversing through a sequence (usually an array or linked list) to find target pairs or sub-segments.

### Variants of Two Pointers
1. **Opposite Direction**: Pointers start at opposite ends (`left = 0`, `right = len(arr) - 1`) and move toward each other.
   * *Common use cases*: Palindrome checks, reversing arrays, finding pairs in a sorted array (e.g., Two Sum II).
2. **Same Direction (Slow/Fast Pointers)**: Both pointers start at one end but move at different speeds or conditions.
   * *Common use cases*: Removing duplicates from sorted array, finding the middle of a linked list, cycle detection (Floyd's Tortoise and Hare).

### When to Use?
* When the input is sorted or can be sorted (most critical indicator).
* When working with Linked Lists.
* When finding pairs, triplets, or subarrays in a linear structure satisfying a specific sum or property.
* For in-place array transformations (e.g., reverse, partition, merge).


# backtracking
A simple mental model

Whenever you're stuck on a backtracking problem, ask these 4 questions:

1. What is my current state?
2. What choices do I have?
3. When is my solution complete?
4. What do I need to undo after recursion?

For Letter Combinations:

Current state → current string
Choices       → letters mapped to current digit
Complete      → processed all digits
Undo          → not required because we create new strings

For Subsets:

Current state → current subset
Choices       → take / don't take
Complete      → processed all numbers
Undo          → current.pop()

For Permutations:

Current state → current permutation
Choices       → unused numbers
Complete      → permutation length == input length
Undo          → pop + remove from used