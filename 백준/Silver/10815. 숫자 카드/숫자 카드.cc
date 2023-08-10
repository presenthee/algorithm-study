#include <algorithm>
#include <iostream>

using namespace std;

int BinarySearch(const vector<int>& cards, const int target) {
  int low = 0;
  int high = cards.size() - 1;

  while (low + 1 < high) {
    int mid = (low + high) / 2;
    if (cards[mid] == target)
      return 1;
    else if (cards[mid] < target) {
      low = mid;
    } else {
      high = mid;
    }
  }
  return cards[low] == target || cards[high] == target ? 1 : 0;
}

int main() {
  int N, M;
  scanf("%d", &N);
  vector<int> cards(N);

  for (int i = 0; i < N; i++) scanf("%d", &cards[i]);
  sort(cards.begin(), cards.end());

  scanf("%d", &M);
  for (int i = 0; i < M; i++) {
    int test_int;
    scanf("%d", &test_int);
    printf("%d ", BinarySearch(cards, test_int));
  }

  printf("\n");

  return 0;
}