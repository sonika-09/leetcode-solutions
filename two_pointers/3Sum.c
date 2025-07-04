// 15 - 3Sum
// Runtime=51ms, Beats=100%

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
    int row = 0;
    qsort(&nums[0], numsSize, sizeof(int), compare);
    int capacity = 100;
    int **result = (int**)malloc(capacity*sizeof(int*));
    *returnColumnSizes = (int*)malloc(capacity*sizeof(int));
    for(int i=0; i<numsSize-2; i++) {
        if(i>0 && nums[i]==nums[i-1])   //to avoid duplicate results
            continue;
        int j = i+1;
        int k = numsSize-1;
        while (j < k) {
            int sum = nums[i] + nums[j] + nums[k];
            if(sum == 0) {
                if (row == capacity) {
                capacity *= 2;
                result = (int**)realloc(result, capacity * sizeof(int*));
                *returnColumnSizes = (int*)realloc(*returnColumnSizes, capacity * sizeof(int));
                }
                result[row] = (int*)malloc(3*(sizeof(int)));
                result[row][0] = nums[i];
                result[row][1] = nums[j];
                result[row][2] = nums[k];
                (*returnColumnSizes)[row] = 3; 
                row++;
                while (j < k && nums[j] == nums[j + 1]) j++;    //skips duplicate j's
                while (j < k && nums[k] == nums[k - 1]) k--;    //skips duplicate k's
                j++;
                k--;
            }
            else if(sum < 0)
                j++;
            else
                k--;
        }
    }
    *returnSize = row;
    return result;
}