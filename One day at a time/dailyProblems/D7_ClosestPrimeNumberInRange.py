'''
Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.
Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
 

Constraints:

1 <= left <= right <= 10^6
'''

# man idk what I even did

class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        prime = [True for i in range(right+1)]
        primes =[]
        # boolean array
        p = 2
        while (p * p <= right):
    
            # If prime[p] is not
            # changed, then it is a prime
            if (prime[p] == True):
    
                # Updating all multiples of p
                for i in range(p * p, right+1, p):
                    prime[i] = False
            p += 1
    
        for p in range(left, right+1):
            if prime[p]:
                primes.append(p)
 
        if len(primes) <= 1:
            return [-1,-1]

        if primes[0] == 1 and primes[1] == 2 and len(primes) == 2:
            return [-1,-1]

        if primes[0] == 1:
            mins = primes[2] - primes[1]
            lowest = [primes[1], primes[2]]
        else:
            mins = primes[1] - primes[0]
            lowest = [primes[0], primes[1]]


        for i in range(1, len(primes)-1):
            if primes[i+1] - primes[i] >= mins:
                pass
            else:
                mins = primes[i+1] - primes[i]
                lowest = [primes[i], primes[i+1]]

        return lowest


    # fastest way?

    def closestPrimes(self, left, right):
        q = []
        diff = float('inf')
        pair = [-1,-1]
        for i in range(left,right+1):
            if self.isPrime(i): 
                q.append(i)
            while len(q)>=2:
                if abs(q[0]-q[1])<diff:
                    pair=[q[0],q[1]]
                    diff=abs(q[0]-q[1])  
                    if diff<=2: return pair
                q.pop(0)
        return pair
    

    def isPrime(self, num):
        if num<2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True



        