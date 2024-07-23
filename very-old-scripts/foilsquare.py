#!/usr/bin/python3.8

from itertools import count

class Var:
    def __init__(self, name, degree=1):
        self.name = name
        self.degree = degree

    def __str__(self):
        if self.degree == 1:
            return self.name
        return f"{self.name}^{self.degree}"

class Term:
    def __init__(self, co, variables={}):
        self.co = co
        self.variables = variables

    def alike(self, other):
        if len(other.variables) != len(self.variables):
            return False
        for v in self.variables:
            if v not in other.variables:
                return False
            elif other.variables[v].degree != self.variables[v].degree:
                return False
        return True

    def add(self, other):
        if not self.alike(other):
            raise ValueError
        return Term(self.co + other.co, self.variables)

    def mult(self, other):
        co = self.co * other.co
        result = Term(co, other.variables.copy())
        for v in self.variables:
            var = self.variables[v]
            if v not in result.variables:
                result.variables[v] = var
            else:
                result.variables[v].degree += var.degree
        return result

    def __str__(self):
        output = ""
        if self.co == -1:
            output += "-"
        elif self.co != 1:
            output += str(self.co)
        for v in self.variables:
            output += str(self.variables[v])
        return output

class Expr:
    def __init__(self, terms):
        self.terms = terms

    def mult(self, other):
        terms = []
        print(self)
        print(other)
        for term1 in self.terms:
            for term2 in other.terms:
                print(self)
                print(other)
                print(term1, term2)
                terms.append(term1.mult(term2))
        return Expr(terms)

    def simplify(self):
        terms = []
        for i, term in enumerate(self.terms):
            accum = term
            for j, other_term in enumerate(self.terms):
                if i == j:
                    continue
                if accum.alike(other_term):
                    accum = accum.add(other_term)
            terms.append(accum)
        return Expr(terms)

    def __str__(self):
        return ' + '.join(str(i) for i in self.terms)

expr = Expr([Term(1, {"a" : Var("a")}), Term(1, {"b" : Var("b")})])
other_expr = Expr([Term(1, {"a" : Var("a")}), Term(1, {"b" : Var("b")})])
print(expr.mult(other_expr))
