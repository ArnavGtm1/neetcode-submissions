class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //1: hashmap of hashmaps
        //where each string that we iterate to will have its own freqency table (hashmap)
        //and will be compared if another similar frequency table exits. If it does, then it's part of that group.
        //so the data structure would be hashmap where key is a hashmap and value is a list of the strings (group)..
        HashMap<String, ArrayList<String>> store = new HashMap<>();
        for(String s : strs){
            int[] count = new int[26];
            for(int i = 0; i<s.length(); i++){
                char currentChar = s.charAt(i);
                int index = currentChar-'a';
                count[index]++;
            }
            String key = Arrays.toString(count);
            if(!store.containsKey(key)){
                store.put(key, new ArrayList<>());
            }
            store.get(key).add(s);
        }
        return new ArrayList<>(store.values());
    }
}
