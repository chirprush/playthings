#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

typedef long long ll;

ll powmod(ll a, ll b, ll m){
    ll ans = 1;
    while (b) {
        if (b % 2 == 1) { ans = (ans * a) % m; }
        b /= 2;
        a = (a * a) % m;
    }
    return ans;
}

int main() {
    constexpr ll N = 1e8;
    ll total = 2;

    std::set<ll> show = {};
    ll value = 10;

    while (value <= N) {
        show.insert(value);
        value *= 10;
    }

    for (ll n = 3; n <= N; n++) {
        if (powmod(2, n - 1, n) == 1) {
            total += n;
        }

        if (show.find(n) != show.end()) {
            std::cout << n << " " << total << std::endl;
        }
    }

    return 0;
}

// Of course, this loses to the following crazy O(n^{2/3} log n) algorithm
// https://mathoverflow.net/questions/81443/fastest-algorithm-to-compute-the-sum-of-primes
// in both speed and precision.

// Results:
// log10(N) Estimate         Actual           Percent Error
// 1        17               17               0.00%
// 2        1060             1060             0.00%
// 3        77674            76127            2.03%
// 4        5820566          5736396          1.47%
// 5        457066791        454396537        0.59%
// 6        37631769100      37550402023      0.22%
// 7        3205708900056    3203324994356    0.07%
// 8        279272802315269  279209790387276  0.02%

// Due to the low density of pseudoprimes, this actually works quite well! I assume the
// percent error will drop as N increases as well.
// 
// One saving grace to this is that although the sum of primes may very well
// have structure, other functions of many primes may not. In this case,
// allowing for psuedoprimes in exchange for a far greater speed up is actually
// not an entirely terrible idea.

// This is just rambling on my part, though.
