# Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## Approach & Explanation
Used a hash map (dictionary) to store each number's complement (`target - num`) as we iterate through the array. This allows us to look up the required matching number in $O(1)$ time.

## Complexity Analysis
- **Time Complexity:** $O(n)$ because we iterate through the array once.
- **Space Complexity:** $O(n)$ to store up to $n$ elements in the hash map.

## Code Reference
Solution implemented in [`01-two-sum.py`](./01-two-sum.py).