import math
from typing import List

def factors_of_number(n: int ) -> List[int]:
    if n == 0:
        return ['Zero input - all integers are factors of 0!']

    n_abs = abs(n)
    factors = set()

    for i in range(1, int(math.isqrt(n_abs)) + 1):
        print(f'Checking value {i}')
        if n_abs % i == 0:
            print(f'Adding factor {i}')
            factors.add(i)
            print('Adding factor {}'.format(n_abs // i))
            factors.add(n_abs // i)

    if n < 0:
        factors = factors.union( {-f for f in factors} )

    return sorted(factors)


if __name__ == '__main__':
    num = input( 'Enter the number to factorize: ' )

    factors = factors_of_number( int(num) )
    print( f'The factors of {num} are: {factors}' )
