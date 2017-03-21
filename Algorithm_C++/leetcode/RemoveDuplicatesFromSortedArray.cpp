class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        //distance返回两个迭代器之间的距离
        //unique删除指定范围中的所有连续重复元素，仅仅留下每组等值元素中的第一个元素,返回指向最后一个未被删除元素之后位置的迭代器
        return distance(nums.begin(),unique(nums.begin(),nums.end()));
    }
};