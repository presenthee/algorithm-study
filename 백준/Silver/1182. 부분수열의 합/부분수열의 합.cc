#include <iostream>
#include <vector>
#define fastio cin.tie(0)->sync_with_stdio(0)
using namespace std;

int main() {
  fastio;
  int N, S;
  cin >> N >> S;

  int answer = 0;
  vector<int> numbers(N);
  for (int i = 0; i < N; i++) cin >> numbers[i];

  for (int i = 1; i < (1 << N); i++) {
    int count = 0;
    for (int j = 0; j < N; j++) {
      if ((i >> j) & 1) count += numbers[j];
    }
    if (count == S) answer++;
  }

  cout << answer << "\n";
}