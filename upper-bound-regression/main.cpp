#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <ctime>

typedef long long ll;

template<typename T>
void read_some(std::vector<T> &v, int N) {
    for (int i = 0; i < N; i++) {
        T a;
        std::cin >> a;
        v.push_back(a);
    }
}

template<typename T>
void print_some(std::vector<T> &v) {
    std::cout << "[";

    for (int i = 0; i < v.size(); i++) {
        std::cout << " " << v[i];
    }
    
    std::cout << " ]" << std::endl;
}

template <typename T>
struct Optional {
    bool has;
    T value;
};

struct Point {
    double x;
    double y;
};

struct Line {
    double m;
    double b;
};

struct Intersection {
    Point p;
    int l1;
    int l2;
};

Optional<Point> intersect(const Line &line1, const Line &line2) {
    // m1 x + b1 = m2 x + b2
    // x = (b2 - b1) / (m1 - m2)
    if (line1.m == line2.m) {
        return (Optional<Point>) {false, (Point) {0}};
    }

    double x = (line2.b - line1.b) / (line1.m - line2.m);
    double y = line1.m * x + line1.b;

    return (Optional<Point>) {true, (Point) { x, y }};
}

bool isIntersectionLefter(const Intersection &left, const Intersection &right) {
    // The equal case is a bit superfluous because if i1 and i2 share some mutual line
    // then clearly the point must be equal anyway.
    return left.p.x == right.p.x ? left.p.y > right.p.y : left.p.x < right.p.x; 
}

int main() {
    // Points should be the only input really and should be a unique list of points.
    std::vector<Point> points;

    /*
    [(2, 1), (3, 0), (4, 2), (5, 2), (6, 4), (7, 2), (8, 2), (9, 2), (10, 6), (11, 6), (12, 8), (13, 6), (14, 2), (15, 0), (16, 8), (17, 10), (18, 12), (19, 10), (20, 4), (21, 2), (22, 12), (23, 14), (24, 12), (25, 8), (26, 6), (27, 6), (28, 16), (29, 20), (30, 22), (31, 14), (32, 4), (33, 4), (34, 8), (35, 12), (36, 24), (37, 18), (38, 6), (39, 8), (40, 24), (41, 28), (42, 30), (43, 22), (44, 4), (45, 2), (46, 24), (47, 30), (48, 26), (49, 22), (50, 12), (51, 8), (52, 28), (53, 34), (54, 22), (55, 16), (56, 12), (57, 8), (58, 30), (59, 42), (60, 44), (61, 30), (62, 6), (63, 4), (64, 16), (65, 28), (66, 46), (67, 34), (68, 12), (69, 20), (70, 46), (71, 46), (72, 48), (73, 36), (74, 4), (75, 4), (76, 24), (77, 36), (78, 54), (79, 46), (80, 22), (81, 14), (82, 42), (83, 58), (84, 40), (85, 22), (86, 14), (87, 16), (88, 48), (89, 64), (90, 48), (91, 28), (92, 16), (93, 14), (94, 26), (95, 40), (96, 64), (97, 54), (98, 18), (99, 20), (100, 60), (101, 68)]
    */

    points.push_back((Point) {2, 1}); points.push_back((Point) {3, 0}); points.push_back((Point) {4, 2}); points.push_back((Point) {5, 2});
    points.push_back((Point) {6, 4}); points.push_back((Point) {7, 2}); points.push_back((Point) {8, 2}); points.push_back((Point) {9, 2});
    points.push_back((Point) {10, 6}); points.push_back((Point) {11, 6}); points.push_back((Point) {12, 8}); points.push_back((Point) {13, 6});
    points.push_back((Point) {14, 2}); points.push_back((Point) {15, 0}); points.push_back((Point) {16, 8}); points.push_back((Point) {17, 10});
    points.push_back((Point) {18, 12}); points.push_back((Point) {19, 10}); points.push_back((Point) {20, 4}); points.push_back((Point) {21, 2});
    points.push_back((Point) {22, 12}); points.push_back((Point) {23, 14}); points.push_back((Point) {24, 12}); points.push_back((Point) {25, 8});
    points.push_back((Point) {26, 6}); points.push_back((Point) {27, 6}); points.push_back((Point) {28, 16}); points.push_back((Point) {29, 20});
    points.push_back((Point) {30, 22}); points.push_back((Point) {31, 14}); points.push_back((Point) {32, 4}); points.push_back((Point) {33, 4});
    points.push_back((Point) {34, 8}); points.push_back((Point) {35, 12}); points.push_back((Point) {36, 24}); points.push_back((Point) {37, 18});
    points.push_back((Point) {38, 6}); points.push_back((Point) {39, 8}); points.push_back((Point) {40, 24}); points.push_back((Point) {41, 28});
    points.push_back((Point) {42, 30}); points.push_back((Point) {43, 22}); points.push_back((Point) {44, 4}); points.push_back((Point) {45, 2});
    points.push_back((Point) {46, 24}); points.push_back((Point) {47, 30}); points.push_back((Point) {48, 26}); points.push_back((Point) {49, 22});
    points.push_back((Point) {50, 12}); points.push_back((Point) {51, 8}); points.push_back((Point) {52, 28}); points.push_back((Point) {53, 34});
    points.push_back((Point) {54, 22}); points.push_back((Point) {55, 16}); points.push_back((Point) {56, 12}); points.push_back((Point) {57, 8});
    points.push_back((Point) {58, 30}); points.push_back((Point) {59, 42}); points.push_back((Point) {60, 44}); points.push_back((Point) {61, 30});
    points.push_back((Point) {62, 6}); points.push_back((Point) {63, 4}); points.push_back((Point) {64, 16}); points.push_back((Point) {65, 28});
    points.push_back((Point) {66, 46}); points.push_back((Point) {67, 34}); points.push_back((Point) {68, 12}); points.push_back((Point) {69, 20});
    points.push_back((Point) {70, 46}); points.push_back((Point) {71, 46}); points.push_back((Point) {72, 48}); points.push_back((Point) {73, 36});
    points.push_back((Point) {74, 4}); points.push_back((Point) {75, 4}); points.push_back((Point) {76, 24}); points.push_back((Point) {77, 36});
    points.push_back((Point) {78, 54}); points.push_back((Point) {79, 46}); points.push_back((Point) {80, 22}); points.push_back((Point) {81, 14});
    points.push_back((Point) {82, 42}); points.push_back((Point) {83, 58}); points.push_back((Point) {84, 40}); points.push_back((Point) {85, 22});
    points.push_back((Point) {86, 14}); points.push_back((Point) {87, 16}); points.push_back((Point) {88, 48}); points.push_back((Point) {89, 64});
    points.push_back((Point) {90, 48}); points.push_back((Point) {91, 28}); points.push_back((Point) {92, 16}); points.push_back((Point) {93, 14});
    points.push_back((Point) {94, 26}); points.push_back((Point) {95, 40}); points.push_back((Point) {96, 64}); points.push_back((Point) {97, 54});
    points.push_back((Point) {98, 18}); points.push_back((Point) {99, 20}); points.push_back((Point) {100, 60}); points.push_back((Point) {101, 68});

    /*
    srand(time(0));

    for (int i = 0; i < 6; i++) {
        points.push_back((Point) { rand() % 20, rand() % 20 });
    }
    */

    ll n = points.size();

    std::vector<Line> lines;

    for (const Point &point : points) {
        lines.push_back((Line) { -point.x, point.y });
    }

    // Highest lines first
    std::sort(lines.begin(), lines.end(), [](const Line &left, const Line &right) { return left.m == right.m ? left.b > right.b : left.m < right.m; });

    std::vector<std::vector<Intersection>> intersections(n);

    for (ll i = 0; i < n; i++) {
        for (ll j = i + 1; j < n; j++) {
            Optional<Point> intersectionPoint = intersect(lines[i], lines[j]);

            if (!intersectionPoint.has) { continue; }

            Intersection intersection = (Intersection) { intersectionPoint.value, i, j };
            intersections[i].push_back(intersection);

            // Interestingly I think we can just pick the first point, which is kinda cool
            // it might be useful to prove that though
            // intersections[j].push_back(intersection);
        }

        std::sort(intersections[i].begin(), intersections[i].end(), isIntersectionLefter);
    }

    /*
    for (ll i = 0; i < n; i++) {
        for (ll j = 0; j < intersections[i].size(); j++) {
            Intersection in = intersections[i][j];
            std::cout << in.l1 << " -> " << in.l2 << " (" << in.p.x << ", " << in.p.y << ")" << " ";
        }

        std::cout << std::endl;
    }
    */
    
    std::vector<Point> critical;
    int current = 0;

    while (intersections[current].size()) {
        critical.push_back(intersections[current][0].p);

        current = intersections[current][0].l2;
    }

    /*
    for (const Point &p : critical) {
        std::cout << "(" << p.x << ", " << p.y << ")" << std::endl;
    }
    */

    double cost = std::numeric_limits<double>::max();
    Point best;

    for (Point c : critical) {
        double ccost = 0;

        double beta = c.x;
        double alpha = c.y;

        for (ll i = 0; i < n; i++) {
            ccost += std::pow(beta * points[i].x + alpha - points[i].y, 2) / n;
        }

        if (ccost < cost) {
            cost = ccost;
            best = c;
        }
    }

    std::cout << "Line (beta, alpha): (" << best.x << ", " << best.y << ")" << std::endl;
    std::cout << "Cost: " << cost << std::endl;

    // I suppose the next thing to do would be to precompute the transitions for a giant set
    // and then randomly sample and average to see if there's any notion of convergence idk.

    return 0;
}
