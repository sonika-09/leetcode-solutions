//217 - contains duplicate
//Runtime = 41ms, Beats = 75.95%

//this function returns the relation between numbers a and b
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

bool containsDuplicate(int* nums, int numsSize) {
    //we sort the array using quick sort
    qsort(nums, numsSize, sizeof(nums[0]), compare);
    for(int i=0; i<numsSize-1; i++) {
        //check the adjacent array elements to find any duplicates
        if(nums[i] == nums[i+1])
            return true;
    }
    return false;
}

