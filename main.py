"""You can test your functions in this module as in the following code: """


from formula import *
from functions import *


formula1 = Atom('p')  # p
formula2 = Atom('q')  # q
formula3 = And(formula1, formula2)  # (p /\ q)
formula4 = And(Atom('p'), Atom('s'))  # (p /\ s)
formula5 = Not(And(Atom('p'), Atom('s')))  # (¬(p /\ s))
formula6 = Or(Not(And(Atom('p'), Atom('s'))), Atom('q'))  # ((¬(p /\ s)) v q)
formula7 = Implies(Not(And(Atom('p'), Atom('s'))), And(Atom('q'), Atom('r')))  # ((¬(p /\ s)) -> (q /\ r))
formula8 = Implies(Not(And(Atom('p'), Atom('s'))), And(Atom('q'), Not(And(Atom('p'), Atom('s')))))
# ((¬(p /\ s)) -> (q /\ (¬(p /\ s))))


print(formula1 == formula3)
print(formula1 == formula2)
print(formula3 == And(Atom('p'), Atom('q')))

print('formula1:', formula1)
print('formula2:', formula2)
print('formula3:', formula3)
print('formula4:', formula4)
print('formula5:', formula5)
print('formula6:', formula6)
print('formula7:', formula7)
print('formula8:', formula8)

print('length of formula1:', length(formula1))
print('length of formula3:', length(formula3))

print('length of formula7:', length(formula7))

print('subformulas of formula7:')
print(subformulas(formula7))
for subformula in subformulas(formula7):
    print(subformula)

print('length of formula8:', length(formula8))
print('subformulas of formula8:')
for subformula in subformulas(formula8):
    print(subformula)

#  we have shown in class that for all formula A, len(subformulas(A)) <= length(A):
# for example, for formula8:
print('number of subformulas of formula8:', len(subformulas(formula8)))
print('len(subformulas(formula8)) <= length(formula8):', len(subformulas(formula8)) <= length(formula8))

# testing number_of_atoms() method
print('number of atoms:', number_of_atoms(formula3))

# testing atoms() method
print('atoms of formula8:')
for atom in atoms(formula3):
    print(atom)

# testing number_of_connectives() method
print('number of connectives of formula3:', number_of_connectives(formula3))

# testing substitution() method
formula10 = Implies(And(Atom('p'), Not(Atom('q'))), Atom('r'))  # (((p ^ ¬q)) -> r)
formula11 = Not(Atom('q'))
formula12 = Or(Atom('r'), Atom('t'))
print(formula10)
print(formula11)
print(formula12)
print()
print('substitution of formula10:', substitution(formula10, formula11, formula12))