import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] words = s.split("\\s+");
        
        if (pattern.length() != words.length) {
            return false;
        }
        
        // Map to store character-to-word relationships
        Map<Character, String> charToWord = new HashMap<>();
        
        for (int i = 0; i < pattern.length(); i++) {
            char ch = pattern.charAt(i);
            String word = words[i];
            
            // Check if the character has already been seen
            if (charToWord.containsKey(ch)) {
                // If it maps to a different word, it violates the pattern
                if (!charToWord.get(ch).equals(word)) {
                    return false;
                }
            } else {
                // Check if the word is already claimed by another character
                if (charToWord.containsValue(word)) {
                    return false;
                }
                // Otherwise, establish the mapping
                charToWord.put(ch, word);
            }
        }
        
        return true;
    }
}