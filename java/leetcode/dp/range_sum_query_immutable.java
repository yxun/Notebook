/**
 * 303. Range Sum Query - Immutable
 * Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:

You may assume that the array does not change.
There are many calls to sumRange function.
 */

public class range_sum_query_immutable {

    // sum[j+1] - sum[i], sum[i] is sum of index 0 to i-1

    private int [] sums;

    public NumArray(int[] nums) {
        sums = new int[nums.length+1];
        for (int i = 1; i <= nums.length; i++) {
            sums[i] = sums[i-1] + nums[i-1];
        }
    }

    public int sumRange(int i, int j) {
        return sums[j+1] - sums[i];
    }
}