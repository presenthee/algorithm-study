#include <algorithm>
#include <iostream>
#define fastio cin.tie(0)->sync_with_stdio(0)
#define MAX 65
using namespace std;

int N, M;
int answer = MAX;
string board[50];

int Solve() {
  for (int i = 0; i <= N - 8; i++)
    for (int j = 0; j <= M - 8; j++) {
      int cnt = 0;
      // calculate when the upperleft square is black.
      for (int x = i; x < i + 8; x++)
        for (int y = j; y < j + 8; y++) {
          int parity = (x + y) & 1;
          if (parity ^ (board[x][y] == 'W')) cnt++;
        }
      int min_count = min(cnt, 64 - cnt);
      answer = min(answer, min_count);
    }
  return answer;
}

int main() {
  cin >> N >> M;
  for (int i = 0; i < N; i++) cin >> board[i];

  cout << Solve() << endl;
}