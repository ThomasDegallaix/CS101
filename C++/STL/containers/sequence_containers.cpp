#include <iostream>
#include <vector>
#include <list>
#include <deque>
#include <array>
#include <forward_list>

using namespace std;

/* 
  Vector :
- Dynamic arrays : Resize itself automatically
- Elements placed in contiguous storage : Can be accessed using an iterator
*/

void vectorTest() {

    cout << " ***** VECTOR TEST ***** " << endl;

    vector<int> vector {1,2,3,4,5,6,7,8,9,10};


    // Return vector size
    cout << "Vector size : " << vector.size() << endl;

    // Request that the vector capacity be at least enough to contain n elements

    // return max elements that can be hold by the vector


}

/*
  List :
- Allows non-contiguous memory allocation
- Corresponds to double Linked-list
- Use forward list for single Linked_list
*/

// NB : Almost same functions as vectors
void listTest() {

    cout << " ***** LIST TEST ***** " << endl;

    list<int> list {1,2,3,4,5,6,7,8,9,10};

    for(auto it = list.begin(); it != list.end(); ++it) {
        cout << *it << ' ';
    }

    cout << endl;
}

/*
  Deque (Double ended queue) :
- Similar to vectors but more efficient in case of insertion and deletion
- Contiguous storage may not be garanted
- Can delete and insert both at end and front
*/

// NB : Exactly same functions as vectors but with pop_back() and push_front() functions in addition
void dequeTest() {

    cout << " ***** DEQUE TEST ***** " << endl;

    deque<int> deque {1,2,3,4,5,6,7,8,9,10};

    deque.push_front(11);
    deque.pop_back();
    cout << deque.size() << endl;
    for(auto it = deque.begin(); it != deque.end(); ++it) {
        cout << *it << ' ';
    }

    cout << endl;
}

/*
  Array :
- Fixed size
- Better implementation for C-style arrays
- Array classes knows its own size (don't need to pass it to a function)
- More efficient than C-style arrays
*/

void arrayTest() {

    cout << " ***** ARRAY TEST ***** " << endl;

    // Need so specify array size 
    array<int,10> array {1,2,3,4,5,6,7,8,9,10};


    cout << endl;

}

/*
  Forward list :
- Corresponds to single Linked-list
- Really efficient in moving, insertion, deletion operations
- No backward iteration as it doesn't keep track of previous elements
*/

void forwardListTest() {

    cout << " ***** FORWARD_LIST TEST ***** " << endl;

    forward_list<int> forward_list {1,2,3,4,5,6,7,8,9,10};

    cout << endl;

}

int main() {

    vectorTest();

    listTest();

    dequeTest();

    arrayTest();

    forwardListTest();

    return 0;
}