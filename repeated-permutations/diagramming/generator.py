from dataclasses import dataclass
from typing import List, TextIO

@dataclass
class Arrow:
    start: int
    end: int

@dataclass
class Permutation:
    m: int
    swaps: List[Arrow]

    def id(self) -> str:
        start = list(range(1, self.m + 1))

        for swap in self.swaps:
            temp = start[swap.end - 1]
            start[swap.end - 1] = start[swap.start - 1]
            start[swap.start - 1] = temp

        return ''.join(map(str, start))

    def draw(self, buffer: TextIO) -> None:
        buffer.write("\\begin{center}\n")
        buffer.write("\\begin{tikzpicture}[\n")
        buffer.write("    cookie/.style = {\n")
        buffer.write("        circle,\n")
        buffer.write("        thick,\n")
        buffer.write("        minimum size = 0.2cm\n")
        buffer.write("    },\n")
        buffer.write("    arrow/.style = {\n")
        buffer.write("        thick,\n")
        buffer.write("        ->\n")
        buffer.write("    }\n")
        buffer.write("]\n")

        for i in range(self.m):
            buffer.write(
                f"    \\node[cookie, draw] ({i + 1}) at ({i}, 0) {{}};\n"
            )

        file.write("\n")

        bend = "left"

        for swap in self.swaps:
            buffer.write(
                f"    \\draw[arrow] ({swap.start}) edge [bend {bend}=75] ({swap.end});\n"
            )

            bend = "right" if bend == "left" else "left"

        buffer.write("\end{tikzpicture}\n")
        buffer.write("\end{center}\n")

@dataclass
class Group:
    n: int
    m: int

    permutations: List[Permutation]

def recursive_nested_permutation_generator(n, m, arrows, out):
    if n == 0:
        for i, arrow in enumerate(arrows):
            if arrow in arrows[i + 1:]:
                return

        p = Permutation(m, arrows)
        if p.id() not in map(Permutation.id, out):
            out.append(p)
        return

    for start in range(1, m + 1):
        for end in range(start + 1, m + 1):
            # To go further beyond
            recursive_nested_permutation_generator(n - 1, m, [*arrows, Arrow(start, end)], out)

groups = []

for m in range(4, 5):
    for n in range(0, m):
        group = Group(n, m, [])

        recursive_nested_permutation_generator(n, m, [], group.permutations)

        groups.append(group)

with open("swaps.tex", "w") as file:
    file.write("\\documentclass{article}\n\n")
    file.write("\\usepackage{geometry}\n")
    file.write("\\usepackage{tikz}\n\n")
    file.write("\\usepackage{multicol}\n\n")
    file.write("\\begin{document}\n")

    for group in groups:
        file.write(f"\\( P_{{{group.n}, {group.m}}} \\):\n\n")
        file.write(f"\\begin{{multicols}}{{3}}\n\n")

        for permutation in group.permutations:
            file.write(f"\\vspace{{0.25cm}}\n\n")

            print(permutation, permutation.id())
            permutation.draw(file)
            
            file.write("\n")

        file.write(f"\\end{{multicols}}\n\n")

    file.write("\\end{document}\n")
