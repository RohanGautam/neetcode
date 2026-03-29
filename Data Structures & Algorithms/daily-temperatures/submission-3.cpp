class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temps) {
        vector<int> result(temps.size(), 0);
        // strictly decreasing stack -> what we maintain 
        // in C++, a stl stack pop does not return the popped value, use top for that 
        stack<int> s;
        for (int i=0;i<temps.size();i++){
            // make sure the current element isnt larget than anything 
            while (s.size()>0 && temps[s.top()]<temps[i]){
                int top = s.top();
                result[top]=i-top;
                s.pop();
            }
            // now adding the current value maintains the strictly decreasing order
            s.push(i);
        }
        return result;
    }
};
