class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode()  # Dummy node to start the merged list
    current = dummy
    
    while list1 and list2:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Append any remaining nodes from list1 or list2
    if list1:
        current.next = list1
    if list2:
        current.next = list2
    
    return dummy.next

# Function to print the merged list
def printList(node):
    while node:
        print(node.value, end=" ")
        if node.next:
            print(">", end=" ")
        node = node.next
    print()

# Create sample linked lists
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# Merge the two lists
result = mergeTwoLists(list1, list2)

# Print the merged list
print("Merged List:", end=" ")
printList(result)
