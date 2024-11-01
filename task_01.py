class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    #Функція для реверсування списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    #Функція для сортування списку 
    def merge_sort(self):
        if not self.head or not self.head.next:
            return self.head

        mid = self.get_middle(self.head)
        next_to_mid = mid.next
        mid.next = None

        left = LinkedList()
        left.head = self.head
        left.merge_sort()

        right = LinkedList()
        right.head = next_to_mid
        right.merge_sort()

        self.head = self.sorted_merge(left.head, right.head)

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, left, right):
        if not left:
            return right
        if not right:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)
        return result

    
    def merge_two_sorted_lists(self, l1, l2):
        dummy = Node(0)
        tail = dummy

        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next



#Створюємо список і додаємо елементи
llist = LinkedList()
llist.insert_at_end(4)
llist.insert_at_end(3)
llist.insert_at_end(1)
llist.insert_at_end(2)

print("Оригінальний список:")
llist.print_list()

#Реверсування списку
llist.reverse()
print("\nРеверсований список:")
llist.print_list()

#Сортування списку
llist.merge_sort()
print("\nВідсортований список:")
llist.print_list()

#Другий відсортований список 
llist2 = LinkedList()
llist2.insert_at_end(5)
llist2.insert_at_end(6)
llist2.insert_at_end(7)

#Об'єднання двох відсортованих списків
merged_head = llist.merge_two_sorted_lists(llist.head, llist2.head)

print("\nОб'єднаний відсортований список:")
current = merged_head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
