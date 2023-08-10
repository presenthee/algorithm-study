#include <iostream>

using namespace std;

using ull = unsigned long long;

int main() {
  // N의 범위가 < 2^63이므로 int는 불가능
  // int - ~ 2^31 -1
  // long long - ~ 2^63 - 1
  ull N;
  scanf("%llu", &N);

  ull low = 0;
  ull high = (1ULL << 32) - 1;

  if (N == 0) {
    printf("%d\n", 0);
    return 0;
  }

  while (low + 1 < high) {
    ull mid = (low + high) / 2;
    if (mid * mid < N) {
      low = mid;
    } else {
      high = mid;
    }
  }

  printf("%llu\n", high);
  return 0;
}