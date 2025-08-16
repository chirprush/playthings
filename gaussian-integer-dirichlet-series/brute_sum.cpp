#include <iostream>
#include <complex>
#include <iomanip>

typedef long long ll;

int main() {
    constexpr ll N = 15000;
    std::complex<double> sum(0, 0);

    for (ll x = 1; x <= N; x++) {
        for (ll y = 0; y <= N; y++) {
            std::complex<double> z(x, y);
            std::complex<double> invz = (std::complex<double>) 1 / z;
            sum += invz * invz * invz * invz;
        }
    }

    std::cout << std::setprecision(15) << (std::complex<double>) 4 * sum << std::endl;

    return 0;
}
