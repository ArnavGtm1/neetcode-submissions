class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> store = new HashMap<>();
        for(int i = 0; i<nums.length; i++){
            int diff = target-nums[i];
            if(store.containsKey(nums[i])){
                return new int[] {store.get(nums[i]), i};
            }
            store.put(diff, i);
        }
        return new int[] {0,0};
    }
}
