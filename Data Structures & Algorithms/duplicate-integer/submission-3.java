class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> store = new HashSet<>();
        for(int num : nums){
            if(!store.add(num)){
                return true;
            }
        }
        return false;
    }
}