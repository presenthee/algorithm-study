#include <algorithm>
#include <iostream>

using namespace std;

int LowerBound(vector<int>& cards, int target) {}

int UpperBound(vector<int>& cards, int target) {}

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
    int num_target = upper_bound(cards.begin(), cards.end(), target) -
                     lower_bound(cards.begin(), cards.end(), target);
    printf("%d ", num_target);
  }

  printf("\n");
  return 0;
}