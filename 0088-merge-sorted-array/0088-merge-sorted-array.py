class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i=0
        j=0
        set1=nums1[:m]
        nums1[:]=[]
        while i<m and j<n:
            if set1[i]<nums2[j]:
                nums1.append(set1[i])
                i+=1
            elif set1[i]>nums2[j]:
                nums1.append(nums2[j])
                j+=1
            else:
                nums1.append(nums2[j])
                nums1.append(set1[i])
                i+=1
                j+=1
        if i==m and j!=n:
            for temp in range(j,len(nums2)):
                nums1.append(nums2[temp])
        if j==n and i!=m:
            for temp in range(i,len(set1)):
                nums1.append(set1[temp])
        """
        Do not return anything, modify nums1 in-place instead.
        """