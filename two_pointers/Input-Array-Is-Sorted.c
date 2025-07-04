// 167 - Two Sum II - Input Array Is Sorted
// Runtime=0ms, Beats=100%
int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int i=0, j=numbersSize-1;
    int *result = (int*)calloc(2, sizeof(int));
    while(j > i) {
        int sum = numbers[i] + numbers[j];
        if(sum == target) {
            result[0] = i+1;
            result[1] = j+1;
            *returnSize = 2;
            return result;
        }
        else if (sum < target) {
            i++;
        }
        else {
            j--;
        }
    }
    result[0] = 0;
    result[1] = 0;
    *returnSize = 2;
    return result;
}