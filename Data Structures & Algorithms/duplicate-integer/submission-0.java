class Solution {
    public boolean hasDuplicate(int[] nums) {
        Hashtable<Integer, Integer> store = new Hashtable<>();
        boolean flag = false;
        for(int i = 0; i<nums.length; i++){
            if(store.containsKey(nums[i])){
                flag = true;
            }
            else{
                store.put(nums[i], 1);
            }
        }
        return flag;
    }
}