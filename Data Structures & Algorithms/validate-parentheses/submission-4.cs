public class Solution {
    public bool IsValid(string s) {
        char[] c = s.ToCharArray();
        var stack = new Stack<char>();
        var dict = new Dictionary<char, char>
        {
            { ')', '(' },
            { ']', '[' },
            { '}', '{' }
        };
        for(int i = 0; i < c.Length; i++){
            if (c[i] is '(' or '[' or '{'){
                stack.Push(c[i]);
            }
            if(c[i] is '}' or ']' or ')'){
                if(stack.Count == 0 || stack.Pop()!=dict[c[i]]){
                    return false;
                }
            }
        }
        return stack.Count == 0;
    }
}
