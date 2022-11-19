from pyprover import *
from pyprover.logic import Var

def vars (string) : return map(Var,string.split(" "))

def prove_by_refutation(givens,conclusion):
    if isinstance(givens, (list)):
        givens = And(*givens)
    # (permises & ~ conclusion) is contradiction
    return solve(givens & ~conclusion) == bot    

def prove_theorems(givens, theorems, from_exprs= False):
    if from_exprs:
        givens = list(map(expr,givens))
        theorems = map(expr,theorems)
    for theorem in theorems:
        result = prove_by_refutation(givens,theorem)
        print(
            "The Given Facts prove the theorem,",
            theorem,"as",result
        )

def find_matching_solutions(givens,query,from_exprs = False):
    if from_exprs:
        givens = list(map(expr,givens))
    expr_ = solve(And(*givens))
    while isinstance(expr_,(FA,TE)):
        expr_ = expr_.elem
    matches = [
        elem
        for elem in expr_.elems
        if query.find_unification(elem)
    ]
    return matches


if __name__ == "__main__":
    (
        Child,Loves,Raindeer,HasRedNose,Wierd,Clown
    ) =props(
        "Child Loves Raindeer HasRedNose Wierd Clown"
    )
    Santa,Rudo,Carl= terms("Santa Rudo Carl")

    givens = [
        FA(x,Child(x)>>Loves(x,Santa)),
        FA(x,FA(y,(Loves(x,Santa) & Raindeer(y))>>Loves(x,y))),
        Raindeer(Rudo) & HasRedNose(Rudo),
        FA(x, HasRedNose(x) >> (Wierd(x) | Clown(x))),
        FA(x, Raindeer(x)>> ~Clown(x)),
        FA(x, Wierd(x) >> ~Loves(Carl,x))
    ]
    theorems=[
        ~Child(Carl),
        Loves(Carl,Santa),
    ]
    print("THEOREM PROVING:\n")
    prove_theorems(givens,theorems)

    givens = [
        "A x. A y. Child(x) & Candy(y) -> Loves(x,y)",
        "A x. E y. Candy(y) & Loves(x,y) -> ~NutritionFan(x)",
        "A x. A y. Pumpkin(y) & Eats(x,y) -> NutritionFan(x)",
        "A x. A y. Pumpkin(y) & Buys(x,y) -> Eats(x,y)",
        "E y. Buys(john,y) & Pumpkin(y)",
    ]

    theorems = [
        "E y. Eats(john,y) & Pumpkin(y)",
        "NutritionFan(john)",
        "Child(john)",

    ]
    
    print("\nTHEOREM PROVING USING THEOREM EXPRESSIONS:\n")
    prove_theorems(givens, theorems,True)

    SimpleSentence, = props("SimpleSentence")    
    x1,z1,u1,v1  = vars("x1 z1 u1 v1")
    dog, = terms("dog")
    query = SimpleSentence(x1,dog,z1,u1,v1)
    givens = [
        '''\
A x. A y. A z. A u. A v. (
    Article(x)& Noun(y) & Verb(z) & Article(u) & Noun(v) -> SimpleSentence(x,y,z,u,v)
)''',
        "Article(a) & Article(the)",
        "Noun(man) & Noun(dog) ",
        "Verb(likes) & Verb(bites)",
    ]
    print("\nFINDING SOLUTIONS:\n")
    print("GIVENS:\n")
    for permise in givens: print(permise)
    print("\nQUERY:\n")
    print(query)
    solutions = find_matching_solutions(givens, query,True)
    print("\nSOLUTIONS:\n")
    for solution in solutions:print(*solution.args)