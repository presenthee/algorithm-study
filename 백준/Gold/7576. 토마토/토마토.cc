#include <algorithm>
#include <iostream>
#include <queue>

using namespace std;

vector<vector<int>> graph;
queue<pair<int, int>> visit_queue;
int dx[] = {0, 0, -1, 1};
int dy[] = {-1, 1, 0, 0};
int result = 0;
int ideal_result;
int visited_node = 0;

void bfs(int m, int n) {
  while (!visit_queue.empty()) {
    int x = visit_queue.front().first;
    int y = visit_queue.front().second;
    visit_queue.pop();
    visited_node++;

    for (int i = 0; i < 4; i++) {
      int nx = x + dx[i];
      int ny = y + dy[i];
      if (nx >= 0 && ny >= 0 && nx < n && ny < m) {
        if (graph[nx][ny] == 0) {
          int dist = graph[x][y] + 1;
          graph[nx][ny] = dist;
          result = max(result, dist);
          visit_queue.push(make_pair(nx, ny));
        }
      }
    }
  }
}

int main() {
  int m, n;
  cin >> m >> n;
  ideal_result = m * n;

  graph.assign(n, vector<int>(m, 0));
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      cin >> graph[i][j];
      if (graph[i][j] == 1) visit_queue.push(make_pair(i, j));
      if (graph[i][j] == -1) ideal_result--;
    }
  }

  bfs(m, n);

  if (visited_node != ideal_result) {
    cout << -1 << endl;
    return 0;
  }

  if (result == 0) {
    cout << 0 << endl;
    return 0;
  }

  cout << result - 1 << endl;
  return 0;
}