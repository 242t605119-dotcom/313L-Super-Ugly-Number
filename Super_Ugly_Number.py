class Solution:
    def nthSuperUglyNumber(self, n, primes):
        ugly = [1] * n
        indices = [0] * len(primes)

        for i in range(1, n):
            next_ugly = min(
                primes[j] * ugly[indices[j]]
                for j in range(len(primes))
            )

            ugly[i] = next_ugly

            for j in range(len(primes)):
                if primes[j] * ugly[indices[j]] == next_ugly:
                    indices[j] += 1

        return ugly[-1]
