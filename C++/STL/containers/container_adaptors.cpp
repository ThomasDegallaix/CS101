#include <iostream>
#include <queue>
#include <stack>

using namespace std;

/*
  Queue :
- FIFO type of arrangement
*/

void queueTest() {

    cout << " ***** QUEUE TEST ***** " << endl;

    queue<int> queue;

    cout << "Push :" << endl;
    queue.push(1);
    cout << " Front : " << queue.front() << " Back : " << queue.back() << endl;
    queue.push(2);
    cout << " Front : " << queue.front() << " Back : " << queue.back() << endl;
    queue.push(3);
    cout << " Front : " << queue.front() << " Back : " << queue.back() << endl;

    cout << "Pop :" << endl;
    queue.pop();
    cout << " Front : " << queue.front() << " Back : " << queue.back() << endl;
    queue.pop();
    cout << " Front : " << queue.front() << " Back : " << queue.back() << endl;
    queue.pop();
    cout << " Front : " << queue.front() << " Back : " << queue.back() << endl;
    
    cout << "Queue size : " << queue.size() << endl;

    cout << endl;

}

/*
  Priority queue :
- Same as queue but elements are stored are stored in non increasing order
- Idea of a priority element that needs to be pop first
*/

void priorityQueueTest() {

    cout << " ***** PRIORITY QUEUE TEST ***** " << endl;

    priority_queue<int> priority_queue;

    priority_queue.push(1);
    priority_queue.push(7);
    priority_queue.push(6);
    priority_queue.push(2);
    priority_queue.push(5);

    while(!priority_queue.empty()) {
        cout << priority_queue.top() << ' ';
        priority_queue.pop();
    }
    
    cout << endl;

}

/* 
  Stack :
- LIFO type of arrangement
*/

void stackTest() {

    cout << " ***** STACK TEST ***** " << endl;

    stack<int> stack;

    stack.push(1);
    cout << stack.top() << ' ';
    stack.push(2);
    cout << stack.top() << ' ';
    stack.push(3);
    cout << stack.top() << ' ';
    stack.push(4);
    cout << stack.top() << ' ';
    stack.push(5);
    cout << stack.top() << endl;

    
    cout << "Popping 2 elements : " << endl;
    stack.pop();
    stack.pop();

    while(!stack.empty()) {
        cout << stack.top() << ' ';
        stack.pop();
    }


    cout << endl;

}

int main() {

    queueTest();

    priorityQueueTest();

    stackTest();

    return 0;
}