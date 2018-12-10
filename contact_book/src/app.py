from contact_book.src.contacts_trie import Trie, insert_data, search_data


def deligator(choice):
    deligator_map = {
        1: insert_data,
        2: search_data,
    }

    return deligator_map.get(choice)


class ContactBook:
    def __init__(self):
        self.name = Trie('')
        self.surname = Trie('')

    def run(self):
        while True:
            choice = input('1) Add contact 2) Search 3) Exit\n')
            func = deligator(choice)
            if func:
                data = raw_input('Enter name: ')
                func(self.name, self.surname, data)
            else:
                print "Happy Searching"
                break


if __name__ == '__main__':
    c = ContactBook()
    c.run()
