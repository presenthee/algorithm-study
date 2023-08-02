#include <stdio.h>
#include <algorithm>
#define arr 10000

int main() {
    int k, n, tempcnt, lens[arr];
    long long high=0;
    long long result;

    scanf("%d %d", &k, &n);
    for (int i=0; i<k; i++) {
        scanf("%d", &lens[i]);
        if (lens[i]>high)
            high=lens[i];
    }
    
    std::sort(lens, lens+k);

    long long low=1;
    long long mid;
    long long tempmax=0;

    while(high>=low) {
        mid = (high+low)/2;
        tempcnt=0;
        for (int j=0; j<k; j++) {
            tempcnt += (lens[j]/mid);
        }
        if (tempcnt>=n) {
            tempmax= std::max(tempmax, mid);
            low=mid+1;
            continue;
        }
        else
            high=mid-1;
    }

    printf("%ld", tempmax);
    return 0;
}

