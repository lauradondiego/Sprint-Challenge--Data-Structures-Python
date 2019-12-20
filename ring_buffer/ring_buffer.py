from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity  # the max or limit
        self.current = 0
        self.storage = DoublyLinkedList()  # your methods

    def append(self, item):  # adds elements to the buffer
        # when full, the oldest element is overwritten with the newest
        # fixed size
        # append element at the end of the buffer
        # data append in head (newest), data pop from tail (oldest)
        if self.current >= self.capacity:
            self.storage.remove_from_tail()  # remove the oldest item
        # self.storage.add_to_head(item)
            self.current -= 1
        self.storage.add_to_head(item)
        self.current += 1

    def get(self):  # returns all elements in an ordered list
        # except for NONE
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        if list_buffer_contents is not None:
            return list_buffer_contents

# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
