#merge two Unsorted arrays and return a sorted array
from Selection_sort_new import Selection_sort
from quick_sort import quick_sort
def merge_sorted(nums1, nums2):
    merged = []
    i = j = 0
    if not nums1 and not nums2:
        return None

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            if len(merged)==0 or nums1[i] not in merged:
                merged.append(nums1[i])
            i += 1

        else:
            if len(merged)==0 or nums2[j] not in merged:
               merged.append(nums2[j])
            j += 1


    while i < len(nums1):
        if len(merged)==0 or nums1[i] not in merged:
            merged.append(nums1[i])
        i += 1

    while j < len(nums2):
        if len(merged)==0 or nums2[j] not in merged:
            merged.append(nums2[j])
        j += 1

    return merged

nums1 = [7,1,2,1,2,1,2,1,2,1,2,1,2,1,2,2,2,1,2,1,2,1,2]
nums2 = [1,1]
merged_list = merge_sorted(nums1, nums2)
print(Selection_sort(merged_list))
