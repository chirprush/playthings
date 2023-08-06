import graph;

settings.outformat = "svg";
unitsize(1.5cm);
defaultpen(fontsize(6pt));

real w = 7;
real h = 5;
pen funccolor = RGB(129, 161, 193);
pen areacolor = /* RGB(167, 189, 212) */ funccolor + opacity(0.3);

draw((-0.1, 0) -- (w, 0), arrow=Arrow(TeXHead), L=Label("\( x \)", position=EndPoint, align=2N + 2.5W), p=linewidth(0.4pt));
draw((0, -0.1) -- (0, h), arrow=Arrow(TeXHead), L=Label("\( y \)", position=EndPoint, align=2E + 2.5S), p=linewidth(0.4pt));

void xtick_at(real x, string l) {
    real h = 0.05;
    draw((x, h) -- (x, -h), L=Label(l, position=EndPoint, align=S), p=linewidth(0.4pt));
}

void ytick_at(real y, string l) {
    real h = 0.05;
    draw((-h, y) -- (h, y), L=Label(l, position=BeginPoint, align=W), p=linewidth(0.4pt));
}

real f(real x) {
    return x^2 / w^2 * h * 0.9;
}

defaultpen(fontsize(8pt));

real lower = 0;
real upper = w - 1;
int n = 100;

real dx = (upper - lower) / n;

for (int i = 0; i < n; ++i) {
    real x = i * dx;
    real y = f((i + 1) * dx);

    path rect = (i * dx, 0) --
        (x, y) --
        (x + dx, y) --
        (x + dx, 0);
    draw(rect, p=funccolor);
    fill(rect -- cycle, p=areacolor);
}

draw(graph(f, 0, w * 0.99), arrow=Arrow(TeXHead), p=linewidth(0.55pt));
