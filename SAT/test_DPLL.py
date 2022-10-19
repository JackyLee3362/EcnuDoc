from sympy import symbols
from DPLL import dpll_algorithm, Conjunctive

def test_DPLL():
  a, b, c, d, e = symbols('a b c d e')
  conj = [[~c], [~b], [d, e], [~a], [a, c]]
  assert dpll_algorithm(Conjunctive(conj)) == 0
  conj = [[a,~b], [~a,b]]
  assert dpll_algorithm(Conjunctive(conj)) == 1