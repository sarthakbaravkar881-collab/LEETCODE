import java.util.*;

class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            // Push opening brackets onto the stack
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            } 
            // Handle closing brackets
            else {
                // If stack is empty but we have a closing bracket, it's invalid
                if (stack.isEmpty()) {
                    return false;
                }
                
                char top = stack.pop(); // Remove and check the top element
                
                // If the popped bracket doesn't match the closing bracket, it's invalid
                if ((c == ')' && top != '(') || 
                    (c == ']' && top != '[') || 
                    (c == '}' && top != '{')) {
                    return false;
                }
            }
        }
        
        // If the stack is empty at the end, all brackets were matched properly
        return stack.isEmpty();
    }
}