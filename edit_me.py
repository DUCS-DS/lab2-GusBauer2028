
def monotonic(lst):
    """Return True if lst is monotonic; return False, otherwise."""

    increasing = decreasing = True


    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            decreasing = False
        if lst[i] < lst[i - 1]:
            increasing = False

    return increasing or decreasing 
print(monotonic([1,3,5,9]))#True
print(monotonic([1,3,5,4]))#false
#
