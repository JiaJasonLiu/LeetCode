public class P01 {

    // Example 1:
    // Input: nums = [2,7,11,15], target = 9
    // Output: [0,1]
    // Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    // Example 2:

    // Input: nums = [3,2,4], target = 6
    // Output: [1,2]
    // Example 3:

    // Input: nums = [3,3], target = 6
    // Output: [0,1]

    public static void main(String[] args) throws Exception {
        int[] arr = { 3, 2, 4 };
        int target = 6;
        int[] output = new int[2];
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (arr[i] + arr[j] == target && i != j) {
                    output[0] = j;
                    output[1] = i;
                }
            }
        }
        for (int i : output) {
            System.out.println(i);
        }

    }
}
