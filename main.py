# A Python script solving https://www.codewars.com/kata/515bb423de843ea99400000a/train/python
# TODO: complete this class
import math


class PaginationHelper:

    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        n = round(self.item_count() / self.page_count())
        self.chunks = []

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return math.ceil(self.item_count() / self.items_per_page)

    def chunks(self):

        self.chunks = [self.collection[x:x+n] for x in range(0, len(self.collection), n)]
        print(self.chunks)
        return 0

    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        return 0


    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
    my_helper.chunks()
    print(f" item count: {my_helper.item_count()}, page count: {my_helper.page_count()}")
    print(my_helper.chunks[0])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
