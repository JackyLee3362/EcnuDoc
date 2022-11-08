# Conflict Driven Clause Learning

​					University of Washington | CSE 442

------

https://cse442-17f.github.io/Conflict-Driven-Clause-Learning/

We have a sudoku board!
You may assume a solution exists, but how can we check?

## The Boolean Satisfiability Problem

The Boolean Satisfiability Problem is one in which we have to decide if there exists an assignment for some boolean variables that would make a boolean formula evaluate to true.

If a formula has an assignment under which the formula evaluates to True, then it is satisfiable. If no such assignment exists for a formula, then it is unsatisfiable.

In general, the **Boolean Satisfiability Problem** can take a very long time to solve (in fact, it’s NP-Complete). If a boolean formula has n variables, then there are 2^n possible assignments. All known algorithms, in the worst case, will have to do a full search on that exponentially sized search space. However, in real world problems, there are often logical structures in the problem that an algorithm can utilize to search better.

In this article, we will be covering two algorithms that try to find a satisfying assignment for a formula (SAT solvers). The first one will be the Davis-Putnam-Logemann-Loveland Algorithm developed in the 1960s, which forms the basis for modern SAT solving algorithms today. The second one will be the Conflict-Driven Clause Learning Algorithm which is more recent - around 1996, which improves on the first algorithm in really cool ways.

Both algorithms will only work on boolean formulas that are in Conjunctive Normal Form (CNF). In this form, boolean formulas are composed of the ANDs (∧) of clauses, clauses are the ORs (v) of literals, and literals are a variable or its negation.

Formulas in CNF have some nice properties that make reasoning quick. Since the formula is just the clauses ANDed together, for our formula to be satisfied every clause must be satisfied. Since each clause is made of the ORs of literals, only one literal needs to be satisfied for the whole clause to be satisfied.

Below is the example formula f = (-x1 ∨ -x2 ∨ x3) ∧ (-x3 ∨ x4). See if you can find assignments that satisfy this formula.

![](E:\研究生\智能系统分析与验证\Snipaste_2022-10-15_10-30-27.png)

The visualization starts out by visualizing the formula in a single line. This can be unwieldy for large formulas. We will visualize it instead by having each clause on its own line. Clicking the “To Clauses” and the “To Formula” button will show you the difference in the visualizations. Just remember that all clauses must be true for the formula to be true.

## Boolean Constraint Propagation

When an algorithm searches for a satisfying assignment for a CNF formula, one optimization is to look for unit clauses. A clause is unit under a partial assignment when that assignment makes every literal in the clause unsatisfied but leaves a single literal undecided.

Because the clause must be satisfied for the formula to be satisfied, there’s no point in checking any assignment that would make that undecided literal false. The algorithm can just make its next guess such that the literal will be true and thus the clause true.

This process is known as Boolean Constraint Propagation (BCP). Algorithms will run BCP to assign variables that logically only have one option due to unit clauses. Sometimes, doing BCP for unit clauses will cause other clauses to become unit! Algorithms will run BCP repeatedly until there are no unit clauses.

In the example below, we have guessed so far that x1 and x2 are both true. Try to predict how BCP will work below.

![](E:\研究生\智能系统分析与验证\Snipaste_2022-10-15_10-40-00.png)

## Davis-Putnam-Logemann-Loveland Algorithm

The DPLL algorithm is a SAT solver based on recursive backtracking that makes use of BCP. While a naive recursive backtracker would check every possible assignment until it found one that satisfies the formula, DPLL makes BCP-driven inferences to cut down on the size of the search tree – removing assignments that can’t satisfy the formula. When it encounters a conflict, it backtracks to the last non-BCP decision it made, and makes the other choice.

Here’s the pseudo-code:

```pseudocode
DPLL:
  Run BCP on the formula.
  If the formula evaluates to True, return True.
  If the formula evaluates to False, return False.
  If the formula is still Undecided:
    Choose the next unassigned variable.
    Return (DPLL with that variable True) || (DPLL with that variable False)
```


See how DPLL works with the example below. On the left, we have a visualization of the decision tree which shows the history of choices that the algorithm makes. Edges that are solid represent the guesses/decisions the algorithm makes, while edges that are dashed represent that the algorithm used BCP to get that choice. The path in blue leads to where the algorithm currently is at.

![](E:\研究生\智能系统分析与验证\Snipaste_2022-10-15_10-50-10.png)

Finally, DPLL finds an assignment that satisfies the formula. We can return that the formula is satisfiable now!

This example highlights some problems that DPLL has. When it makes a mistake, it doesn’t think about the mistake on a deeper level than just seeing that the current partial assignment won’t work. In this example, it doesn’t realize that x5 has to be false when x1 is true or else it will BCP itself into a conflict on clause 4.