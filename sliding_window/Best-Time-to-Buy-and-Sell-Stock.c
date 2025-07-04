//121 - Best Time to Buy and Sell Stock
//Runtime = 1ms, Beats = 38.83%
int maxProfit(int* prices, int pricesSize) {
    int min=prices[0], profit, max_profit=0;
    for(int i=0; i<pricesSize; i++) {
        if(prices[i] < min)    //we check for the minimum element up till this point
            min = prices[i];
        profit = prices[i] - min;
        if(profit > max_profit) {
            max_profit = profit;
        }
    }
    return max_profit;
}

//Had multiple tries before my solution was accepted, so here are all the rejected ones
//solution 2 - TLE!
int maxProfit(int* prices, int pricesSize) {
    int i=0, j, max_profit=0, profit;
    while(i < pricesSize-1) {
        j = i + 1;
        while(j < pricesSize) {
            if(prices[i]<prices[j]) {
                profit = prices[j] - prices[i];
                if(profit > max_profit) {
                    max_profit = profit;
                }
            }
            j++;
        }
        i++;
    }
    return max_profit;
}

//solution 3 - TLE!
#include <string.h>
int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}
int maxProfit(int* prices, int pricesSize) {
    int i=0, j, temp[pricesSize], profit, max_profit=0;
    while(i < pricesSize-1) {
        memcpy(temp, prices, pricesSize * sizeof(int));
        j = i+1;
        qsort(&temp[j], pricesSize-j, sizeof(int), compare);
        profit = temp[pricesSize-1] - prices[i];
        if(profit > max_profit) {
            max_profit = profit;
        }
        i++;
    }
    return max_profit;
}

//solution 4 - TLE!
#include <string.h>
int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}
int maxProfit(int* prices, int pricesSize) {
    int i=0, j, *temp, len, profit, max_profit=0;
    while(i < pricesSize-1) {
        j = i+1;
        len = pricesSize - j;
        temp = (int*)malloc(len * sizeof(int));
        memcpy(temp, &prices[j], len * sizeof(int));
        qsort(&temp[0], len, sizeof(int), compare);
        profit = temp[len-1] - prices[i];
        if(profit > max_profit) {
            max_profit = profit;
        }
        i++;
    }
    return max_profit;
}
