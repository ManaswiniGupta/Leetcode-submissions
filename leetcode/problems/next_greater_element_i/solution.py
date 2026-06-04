class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d={}
        
        for i in range(len(nums2)):
            y=0
            while stack and nums2[i]>nums2[stack[-1]]:
                m=stack.pop()
                d[nums2[m]]=nums2[i]+y
            stack.append(i) 
        ans=[]
        for k in nums1:
            if k in d.keys():
                ans.append(d.get(k))
            else:
                ans.append(-1)
        # print(d)
        return ans

        # stack = []
        # answer = [-1]*len(nums1)
        # for i in range(len(nums1)):
        #     k=0
        #     for j in range(len(nums2)):
        #         if nums1[i]==nums2[j]:
        #             k=j
        #             break
        #     nums21=nums2[k:]
        #     for m in range(len(nums2[k-1:])):
        #         while stack and nums21[m]>stack[-1]:
        #             r=stack.pop()
        #             answer[i]=r
        #         stack.append(nums21[m])
        # return answer



        