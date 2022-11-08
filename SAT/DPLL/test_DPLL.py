from sympy import symbols
from DPLL import ConjunctiveNormalForm, DPLL

def test_DPLL():
  a, b, c, d, e = symbols('a b c d e')
  l = [[~c], [~b], [d, e], [~a], [a, c]]
  assert DPLL(ConjunctiveNormalForm(l)) == 0 
  l = [[a,~b], [~a,b]]
  assert DPLL(ConjunctiveNormalForm)