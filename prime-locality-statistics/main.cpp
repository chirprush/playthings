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
    std::vector<bool> prime(N + 1, true);
    // std::vector<ll> spf(N + 1);
    std::vector<ll> bpf(N + 1);
    bpf[1] = 1;

    std::vector<ll> primes;

    for (ll p = 2; p <= N; p++) {
        if (!prime[p]) { continue; }

        primes.push_back(p);

        // spf[p] = p;
        bpf[p] = p;

        for (ll j = 2; j * p <= N; j++) {
            prime[j * p] = false;

            // if (spf[j * p] == 0) { spf[j * p] = p; }
            if (bpf[j * p] == 0) { bpf[j * p] = p; }

            // spf[j * p] = std::min(spf[j * p], p);
            bpf[j * p] = std::max(bpf[j * p], p);
        }
    }

    ll total = 0;
    ll left = 0;
    ll middle = 0;
    ll right = 0;

    for (auto it = primes.begin(); it != primes.end(); it++) {
        ll p = *it;
        total++;

        left += bpf[p - 1] > bpf[p + 1];
        middle += bpf[p - 1] == bpf[p + 1];
        right += bpf[p - 1] < bpf[p + 1];
    }
    
    std::cout << "Left: " << (double) left / total << std::endl;
    std::cout << "Middle: " << (double) middle / total << std::endl;
    std::cout << "Right: " << (double) right / total << std::endl;

    return 0;
}
