class EbookBase:

    splitters=[". ", "! ", "? "]
    data=""
    sentances=[]
    pages=[]
    _current_page=0
    _bookmark={}

    def __init__(self, file):
        self.readfile(file)
        self.splitSentances()
        self.splitPage()


    def readfile(self, file):
        f=open(file, 'r')
        self.data=f.readlines()[0]


    def splitSentances(self, arg=None):
        for i in self.splitters:
            self.data=self.data.replace(i, i+"SPLITTERR")
        self.sentances=self.data.split('SPLITTERR')


    def splitPage(self, arg=None):
        while len(self.sentances) > 0:
            page=''
            for i in range(0, 3):
                if self.sentances:
                    page+=str(self.sentances[0])
                    self.sentances.pop(0)

            self.pages.append(page)
            page=""


    def get_currentPage(self):
        return self.pages[self._current_page]


    def get_currentPageNumber(self, arg=None):
        return self._current_page


    def get_totalPageNumbers(self, arg=None):
        return len(self.pages)


    def set_currentPageNumber(self, num):
        try:
            num=int(num)
            if num >= 0 and num < len(self.pages):
                self._current_page=num
            elif num > len(self.pages):
                self._current_page=len(self.pages)-1
            elif num < 0:
                self._current_page=0
        except IndexError:
            print("Please input nuber")
            return

    def set_bookmark(self, pageNum, mark):
        pageNum=int(pageNum)
        if pageNum >= 0 and pageNum < len(self.pages):
            self._bookmark[pageNum]=mark
        else:
            return

    def del_bookmark(self, num):
        self._bookmark.pop(num)


class Read(EbookBase):

    def nextPage(self, arg=None):
        if self.get_currentPageNumber()+1:
            self.set_currentPageNumber(int(self.get_currentPageNumber())+1)

    def prevPage(self, arg=None):
        if self.get_currentPageNumber()-1:
            self.set_currentPageNumber(int(self.get_currentPageNumber())-1)

    def moveN_pagesForvard(self, arg=None):
        page=input("Put page number")
        try:
            page=int(page)
            if page:
                self.set_currentPageNumber(self.get_currentPageNumber() + page)
            else:
                return
        except ValueError:
            print("Incorect input")
            return

    def moveN_pagesBack(self, arg=None):
        page=input("Put page number")
        try:
            page=int(page)
            if page:
                self.set_currentPageNumber(self.get_currentPageNumber() - page)
            else:
                return
        except ValueError:
            print("Incorect input")
            return

    def moveToFirstPage(self, arg=None):
        self.set_currentPageNumber(0)

    def moveToLastPage(self, arg=None):
        self.set_currentPageNumber(len(self.pages))
        print(len(self.pages))

    def set_bookmarkOnCurrentPage(self, arg=None):
        mark=input("Put your bookmark")
        page=input("Put page number or leave empty if you want to set bookmark on current page")
        try:
            if page:
                self.set_bookmark(int(page), mark)
            else:
                self.set_bookmark(self.get_currentPageNumber(), mark)
        except ValueError:
            print("Incorect input")
        return

    def del_bookmark(self, arg=None):
        page=int(input("Put page number or leave empty if you want to delete bookmark on current page"))
        if page:
            super.self.del_bookmark(page)
        else:
            super.self.del_bookmark(self.get_currentPageNumber())

    def get_bookmarks(self, arg=None):
        for i in self._bookmark.keys():
            print(i, self._bookmark[i])

    def couunt_pages(self, arg=None):
        print(len(self.pages))




def main():
    ebook=Read('text')

    handlers = {'nextPage': ebook.nextPage,
                'prevPage': ebook.prevPage,
                'moveN_pagesForvard': ebook.moveN_pagesForvard,
                'moveN_pagesBack': ebook.moveN_pagesBack,
                'moveToFirstPage': ebook.moveToFirstPage,
                'moveToLastPage': ebook.moveToLastPage,
                'set_bookmarkOnCurrentPage':ebook.set_bookmarkOnCurrentPage,
                'get_bookmarks':ebook.get_bookmarks,
                'del_bookmark':ebook.del_bookmark,
                'couunt_pages':ebook.couunt_pages
                }


    def describe_handlers(arg=None):
        print("Handler list:")
        for i in handlers.keys():
            print("- " + i)



    describe_handlers()

    while True:
        print(ebook.get_currentPage())
        command = input("Do your choice ")

        if len(command) != 0 and handlers.get(command.split()[0]):
            handlers[command.split()[0]](command)

        else:
            print("No such choice, please try something from list")


main()

