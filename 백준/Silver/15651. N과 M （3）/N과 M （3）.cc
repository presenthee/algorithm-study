#include <iostream>

using namespace std;

int main() {
  int N, M, sequence[7];
  cin >> N >> M;

  int p = 1;
  for (int i = 0; i < M; i++) p *= N;
  for (int i = 0; i < p; i++) {
    for (int j = 0, cur = i; j < M; j++) {
      sequence[j] = cur % N + 1;
      cur /= N;
    }
    for (int j = M - 1; j >= 0; j--) cout << sequence[j] << ' ';
    cout << '\n';
  }
  return 0;
}