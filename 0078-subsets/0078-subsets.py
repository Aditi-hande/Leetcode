class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return subb(0,nums,[],[]) #recursion

def subb(i,nums,l,ans):
    print(i,l)
    if i==len(nums):#if we are at the last element of the array
        

        if l not in ans:
            ans.append(l)#if l is not in ans then we will apppend l to nums
        return
    #we have 2 choices here one to choose the element or not to choose a element
    subb(i+1,nums,l+[nums[i]],ans)#choosing an element append the ith element to l and send i+1 to recursion
    subb(i+1,nums,l,ans)#not choosing an element we will just send i+1 to the recursion
    return ans