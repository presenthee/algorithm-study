#include <algorithm>
#include <iostream>

using namespace std;

int LowerBound(vector<int>& cards, int target) {
  int low = 0;
  int high = cards.size() - 1;

  if (cards[high] < target) {
    return high + 1;
  } else if (cards[low] >= target) {
    return 0;
  }

  while (low + 1 < high) {
    int mid = (low + high) / 2;
    if (cards[mid] >= target) {
      high = mid;
    } else {
      low = mid;
    }
  }
  return high;
}

int UpperBound(vector<int>& cards, int target) {
  int low = 0;
  int high = cards.size() - 1;

  if (cards[high] <= target) {
    return high + 1;
  } else if (cards[low] > target) {
    return 0;
  }

  while (low + 1 < high) {
    int mid = (low + high) / 2;
    if (cards[mid] > target) {
      high = mid;
    } else {
      low = mid;
    }
  }

  return high;
}

int main() {
  int N, M;
  scanf("%d", &N);
  vector<int> cards(N);

  for (int i = 0; i < N; i++) scanf("%d", &cards[i]);
  sort(cards.begin(), cards.end());
  scanf("%d", &M);

  for (int i = 0; i < M; i++) {
    int target;
    scanf("%d", &target);
    int num_target = UpperBound(cards, target) - LowerBound(cards, target);
    printf("%d ", num_target);
  }

  printf("\n");
  return 0;
}