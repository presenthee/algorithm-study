#include <algorithm>
#include <iostream>

using namespace std;

// 0 ~ max까지 이분 탐색. k에 대해 한 학생당 k개 이하의 보석을 준다고 했을 때,
// 보석을 모두 나눠줄 수 있는가? 가 조건이다.
bool Check(vector<int>& gems, int mid, int N) {
  int count = 0;
  for (int gem : gems) {
    count += (gem + mid - 1) / mid;
  }
  return count <= N;
}

int main() {
  int N, M;
  scanf("%d %d", &N, &M);

  vector<int> gems(M);
  for (int i = 0; i < M; i++) scanf("%d", &gems[i]);
  sort(gems.begin(), gems.end());

  int low = 0;
  int high = gems[gems.size() - 1];

  while (low + 1 < high) {
    int mid = (low + high) / 2;
    if (Check(gems, mid, N)) {
      high = mid;
    } else {
      low = mid;
    }
  }

  printf("%d\n", high);
}