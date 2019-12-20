from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity  # the max or limit
        self.current = 0
        self.storage = DoublyLinkedList()  # your methods

    def append(self, item):  # adds elements to the buffer
        # lru_cache
        # when full, the oldest element is overwritten with the newest
        # fixed size
        # append element at the end of the buffer
        # data append in head (newest), data pop from tail (oldest)
        if self.capacity > self.storage.__len__():
            # if room allows, add the newest item to the head below
            self.storage.add_to_head(item)
        # self.storage.add_to_head(item)
            # self.current -= 1
        else:
            self.storage.remove_from_tail()  # remove the oldest item
            self.storage.add_to_head(item)

    def get(self):  # returns all elements in an ordered list
        # except for NONE
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        num = 0
        while num < self.storage.__len__():  # less than 0
            # ^ loop thru storage
            current_head = self.storage.head  # get the head
            list_buffer_contents.append(current_head.value)
            # ^ append head value to list. value comes from DLL
            self.storage.move_to_end(current_head)
            # ^ shift the head to the tail
            num += 1  # counter by 1
        return list_buffer_contents


# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
