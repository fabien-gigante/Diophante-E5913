from typing import Iterable, Tuple, Union, List

Hand = Tuple[int,int,int,int]
Deal = Tuple[Hand,Hand,Hand,Hand]
Several = ...
SeveralType = type(Several)

def hands() -> Iterable[Hand]:
    for a in range(1, 14):
        for b in range(a + 1, 15):
            for c in range(b + 1, 16):
                for d in range(c + 1, 17):
                    yield (a,b,c,d)

primes = [2,3,5,7,11,13]
factorials = [1,2,6,24,120,720,5040,40320]

def all_primes(x: Hand) -> bool:     return all(a in primes for a in x)
def is_arithmetic(x: Hand) -> bool:  (a,b,c,d) = x ; return b-a == c-b == d-c
def product(x: Hand) -> int:         (a,b,c,d) = x ; return a*b*c*d
def is_factorial(x: Hand) -> bool:   return product(x) in factorials
def are_disjoint(*s: Hand) -> bool:  return len({x for h in s for x in h}) == sum(len(h) for h in s)

hands_a = [ *filter(all_primes, hands()) ]
hands_b = [ *filter(is_arithmetic, hands()) ]
hands_c = [ *filter(is_factorial, hands()) ]

def known(d: Hand) -> Union[Deal, None, SeveralType]:
    sol: Union[Deal, None] = None
    for c in filter(lambda c: are_disjoint(c,d), hands_c):
        for b in filter(lambda b: are_disjoint(b,c,d), hands_b):
            for a in filter(lambda a: are_disjoint(a,b,c,d), hands_a):
                if sol is not None: return Several
                else: sol = (a,b,c,d)
    return sol
def is_unique(x: Union[Deal, None, SeveralType]) -> bool: 
    return x is not None and x is not Several

sols: List[Deal] = [*filter(is_unique, (known(d) for d in hands()))]
print(f'Number of D hands with a unique deal : {len(sols)}')
set_k = sorted({ product(c) for (a,b,c,d) in sols })
print(f'Values of k! for those deals : {set_k}')
for k in set_k:
    sols_k = [(a,b,c,d) for (a,b,c,d) in sols if product(c) == k]
    print(f'- deals with k! = {k:5} :   {len(sols_k):3}', end = 6 * ' ')
    print(f'  eg. {sols_k[0]}')
