#include <iostream>
#include <vector>
using namespace std;

//字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。
//
//示例1:
//
//输入：s1 = "waterbottle", s2 = "erbottlewat"
//输出：True
//        示例2:
//
//输入：s1 = "aa", s2 = "aba"
//输出：False
//
//        来源：力扣（LeetCode）
//链接：https://leetcode.cn/problems/string-rotation-lcci
//著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution {
public:
    //nextval数组
    vector<int>getnext(string s){
        //求助next数组
        vector<int>next(s.size(),-1);
        int i=0,k=-1;
        while(i<s.size()-1){
            if(k==-1||s[k]==s[i]){
                i++;
                k++;
                next[i]=k;
            }
            else{
                k=next[k];
            }
        }
        //求取nextval数组
        for(int i=1;i<s.size();++i){
            if(s[i]==s[next[i]]) {
                if(next[next[i]]==-1)
                    next[i]=0;
                else
                    next[i]=next[next[i]];
            }
        }
        return next;
    }

    //将s1 double一下然后从s1中查找s2子串
    bool isFlipedString(string s1, string s2) {
        if(s1==s2)
            return true;
        int n=s1.size();
        if(n!=s2.size())
            return false;
        vector<int>next= getnext(s2);
        string tmp(s1);
        tmp+=s1;
        int i=0,j=0;
        while(2*n-i>=n-j){
            if(tmp[i]!=s2[j]){
                j=next[j];
            }
            i++;
            j++;
            if(j==n)
                return true;
        }
        return false;
    }
};

int main(){
    Solution so;
    string s1,s2;
    cin>>s1>>s2;
    cout<<so.isFlipedString(s1,s2)<<endl;
    return 0;
}