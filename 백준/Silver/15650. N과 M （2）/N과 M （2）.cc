#include <iostream>
#define MAX 9

using namespace std;

int N, M;
int seq[MAX];
bool calling[MAX];

void dfs(int cnt) {
  if (cnt == M) {
    for (int i = 0; i < M; i++) {
      cout << seq[i] + 1 << " ";
    }
    cout << "\n";
  }

  int start = cnt == 0 ? 0 : seq[cnt - 1];

  for (int i = start; i < N; i++) {
    if (calling[i] == true) continue;
    calling[i] = true;
    seq[cnt] = i;
    dfs(cnt + 1);
    calling[i] = false;
  }
}
int main() {
  cin >> N >> M;
  fill_n(seq, MAX, 0);
  fill_n(calling, MAX, false);
  dfs(0);
}