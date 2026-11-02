import java.util.*;
class Solution {
    public int titleToNumber(String columnTitle) {
       Map<Character, Integer> mapping = new HashMap<>();
        char letter = 'A';
        for (int i = 1; i <= 26; i++) {
            mapping.put(letter, i);
            letter++;
        }
        int res=0;
        for (char ch:columnTitle.toCharArray() ){
            res=res*26+mapping.get(ch);
        }
        return res;
    }
}