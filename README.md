# 🚀 Data Structures & Algorithms (DSA) Practice

Welcome to my DSA repository! This repository is dedicated to my learning journey in Data Structures, Algorithmic Patterns, and LeetCode problem-solving. It is structured to be clean, modular, and maintainable, adhering to professional Python packaging standards.

---

## 📁 Repository Structure

```text
DSA/
├── docs/                      # Study notes and roadmaps
│   ├── ALGORITHMS.md          # Theoretical notes on key patterns
│   └── ROADMAP.md             # Topic-wise curriculum and progress tracker
├── pyproject.toml             # Python packaging configuration (Poetry)
├── poetry.lock                # Locked dependencies
└── src/
    ├── dsa_practice/          # Custom implementation of DS & Algorithms
    │   ├── data_structures/   # Stacks, Queues, Binary Trees, General Trees
    │   ├── searching/         # Linear Search, Binary Search
    │   ├── sorting/           # Bubble Sort, Selection Sort, Insertion Sort
    │   └── patterns/          # Two Pointers, Sliding Window, Backtracking
    ├── leetcode/              # Solutions to LeetCode problems
    │   ├── easy/              # Easy difficulty problems (20, 206, 217, etc.)
    │   └── medium/            # Medium difficulty problems (3, 5, 11, 74, etc.)
    └── playground/            # Local test scripts & scratchpads
```

---

## 🛠️ Tech Stack & Setup

* **Language**: Python 3.12+
* **Dependency Manager**: [Poetry](https://python-poetry.org/)
* **Formatters & Linters**: Built following PEP 8 guidelines

### Getting Started

1. **Install Dependencies**:
   Ensure you have Poetry installed, then run:
   ```bash
   poetry install
   ```

2. **Run Practice Scripts**:
   You can execute any of the modules using system Python or Poetry. For example, to run Binary Search:
   ```bash
   poetry run python -m src.dsa_practice.searching.binary_search
   ```

3. **Use the Playground**:
   Try out experimental code in the playground:
   ```bash
   poetry run python src/playground/scratchpad.py
   ```

---

## 📚 Topics & Implementations

### 1. Data Structures (`src/dsa_practice/data_structures/`)
* [Stack](src/dsa_practice/data_structures/stack.py) - LIFO structure implemented using dynamic arrays.
* [Queue](src/dsa_practice/data_structures/queue.py) - FIFO structure with enqueue, dequeue, and peek operations.
* [Binary Search Tree Node](src/dsa_practice/data_structures/binary_tree.py) - Binary Search Tree representation with Pre-order, In-order, and Post-order Traversals.
* [General Tree Node](src/dsa_practice/data_structures/general_tree.py) - Multi-branch tree representation.

### 2. Basic Algorithms (`src/dsa_practice/searching/` & `src/dsa_practice/sorting/`)
* [Linear Search](src/dsa_practice/searching/linear_search.py) - Simple $\mathcal{O}(n)$ search traversal.
* [Binary Search](src/dsa_practice/searching/binary_search.py) - Efficient $\mathcal{O}(\log n)$ search on sorted arrays.
* [Bubble Sort](src/dsa_practice/sorting/bubble_sort.py) - Basic adjacent-swap sorting algorithm.
* [Selection Sort](src/dsa_practice/sorting/selection_sort.py) - In-place comparison sorting by selecting minimum elements.
* [Insertion Sort](src/dsa_practice/sorting/insertion_sort.py) - Building sorted array element-by-element.

### 3. Algorithmic Patterns (`src/dsa_practice/patterns/`)
* [Two Pointers](src/dsa_practice/patterns/two_pointers.py) - Reverse arrays, palindrome checks, merge sorted arrays, remove duplicates.
* [Sliding Window](src/dsa_practice/patterns/sliding_window.py) - Fixed/variable subarray algorithms (e.g., Max Average Subarray).
* [Backtracking](src/dsa_practice/patterns/backtracking.py) - Exploration of decision trees (e.g., Subsets, Permutations).

---

## 🏆 LeetCode Solutions Tracker

Here is a list of LeetCode problems solved in this repository, organized by difficulty:

### 🟢 Easy Difficulty (`src/leetcode/easy/`)

| # | Problem Title | Solution File | Concepts |
|---|---------------|---------------|----------|
| 1 | Two Sum | [1_two_sum.py](src/leetcode/easy/1_two_sum.py) | HashMap, Lookup Optimization |
| 20 | Valid Parentheses | [20_valid_parentheses.py](src/leetcode/easy/20_valid_parentheses.py) | Stack, String Matching |
| 26 | Remove Duplicates | [26_remove_duplicates.py](src/leetcode/easy/26_remove_duplicates.py) | Two Pointers (Same Direction) |
| 121 | Best Time to Buy and Sell Stock | [121_best_time_to_buy_and_sell_stock.py](src/leetcode/easy/121_best_time_to_buy_and_sell_stock.py) | Greedy, Single Pass, Array |
| 125 | Valid Palindrome | [125_valid_palindrome.py](src/leetcode/easy/125_valid_palindrome.py) | Two Pointers, String |
| 206 | Reverse Linked List | [206_reverse_linked_list.py](src/leetcode/easy/206_reverse_linked_list.py) | Linked List, Pointers |
| 217 | Contains Duplicate | [217_contains_duplicate.py](src/leetcode/easy/217_contains_duplicate.py) | HashSet, Deduplication |
| 326 | Power of Three | [326_power_of_three.py](src/leetcode/easy/326_power_of_three.py) | Recursion |
| 342 | Power of Four | [342_power_of_four.py](src/leetcode/easy/342_power_of_four.py) | Recursion |
| 509 | Fibonacci Number | [509_fibonacci_number.py](src/leetcode/easy/509_fibonacci_number.py) | Recursion, Memoization |
| 3304 | Find K-th Character in String Game I | [3304_find_kth_character_in_string_game_i.py](src/leetcode/easy/3304_find_kth_character_in_string_game_i.py) | String Manipulation |

### 🟡 Medium Difficulty (`src/leetcode/medium/`)

| # | Problem Title | Solution File | Concepts |
|---|---------------|---------------|----------|
| 3 | Longest Substring Without Repeating Characters | [3_longest_substring_without_repeating_characters.py](src/leetcode/medium/3_longest_substring_without_repeating_characters.py) | Sliding Window, Hash Set |
| 5 | Longest Palindromic Substring | [5_longest_palindromic_substring.py](src/leetcode/medium/5_longest_palindromic_substring.py) | Expand Around Center, DP |
| 11 | Container With Most Water | [11_container_with_most_water.py](src/leetcode/medium/11_container_with_most_water.py) | Two Pointers (Opposite Direction) |
| 15 | 3Sum | [15_3sum.py](src/leetcode/medium/15_3sum.py) | Sorting, Two Pointers |
| 74 | Search a 2D Matrix | [74_search_a_2d_matrix.py](src/leetcode/medium/74_search_a_2d_matrix.py) | Binary Search on 2D space |
| 167 | Two Sum II - Input Array Is Sorted | [167_two_sum_ii.py](src/leetcode/medium/167_two_sum_ii.py) | Two Pointers (Sorted Array) |
| 347 | Top K Frequent Elements | [347_top_k_frequent_elements.py](src/leetcode/medium/347_top_k_frequent_elements.py) | HashMap, Sorting |
| 390 | Elimination Game | [390_elimination_game.py](src/leetcode/medium/390_elimination_game.py) | Math, Pattern Tracking |
