/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* runningSum(int* nums, int numsSize, int* returnSize){
    int *sum = (int*)malloc((sizeof(int))*numsSize);
    *sum = (*nums);
    for (int i=1;i<numsSize;i++){
        *(sum+i) = *(nums+i) + *(sum + i -1);
    }
    *returnSize = numsSize;
    return (sum);
}

