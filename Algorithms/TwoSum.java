import java.util.Hashtable;

public class TwoSum {
    /*
    https://leetcode.com/problems/two-sum/description/
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

[-1,-2,-3,-4,-5]
-8

Only one solution
 */
public static int[] bruteForceTwoSum(int[] nums, int target) {
    for (int i = 0; i < nums.length; i++) {
        if (nums[i] <= target || target < 0){
            for (int j = 0; j < nums.length; j++) {
                if (nums[i] + nums[j] == target && i != j){
                    return new int[] {i, j};
                }
                
            }
        }
    }
    return new int[] {0, 0};
}

public static int[] hashTableTwoSum(int[] nums, int target) {
    Hashtable<Integer, Integer> hashtable = new Hashtable<>();
    for (int i = 0; i < nums.length; i++) {
        int left = target - nums[i];
        if (hashtable.get(left) != null){
            return new int[]{hashtable.get(left), i};
        }
        hashtable.put(nums[i], i);
        
    }
    return new int[]{};
}
public static void main(String[] args) {
    // int[] nums = {2,7,11,15};
    int[] nums = {3,2,4};
    // int[] nums = {-1,-2,-3,-4,-5};
    int target = 6;
    // int[] result = bruteForceTwoSum(nums, target);
    int[] result = hashTableTwoSum(nums, target);
    for (int i : result) {
        System.out.println(i);
    }
}
}

