class Solution {
public:
    bool isValid(string s) {
        stack<char> stack;
        for(auto ch:s){
            if (ch=='(' or ch=='[' or ch=='{') stack.push(ch);
            else{
                if (stack.empty() or (stack.top()=='(' and ch!=')') or (stack.top()=='[' and ch!=']') or (stack.top()=='{' and ch!='}')) return false;
                stack.pop();
            }
        }
        return stack.empty();
        
    }
};