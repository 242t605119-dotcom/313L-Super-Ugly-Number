# LeetCode 313 - Super Ugly Number

## Problem Statement

A **Super Ugly Number** is a positive integer whose prime factors are all present in the given array `primes`.

Given an integer `n` and an array of prime numbers `primes`, return the `n`th Super Ugly Number.

## Example 1

### Input

```text
n = 12
primes = [2,7,13,19]
```

### Output

```text
32
```

## Example 2

### Input

```text
n = 1
primes = [2,3,5]
```

### Output

```text
1
```

## Approach

Use **Dynamic Programming** with multiple pointers.

The `ugly` array stores the Super Ugly Numbers found so far. Each prime has a pointer that tells us which existing number should be multiplied by that prime to generate the next possible value.

## Algorithm

1. Initialize the first Super Ugly Number as `1`.
2. Create an index for each prime number.
3. Find the smallest value obtained by multiplying each prime with its current indexed Ugly Number.
4. Add the smallest value to the `ugly` array.
5. Move the pointers that produced the selected value.
6. Repeat until the `n`th number is generated.
7. Return the last value.

## Time Complexity

`O(n × k)`

where `k` is the number of primes.

## Space Complexity

`O(n + k)`

## Key Concepts

* Dynamic Programming
* Arrays
* Multiple Pointers
* Prime Numbers
* Sequence Generation

## Language

Python

## LeetCode Details

* **Problem:** 313
* **Title:** Super Ugly Number
* **Difficulty:** Medium

## Author

**T. Nandhini Reddy**

GitHub: `242t605119-dotcom`
