class AppendLeft(list):

    def append_zero(self, arg):
        self.insert(0, arg)

    def append(self, n, args=False):
        if args:
            self.append_zero(n)
        else:
            super().append(n)


new_list=AppendLeft([1,2,3,4,5,6])

new_list.append(2, True)

print(new_list)