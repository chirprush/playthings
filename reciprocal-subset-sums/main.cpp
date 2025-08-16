#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

typedef long long ll;

int main() {
    constexpr ll N = 32;

    std::vector<double> dist; 
    dist.push_back(0);
    
    for (ll n = 1; n <= N; n++) {
        ll s = dist.size();

        for (ll i = 0; i < s; i++) {
            double value = dist[i] + (double) 1 / n;

            if (value < 1) {
                dist.push_back(value);
            }
        }

        std::cout << "P(X_" << n << " < 1) = " << (double) dist.size() / std::pow(2.0, n) << std::endl;
    }

    return 0;
}

// Indeed, one can easily prove (recursively) that the probability is
// non-increasing with respect to n.
