class Solution {
    public boolean isAnagram(String s, String t) {
        //Sorting: Nope. Too much time complex
        //count each character for each string and match: Nope, too much memory
        HashMap<Character, Integer> freqS = new HashMap<>();
        HashMap<Character, Integer> freqT = new HashMap<>();

        for(int i = 0; i<s.length(); i++){
            char j = s.charAt(i);
            if(freqS.containsKey(j)){
                int currentCount = freqS.get(j);
                freqS.put(j, currentCount+1);
            }
            else{
                freqS.put(j,1);
            }
        }

        for(int i = 0; i<t.length(); i++){
            char j = t.charAt(i);
            if(freqT.containsKey(j)){
                int currentCount = freqT.get(j);
                freqT.put(j, currentCount+1);
            }
            else{
                freqT.put(j,1);
            }
        }

        return freqS.equals(freqT);

    }
}
