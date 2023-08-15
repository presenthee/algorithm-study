#include <algorithm>
#include <iostream>
#define fastio cin.tie(0)->sync_with_stdio(0)
using namespace std;

int main() {
  fastio;
  int h[9];
  int sum = 0;
  for (int i = 0; i < 9; i++) {
    cin >> h[i];
    sum += h[i];
  }
  sort(h, h + 9);

  for (int i = 0; i < 9; i++) {
    for (int j = i + 1; j < 9; j++) {
      int height = sum - h[i] - h[j];
      if (height != 100) continue;
      for (int k = 0; k < 9; k++) {
        if (k != i && k != j) cout << h[k] << "\n";
      }
      return 0;
    }
  }
  return 0;
}