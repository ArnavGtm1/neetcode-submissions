class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> store = new HashSet<>();
        boolean flag = false;
        for(int i = 0; i<nums.length; i++){
            if(!store.add(nums[i])){
                return true;
            }
        }
        return flag;
    }
}