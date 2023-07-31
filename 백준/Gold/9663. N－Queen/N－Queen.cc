#include <iostream>
#define MAX 15

using namespace std;

int N;
int answer = 0;
int board[MAX] = {
    0,
};

bool promising(int row, int col) {
  for (int i = 0; i < row; i++) {
    if (board[i] == col || (row - i) == abs(board[i] - col)) return false;
  }
  return true;
}

void find_n_queen(int cnt) {
  if (cnt == N) {
    answer++;
    return;
  }

  for (int i = 1; i <= N; i++) {
    if (promising(cnt, i)) {
      board[cnt] = i;
      find_n_queen(cnt + 1);
    }
  }
}

int main() {
  cin >> N;
  find_n_queen(0);
  cout << answer << endl;
}
