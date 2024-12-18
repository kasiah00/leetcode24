class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string>ans(n);
        int i=1;
        while(i<=n){
            if(i%15==0)
                ans[i-1]="FizzBuzz";
            else if(i%3==0)
               ans[i-1]="Fizz";
            else if(i%5==0)
              ans[i-1]="Buzz";
            else
            {
              string s=to_string(i);
              ans[i-1]=s;
            }
            i+=1;
        }
        return ans;
    }
};