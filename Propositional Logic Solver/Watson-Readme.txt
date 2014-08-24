                             WATSON-README
======================================================================

What is it ?
------------

Watson is an automatic theorem prover for propositional logic using 
resolution.


INPUT/OUTPUT Specification
--------------------------

Input from stdin has syntax: LHS => RHS
Both LHS and RHS are well formed propositional logic formulae:

1. English letters stand for basic propositions.

2. Letters may be joined using connectives: ~ (not), ^ (and), | (or), 
-> (conditional), <-> (biconditional)

3. Brackets may be used for grouping.

4. If brackets are omitted, precedence is used. Precedence order is as above.

Output: 1 (for Valid) or 0 (for not Valid).


Sample I/O - 
-------------

Examples 
1. Input : p,~q=>p
Output:1

2. Input:p|q,~q|r=>p|r
Output:1

3. Input:p|q,~q|r=>r
Output:0


4. p|q,p->r,q->r=>r
Output:1

5. (p->q)->q,(p->p)->r,(r->s)->(~s->q)=>r
Output:1

6.  (p->q)->q,(p->p)->r,(r->s)->(~s->q)=>p
Output:0


Code has 4 modules:

1. A module to parse well formed formulae into internal data structures.

2. A module to convert a formula into CNF.

3. A module to apply resolution on a given set of clauses.

4. A module that takes input and uses above modules to give output.


USAGE
-----

The program takes as input the number of testcases (t) and 
output t binary values on t separate lines.
The following is how the input to watson would look like:

Input: (from stdin)

6
p,~q=>p
p|q,~q|r=>p|r
p|q,~q|r=>r
p|q,p->r,q->r=>r
(p->q)->q,(p->p)->r,(r->s)->(~s->q)=>r
(p->q)->q,(p->p)->r,(r->s)->(~s->q)=>p


Output: (to stdout)
1
1
0
1
1
0

Note:
p->q is "(p logically implies q)" whereas P => Q is used to denote that 
P is a set of premises and Q is the goal.
