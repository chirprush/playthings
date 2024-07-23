#!/usr/bin/env python3
class Var:
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp
    def __repr__(self):
        if (self.exp == 0):
            return "1"
        elif (self.exp == 1):
            return self.name
        else:
            return "%s^%d"%(self.name, self.exp)

class Term:
    def __init__(self, co, variables):
        self.co = co
        self.vars = variables
    def __repr__(self):
        vars_repr = "".join([str(i) for i in self.vars])
        if (self.co == 0):
            return "0"
        elif (self.co == 1):
            return vars_repr
        else:
            return "%d%s" % (self.co, vars_repr)

print(__name__)
print(__name__ == "__main__")
if (__name__ == "__main__"):
    print(Term(-2, [Var("x", 3)]))
