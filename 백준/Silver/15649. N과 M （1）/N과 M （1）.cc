#include <iostream>
#define MAX 9

using namespace std;

int N, M;
int buf[MAX] = {0,};
int calling[MAX] = {0,};

void dfs(int cnt) {
  if (cnt == M) {
    for (int i = 1; i <= M; i++) {
      cout << buf[i] << " ";
    }
    cout << "\n";
    return;
  }

  for (int i = 1; i <= N; i++) {
    if (calling[i] == true) continue;
    calling[i] = true;
    buf[cnt + 1] = i;
    dfs(cnt + 1);
    calling[i] = false;
  }
}

int main() {
  cin >> N >> M;
  // call dfs
  dfs(0);
}