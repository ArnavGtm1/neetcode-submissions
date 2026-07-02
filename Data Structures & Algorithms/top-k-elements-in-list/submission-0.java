class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        //min-heap solution
        //1: Make a frequency map
        HashMap<Integer, Integer> store = new HashMap<>();
        for(int i = 0; i<nums.length; i++){
            if(!store.containsKey(nums[i])){
                store.put(nums[i], 1);
            }
            else{
                store.put(nums[i], store.get(nums[i])+1);
            }
        }
        //2: Make a minheap and pass in the lambda operator to compare frequency
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a,b) -> store.get(a)-store.get(b));
        for(int num : store.keySet()){
            minHeap.add(num);
            if(minHeap.size()>k){
                minHeap.poll();
            }   
        }

        //3: Extract elements
        int[] result = new int[k];
        for(int i = 0; i<k; i++){
            result[i] = minHeap.poll();
        }

        return result;

    }
}
