# Intro:
    'Contact book' is an application implemented using trie data structure to 
    store 
    contacts. It is highly optimised for searching contacts.
    
    Trie is an efficient information reTrieval data structure.
    Using Trie, search complexities can be brought to optimal limit (key length). 
    If we store keys in binary search tree, a well balanced BST will need time proportional to M * log N, where M is maximum string length and N is number of keys in tree.
    
# Steps to extract project
```
tar -xvzf contact_book.tar.gz
```

# Steps to run the test cases
1) Go to project folder 

```
cd  contact_book
```
    
2) Export python path
```
export PYTHONPATH=$PWD;
```

3) Run basic test 
```
python contact_book/tests/test_contacts_trie.py
```


4) Run utility functions test
```
python contact_book/tests/test_contact_function.py
```


5) Run performance test
```
python contact_book/tests/test_performance.py
```

# Steps to run the app
1) Go to project folder 
```
cd  contact_book
```
    
2) Export python path
```
export PYTHONPATH=$PWD;
```

3) Run app
```
python contact_book/src/app.py
```

Eg.
```
1) Add contact 2) Search 3) Exit
1
Enter name: vitthal sarode
1) Add contact 2) Search 3) Exit
1
Enter name: shree vitthal
1) Add contact 2) Search 3) Exit
2
Enter name: vit
vitthal sarode
shree vitthal
1) Add contact 2) Search 3) Exit
3
Happy Searching
```
