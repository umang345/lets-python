'''
def intersection(nums1, nums2):
    """
    Function to find the intersection of two integer arrays.
    :param nums1: List[int] -> First array of integers
    :param nums2: List[int] -> Second array of integers
    :return: List[int] -> An array of unique integers present in both arrays
    """
    
    ### Approach 1 ####
    set1 = set(nums1)
    set2 = set(nums2)
    return [num for num in set1.intersection(set2)]
'''

def intersection(nums1, nums2):
    """
    Function to find the intersection of two integer arrays.
    :param nums1: List[int] -> First array of integers
    :param nums2: List[int] -> Second array of integers
    :return: List[int] -> An array of unique integers present in both arrays
    """
    
    ### Approach 1 ####
    set1 = set(nums1)
    set2 = set(nums2)
    return [num for num in set1.intersection(set2)]