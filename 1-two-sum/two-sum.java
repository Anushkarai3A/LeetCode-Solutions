class Solution {
    public int[] twoSum(int[] nums, int target){
       HashMap <Integer, Integer> h = new HashMap<>();
       for(int i = 0; i<nums.length; i++){
        int x = target - nums[i];
        if(h.containsKey(x)){
            return new int[]{h.get(x), i};
        }
        h.put(nums[i], i);
       } 
       return new int[]{};
    }
}