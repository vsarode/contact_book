def get_first_name_last_name_combinations(node, name, is_first_name):
    '''
    Utility function to get combination of first name last name
    :param node: Last node which has first name of last name list (i.e. Trie
    Node)
    :param name: Current node contact
    :param is_first_name: Boolean flag
    :return: List of first name last name combinations
    '''
    name_or_surname = node.name_or_surname
    names = []
    if name_or_surname:
        if is_first_name:
            for surname in name_or_surname:
                if not surname:
                    names.append(name)
                else:
                    names.append(name + ' ' + surname)
        else:
            for surname in name_or_surname:
                if not surname:
                    names.append(name)
                else:
                    names.append(surname + ' ' + name)
    else:
        names = [name]
    return names


def char_to_index(ch):
    '''
    Utility function to get index based on ascii difference of aplphabet
    :param ch: Alphabet to get index
    :return: index between 0 to 26
    '''
    if not ch.isalpha():
        return None
    if ch.isupper():
        return ord(ch) - ord('A')
    else:
        return ord(ch) - ord('a')


def search_data(f_name_root, l_name_root, data):
    '''

    :param f_name_root: This is root for first name
    :param l_name_root: This is root for last name
    :param data: Data to be search could be first name last name
    :return: Matching results in contact trie
    '''
    f_name_last = f_name_root.search(data)
    l_name_last = l_name_root.search(data)
    names = []
    surnames = []
    if f_name_last:
        names = f_name_last.get_closure_words(data[:-1], f_name_last,
                                              True)
    if l_name_last:
        surnames = l_name_last.get_closure_words(data[:-1], l_name_last,
                                                 False)
    names.extend(surnames)
    if f_name_last and f_name_last.is_end_of_word:
        names.reverse()
    print '\n'.join(names)


def insert_data(f_name_root, l_name_root, data):
    '''
    Inserts contact data
    :param f_name_root: First name root (ie. Trie node)
    :param l_name_root: Last name root (ie. Trie node)
    :param data: Contact data to insert
    :return: Status
    '''
    try:
        splited_data = data.split(" ")
        name = splited_data[0]
        f_name_last_node = f_name_root.insert(name)

        if len(splited_data) > 1:
            last_name = splited_data[1]
            l_name_last_node = l_name_root.insert(last_name)

            f_name_last_node.s_node[char_to_index(last_name[0])] = \
                l_name_root.children[
                    char_to_index(
                        last_name[0])]
            if last_name not in f_name_last_node.name_or_surname:
                f_name_last_node.name_or_surname.append(last_name)
            else:
                # print "Contact already exist."
                return False

            l_name_last_node.s_node[char_to_index(name[0])] = \
                f_name_root.children[
                    char_to_index(
                        name[0])]
            if name not in l_name_last_node.name_or_surname:
                l_name_last_node.name_or_surname.append(name)
            else:
                # print "Contact already exist."
                return False

        else:
            if None not in f_name_last_node.name_or_surname:
                f_name_last_node.name_or_surname.append(None)
            else:
                # print "Contact already exist."
                return False
    except:
        return False
    return True
