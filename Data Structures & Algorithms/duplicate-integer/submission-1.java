class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Create a hash set to store numbers
        Set<Integer> seen = new HashSet<>();

        // for each number in the array, see if the set contains the number
        for (int num : nums) {
            if (seen.contains(num)) {
                // If so, then its a duplicate!
                return true;
            }
            // Otherwise just add the number in the set
            seen.add(num);
        }
        // Once for loop ends, there is no duplicate so return false
        return false;
    }
}
