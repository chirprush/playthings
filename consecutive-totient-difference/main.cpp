#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

typedef long long ll;

constexpr ll L = 1e5;
std::vector<ll> lpf(L + 2, std::numeric_limits<ll>::max());

ll totient(ll n) {
    ll result = n;

    while (n > 1) {
        ll p = lpf[n];

        while (lpf[n] == p) {
            n /= p;
        }

        result /= p;
        result *= p - 1;
    }
    
    return result;
}

int main() {
    std::vector<bool> sieve(L + 2, true);

    for (ll p = 2; p <= L + 1; p++) {
        if (!sieve[p]) { continue; }

        lpf[p] = p;

        for (ll j = p; j * p <= L + 1; j++) {
            sieve[j * p] = false;
            lpf[j * p] = std::min(lpf[j * p], p);
        }
    }

    /*
    std::cout << "Least Prime Factor:" << std::endl;
    for (ll i = 2; i <= L + 1; i++) {
        std::cout << i << ": " << lpf[i] << std::endl;
    }
    */

    std::vector<ll> phi(L + 2);
    phi[0] = 0;
    phi[1] = 0;

    for (ll n = 2; n <= L + 1; n++) {
        phi[n] = totient(n);
    }

    /*
    std::cout << "Totient: " << std::endl;
    for (ll i = 1; i <= L + 1; i++) {
        std::cout << i << ": " << phi[i] << std::endl;
    }
    */

    for (ll n = 2; n <= 101; n++) {
        std::cout << "(" << n << ", " << std::abs(phi[n + 1] - phi[n]) << ")" << std::endl;
    }

    return 0;

    double mean = 0;
    double sqmean = 0;

    ll minn = 0;
    ll maxn = 0;

    double mindiff = std::numeric_limits<double>::max();
    double maxdiff = std::numeric_limits<double>::min();

    // std::cout << "Totient Differences: " << std::endl;
    // We could actually get a closed form (in terms of a long string of phis) for this but it'd probably be not interesting idk
    for (ll n = 1; n <= L; n++) {
        double diff = (double) std::abs(phi[n + 1] - phi[n]) / n;

        // std::cout << n << ": " << diff << std::endl;

        if (diff > maxdiff && n > 2) {
            maxdiff = diff;
            maxn = n;
        } else if (diff < mindiff && n > 2) {
            mindiff = diff;
            minn = n;
        }

        mean += (double) diff / L;
        sqmean += ((double) diff / L) * diff;
    }

    // Var[X] = E[X^2] - E[X]^2
    double std = std::sqrt(sqmean - mean * mean);

    std::cout << "Mean: " << mean << std::endl;
    std::cout << "Standard deviation: " << std << std::endl;
    std::cout << "Min (excluding n = 2): " << mindiff << " found at n = " << minn << std::endl;
    std::cout << "Max (excluding n = 1): " << maxdiff << " found at n = " << maxn << std::endl;

    return 0;
}
