#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

typedef long long ll;

int main() {
    constexpr ll N = 1e8;
    std::vector<ll> d(N + 1, 1);

    for (ll k = 2; k <= N; k++) {
        for (ll j = 1; j * k <= N; j++) {
            d[j * k]++;
        }
    }

    ll total = 0;
    ll left = 0;
    ll middle = 0;
    ll right = 0;

    for (ll n = 2; n < N; n++) {
        if (d[n] == 2) {
            total++;
            right += d[n + 1] > d[n - 1];
            middle += d[n + 1] == d[n - 1];
            left += d[n + 1] < d[n - 1];
        }
    }

    std::cout << "Left: " << (double) left / total << std::endl;
    std::cout << "Middle: " << (double) middle / total << std::endl;
    std::cout << "Right: " << (double) right / total << std::endl;

    // Output:
    // Left: 0.473382
    // Middle: 0.0531371
    // Right: 0.473481

    return 0;
}
