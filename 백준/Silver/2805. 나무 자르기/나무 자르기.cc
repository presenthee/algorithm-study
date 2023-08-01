#include <algorithm>
#include <iostream>

using namespace std;

bool is_possible(int *tree, int N, int M, int height) {
  long long sum = 0;
  for (int i = 0; i < N; i++) {
    if (tree[i] > height) {
      sum += tree[i] - height;
    }
  }
  return sum >= M;
}

int main() {
  int N, M;
  cin >> N >> M;

  int *tree = new int[N];

  for (int i = 0; i < N; i++) {
    cin >> tree[i];
  }
  sort(tree, tree + N);

  int low = 0;
  int high = tree[N - 1];

  while (low + 1 < high) {
    int mid = (low + high) / 2;
    if (is_possible(tree, N, M, mid)) {
      low = mid;
    } else {
      high = mid;
    }
  }

  cout << low << endl;
}