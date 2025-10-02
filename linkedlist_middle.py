# linkedlist_middle.py

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, value):
        """Insert node at the end"""
        node = Node(value)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def to_list(self):
        """Convert linked list to Python list (for printing)"""
        res = []
        cur = self.head
        while cur:
            res.append(cur.value)
            cur = cur.next
        return res

    def find_middle_one_pass(self):
        """
        Find middle node in one pass using slow & fast pointer method.
        For even number of nodes -> returns the first of the two middles.
        """
        slow = self.head
        fast = self.head

        if not self.head:
            return None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value if slow else None

    def __repr__(self):
        return "->".join(map(str, self.to_list()))


def main():
    print("=== Singly Linked List - Find Middle (One Pass) ===")

    # Take user input
    values = input("Enter elements of the linked list (space-separated): ").strip().split()
    
    ll = SinglyLinkedList()
    for v in values:
        ll.insert_end(int(v))  # store as integers

    print("\nList:", ll)
    middle = ll.find_middle_one_pass()
    if middle is not None:
        print("Middle element:", middle)
    else:
        print("The list is empty!")

if __name__ == "__main__":
    main()
