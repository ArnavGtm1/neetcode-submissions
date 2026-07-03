class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        //Bucket sort implementation
        //1: Make a frequency map using hashmap
         HashMap<Integer, Integer> store = new HashMap<>();
        for(int i = 0; i<nums.length; i++){
            if(!store.containsKey(nums[i])){
                store.put(nums[i], 1);
            }
            else{
                store.put(nums[i], store.get(nums[i])+1);
            }
        }

    //2: Create the bucket and add numbers to bucket where their bucket index is frequency
        List[] buckets = new List[nums.length+1];
        for(int num : store.keySet()){
            int frequency = store.get(num);
            if(buckets[frequency] == null){
                buckets[frequency] = new ArrayList<>();
            }
            buckets[frequency].add(num);
        }

    //3: Return the top k elements
        List<Integer> result = new ArrayList<>();
        for(int i = buckets.length-1; i>=0 && result.size()<k; i--){
            if(buckets[i]!=null){
                result.addAll(buckets[i]);
            }
        }
        return result.stream().mapToInt(i -> i).toArray();
    }
}
