#include <iostream>
#define MAX 8

using namespace std;

int N, M;
int arr[MAX];

void dfs(int cnt) {
  if (cnt == M) {
    for (int i = 0; i < M; i++) {
      cout << arr[i] << " ";
    }
    cout << "\n";
    return;
  }

  for (int i = 0; i < N; i++) {
    arr[cnt] = i + 1;
    dfs(cnt + 1);
  }
}

int main() {
  cin >> N >> M;
  fill_n(arr, MAX, 0);
  dfs(0);
}
