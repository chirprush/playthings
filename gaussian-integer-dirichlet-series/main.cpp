#include <iostream>
#include <vector>
#include <complex>
#include <iomanip>
#include <cmath>

typedef long long ll;

int main() {
    constexpr ll N = 1e6;
    std::vector<bool> prime(N + 1, true);
    std::vector<std::complex<double>> gprimes;

    for (ll p = 2; p <= N; p++) {
        if (!prime[p]) { continue; };

        if (p % 4 == 3) {
            gprimes.push_back(p);
        }

        for (ll j = 2; j * p <= N; j++) {
            prime[j * p] = false;
        }
    }

    for (ll i = 1; i * i <= N; i++) {
        for (ll j = i; i * i + j * j <= N; j++) {
            ll p = i * i + j * j;
            if (p == 2) {
                std::complex<double> z(1, 1);
                gprimes.push_back(z);
            } else if (prime[p]) {
                std::complex<double> z1(i, j);
                std::complex<double> z2(i, -j);
                gprimes.push_back(z1);
                gprimes.push_back(z2);
            }
        }
    }

    std::complex<double> prod(1, 0);

    for (std::complex<double> p : gprimes) {
        // std::cout << p << std::endl;

        std::complex<double> pinv = (std::complex<double>) 1 / p;
        double modulus = std::sqrt(std::norm(pinv));
        prod *= (std::complex<double>) 1 / ((std::complex<double>) 1 - modulus * modulus);
    }

    std::cout << std::setprecision(15) << (std::complex<double>) 4 * prod << std::endl;

    // Does this diverge?
    // It does! Zeta(2) diverges for the Gaussian integers!

    return 0;
}
