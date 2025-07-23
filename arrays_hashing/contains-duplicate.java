// 217 - Contains Duplicate
// Runtime = 13ms, Beats = 88.83%

import java.util.HashSet;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> table = new HashSet<>();
        for(int num : nums) {
            if(table.contains(num))	// to check if the number already exists
                return true;
            table.add(num);	// else, we add it
        }
        return false;
    }
}