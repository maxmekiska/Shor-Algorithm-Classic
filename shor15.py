'''
Reference:

Qiskit, 2020. 11. Shor's algorithm II: From Factoring to Period-Finding, Writing the Quantum Program - Part 2. [video] Available at: <https://www.youtube.com/watch?v=dscRoTBPeso&t=1745s> [Accessed 2 October 2021].
'''




class Factor15():
    '''Class to implement the Shor algorithm (classicly). Tested on number 15.

    Methods
    -------

    _gcd(self, *vartuple):
        Private method to compute the greatest common divisor.
    _is_prime(self, target: int):
        Private method to test if a number is a prime.
    _co_primelist(self, target: int):
        Private method to create a list of co-prime numbers for a targer value.
    _shor_subroutine(self, target: int, coprime: int):
        Private method that implements a simplified version of the Shor algorithm.
    _apply(self, target:int ):
        Method to apply the shor algorithm.
    compute(self):
        Method to repeat shor algorithm calculations until no non-prime factors are left in the factor list.
    '''
        
    def __init__(self, target: int) -> object:
        '''
            Parameters:
                target (int): Number (15) to be factored.
        '''
        self.target = target
        
        self.coprimes = []

        self.factors = []
                
    def __str__(self):
        '''Prints the co-prime list computed for the target value.'''
        return f"Co-Primes used: {self.coprimes}"
        
    def _gcd(self, *vartuple) -> int:
        '''Function to implement greatest common divisor.

            Parameters:
                vartuple (*vartuple): Numbers for which gcd needs to be computed.

            Returns:
                greatest_common_divisor (int): GCD.
        '''
        targets = vartuple
        number_elements = len(targets)
        divisors = []
        common_divisors = []
    
        for i in vartuple:
            for j in range(i+1):
                if j == 0:
                    continue
                elif i % j == 0:
                    divisors.append(j)
                
        for i in divisors:
            if divisors.count(i) == number_elements :
                common_divisors.append(i)
                
        greatest_common_divisor = max(common_divisors)
    
        return greatest_common_divisor
    
    def _is_prime(self, target: int) -> bool:
        '''Tests if number supplied is a prime.

            Parameters:
                target (int): Number to be tested if is prime.

            Returns:
                (bool): True when prime, False when not prime.
        '''
        if target == 1:
            return True
        
        if target > 1:
        
            for i in range(2, target):
                if (target % i) == 0:
                    return False
                else:
                    return True
                
    def _co_primelist(self, target: int) -> [int]:
        '''Generates all co-prime numbers up until the targert itself.

            Parameters:
                target (int): Number for which co-primes will be computed.

            Returns:
                co_primes [int]: List containing all computed co-prime values.  
        '''
        co_primes = []
        for i in range(2, target):
            if self._gcd(i, target) == 1 and self._is_prime(i):
                co_primes.append(i)
        return co_primes
    
    def _shor_subroutine(self, target: int, coprime: int) -> [int, int]:
        '''Simplified implementation of Shors algorithm.
    
        Parameters:
            target (int): Value to be factored.
            coprime (int): Coprime elected.
        
        Returns:
            (int, int): Tuple containing factors.
        '''
        r = 2
        while coprime**r % target != 1:
            r += 1
    
        if r % 2 == 0:
            x = int((coprime**(r/2)) % target)
        
            if (x+1) % target != 0:
                return [self._gcd(x+1, target), self._gcd(x-1, target)]
            else:
                return 0
        else:
            return 0
        
    def _apply(self, target: int) -> int:
        '''Method to apply the shor algorithm.
            
            Returns:

                [int, int]: list containing factors.
        '''
        self.target = target
        self.coprimes = self._co_primelist(target)
        i = 0
        while self._shor_subroutine(target, self.coprimes[i]) == 0:
            i += 1
        return self._shor_subroutine(target, self.coprimes[i])


    def compute(self) -> int:
        '''Method to repeat shor algorithm calculations until no non-prime factors are left in the factor list.

            Returns:
                [int, int]: list containing factors.
        '''
        self.factors.extend(self._apply(self.target))
        i = 0
        length_factors = len(self.factors)
        while length_factors > i:
            if self._is_prime(self.factors[i]) == False:
                self.factors.extend(self._apply(self.factors[i]))
                del(self.factors[i])
                length_factors = len(self.factors)

            i += 1 
        
        return self.factors

if __name__ == "__main__":
    test = Factor15(15)
    print(test.compute())
