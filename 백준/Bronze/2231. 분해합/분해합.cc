#include <iostream>
#define fastio cin.tie(0)->sync_with_stdio(0)
using namespace std;

int main() {
  int N;
  cin >> N;

  for (int i = 1; i < N; i++) {
    int sum = 0;
    int cur = i;
    while (cur > 0) {
      sum += cur % 10;
      cur /= 10;
    }

    if (sum + i == N) {
      cout << i << endl;
      return 0;
    }
  }

  cout << 0 << endl;
  return 0;
}
