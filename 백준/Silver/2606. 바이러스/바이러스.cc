#include <stdio.h>
#include <vector>

#define max 101

using namespace std;
int result =0;

void dfs(int start, vector<int> *links, bool *visited) {
    visited[start] = true;
    result++;
    for(int l=0; l< links[start].size(); l++) {
        int temp= links[start][l];
        if(!visited[temp]) {
            dfs(temp, links, visited);
        }
    }
}

int main() {
    int num, link; 
    int temp_start, temp_end;
    scanf("%d %d", &num, &link);
    vector<int> links[max];

    for(int i=0; i<link; i++) {
        scanf("%d %d", &temp_start, &temp_end);
        links[temp_start].push_back(temp_end);
        links[temp_end].push_back(temp_start);
    }

    bool visited[max] = {0};
    dfs(1, links, visited);

    printf("%d\n", result-1);

    return 0;

}