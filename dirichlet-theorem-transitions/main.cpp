#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

typedef long long ll;

int main() {
    constexpr ll N = 1e7;
    constexpr ll M = 4;

    ll total = 0;

    std::vector<bool> prime(N + 1, true);
    std::map<ll, ll> residues;
    std::map<ll, ll> gaps;
    std::map<std::pair<ll, ll>, ll> transitions;

    ll last = -1;

    for (ll p = 2; p <= N; p++) {
        if (!prime[p]) { continue; }

        residues[p % M]++;
        total++;

        if (last != -1) {
            transitions[std::make_pair(last, p % M)]++;
        }
        
        gaps[(p - last + M) % M]++;

        last = p % M;

        for (ll j = 2; j * p <= N; j++) {
            prime[j * p] = false;
        }
    }
    
    // Much of the work surrounding prime gaps seems to be regarding their size
    // as opposed to other number theoretic properties, which is interesting.
    // I'd like to try and calculate the theoretical distribution of these perchance.

    for (auto it = residues.begin(); it != residues.end(); it++) {
        std::cout << "p(n) = " << M << "k + " << it->first << ": " << it->second << " (" << ((double) it->second / total)  << ")" << std::endl;
    }

    std::cout << std::endl;

    for (auto it = gaps.begin(); it != gaps.end(); it++) {
        std::cout << "p(n+1) - p(n) = " << M << "k + " << it->first << ": " << it->second << " (" << ((double) it->second / (total - 1))  << ")" << std::endl;
    }

    std::cout << std::endl;

    for (auto it = transitions.begin(); it != transitions.end(); it++) {
        std::cout << M << "k + " << it->first.first << " -> " << M << "k + " << it->first.second << ": " << it->second << " (" << ((double) it->second / total)  << ")" << std::endl;
    }

    return 0;
}
