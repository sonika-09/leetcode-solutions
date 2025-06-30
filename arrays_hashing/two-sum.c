//1 - Two Sum
//Runtime = 100ms, Beats = 58.34%

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int ele;
    int *j;
    int *output = (int*) malloc (sizeof(int)*2);
    for(int i=0; i<numsSize; i++) {
        ele = target - nums[i];
        j = bsearch(&ele, &nums[0], numsSize, sizeof(int), compare);
        if (j) {
            output[0] = i;
            output[1] = *j;
            *returnSize = 2;
            return output;
        }
    }
    *returnSize = 0;
    return NULL;
}