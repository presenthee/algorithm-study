#include <algorithm>
#include <iostream>
#include <queue>

#define MAX 25

using namespace std;

int N;
string graph[MAX];
bool visited[MAX][MAX];
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};
queue<pair<int, int>> visit_queue;

int bfs(int start_x, int start_y) {
  int cnt = 0;
  visit_queue.push(make_pair(start_x, start_y));
  visited[start_x][start_y] = true;

  while (!visit_queue.empty()) {
    int x = visit_queue.front().first;
    int y = visit_queue.front().second;
    visit_queue.pop();
    cnt++;

    for (int i = 0; i < 4; i++) {
      int nx = x + dx[i];
      int ny = y + dy[i];

      if (nx >= 0 && ny >= 0 && nx < N && ny < N) {
        if (graph[nx][ny] == '1' && !visited[nx][ny]) {
          visit_queue.push(make_pair(nx, ny));
          visited[nx][ny] = true;
        }
      }
    }
  }

  return cnt;
}

int main() {
  int result_num = 0;
  vector<int> result;

  cin >> N;

  for (int i = 0; i < N; i++) {
    cin >> graph[i];
  }

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      if (graph[i][j] == '1' && !visited[i][j]) {
        result.push_back(bfs(i, j));
        result_num++;
      }
    }
  }

  cout << result_num << "\n";

  sort(result.begin(), result.end());
  for (int i = 0; i < result.size(); i++) {
    cout << result[i] << "\n";
  }
}