class Solution {
    public int maxArea(int[] height) {
        int maxwater = 0;
        int l = 0;
        int r = height.length-1;
        while(l<r){
            int w = r - l;
            int h = Math.min(height[l], height[r]);
            int water = h*w;
            maxwater = Math.max(maxwater, water);
            if(height[l]<height[r]){
                l++;
            }else{
                r--;
            }
        }
        return maxwater;
    }
}