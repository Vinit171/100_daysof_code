class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ll = []
        if len(nums1) > len(nums2):
            q = nums2
            s = nums1
        else:
            q = nums1
            s = nums2
        for m in q:
            if m in s:
                ll.append(m)
                s.remove(m)
            else:
                pass

        return (ll)