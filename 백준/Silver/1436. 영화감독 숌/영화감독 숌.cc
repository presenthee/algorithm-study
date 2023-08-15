#include <iostream>
#include <string>
#define fastio cin.tie(0)->sync_with_stdio(0)
#define MAX 6670000
using namespace std;

int main() {
  int N;
  cin >> N;
  int count = N;

  for (int i = 666; i < MAX; i++) {
    if (to_string(i).find("666") != -1) {
      count--;
    }
    if (!count) {
      cout << i << '\n';
      break;
    }
  }

  return 0;
}