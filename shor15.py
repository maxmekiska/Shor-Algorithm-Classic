class Factor15():
        
    def __init__(self, target):
        self.target = target
        
        self.coprimes = []
        
        
    def __str__(self):
        return f"Co-Primes used: {self.coprimes}"
        
    def gcd(self, *vartuple) -> int:
        ''' Function to implement greatest common divisor.'''
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
    
    def is_prime(self, target: int) -> bool:
        ''' Tests if number supplied is a prime.'''
        if target == 1:
            return True
        
        if target > 1:
        
            for i in range(2, target):
                if (target % i) == 0:
                    return False
                else:
                    return True
                
    def co_primelist(self, target: int) -> [int]:
        ''' Generates all co-prime numbers up until the targert itself.'''
        co_primes = []
        for i in range(2, target):
            if self.gcd(i, target) == 1 and self.is_prime(i):
                co_primes.append(i)
        return co_primes
    
    def shor_subroutine(self, target: int, coprime: int) -> (int, int):
        ''' Simplified implementation of Shors algorithm.
    
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
                return [self.gcd(x+1, target), self.gcd(x-1, target)]
            else:
                return 0
        else:
            return 0
        
    def compute(self):
        self.coprimes = self.co_primelist(self.target)
        i = 0
        while self.shor_subroutine(self.target, self.coprimes[i]) == 0:
            i += 1
        return self.shor_subroutine(self.target, self.coprimes[i])

test = Factor15(15)
test.compute()
