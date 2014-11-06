/**
 * CSC 341 Assignment 2
 * radixSort.cpp
 * Purpose: This program was our first in c++. This program uses a 
 * linked list to sort numbers in a text document ("data.txt") using 
 * a radix sort algorithm. 
 * 
 * @author Daniel Graham
 * @version 1.0 10/24/2014
 * */

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

/**
 * Implements a Node object with integers as values and a link to the 
 * next Node in series. Will be used for the Queue implementation later.
 * */

class Node{
	int value;
	Node * link;
  public:
	Node();
	Node (int);
	void setValue(int);
	void setLink(Node *);
	Node* getLink();
	void print();
	int getValue();
};

/**
 * Constructs a generic Node. Does not have a link, and the default
 * value is -1.
 * */

Node :: Node(){
	value = -1;
}

/** 
 * Constructs a Node to a specified value. Does not have a link.
 * 
 * @param startNum The initial value of the value variable for a Node.
 * */

Node :: Node(int startNum){
	value = startNum;
}

/**
 * Changes the value of the Node object from its initial value to num.
 * 
 * @param num The new value of the value variable.
 * */

void Node :: setValue(int num){
	value = num;
}

/**
 * Returns the linked Node of the current Node.
 * 
 * @return link The Node that the current Node has stored as link.
 * */

Node* Node :: getLink(){
	return link;
}

/**
 * Returns the value stored in the Node.
 * 
 * @return value The value stored in the Node.
 * */

int Node :: getValue(){
	return value;
}

/**
 * Prints the value stored in the Node to the screen.
 * */

void Node :: print(){
	cout << getValue() << "\n";
}

/**
 * Sets the link of the current Node to a new Node pointer. 
 * 
 * @param nodeToLink The pointer to the Node which will be linked to
 * 					 the current Node.
 * */
 
void Node :: setLink(Node * nodeToLink){
	link = nodeToLink;
}

/**
 * Implements an integer queue with the preceeding Node objects. Allows 
 * basic enqueue and dequeue options, but is limited to integers.
 * */

class Queue{
		int length;
		Node * queueHead, * queueTail;
	public:
		Queue();
		void enqueue(int);
		int dequeue();
		int peek(Node *);
		void printQueue();
		void radixSort();
		void readFromFile();
	};
	
/**
*   Constructs an empty Queue with a length of 0.
* */
	
Queue :: Queue(){
	length = 0;
}

/**
 * 	Enqueues an integer onto the Queue using a Node. Also sets the 
 * 	pointers to the tail (and head in an initially empty list) to the 
 * 	correct positions. The method also increments the length variable 
 * 	and sets links correctly.
 * 
 * @param numToEnqueue The number to enqueue to the Queue.
 * */
	
void Queue :: enqueue(int numToEnqueue){
	Node * nodeToEnqueue = new Node(numToEnqueue);
	
	if(length == 0){
		queueHead = nodeToEnqueue;
		queueTail = nodeToEnqueue;
	}
	else{
		(*queueTail).setLink(nodeToEnqueue);
		queueTail = nodeToEnqueue;
	}
	length ++;
}

/**
 * 	Dequeues the Node at the queueHead position, unless Queue is empty.
 * 	Returns the value at the head of the Queue, and deletes the pointer
 * 	to that Node.
 * 
 * @return returnValue Either NULL if the Queue is empty, or the integer
 * 					   at the head of the Queue.
 * */

int Queue :: dequeue(){
	Node * newHead;
	if (length == 0){
		cout << "Queue EMPTY!\n";
		return NULL;
	}
	else{
		int returnValue = (*queueHead).getValue();
		newHead = (*queueHead).getLink();
		delete queueHead;
		queueHead = newHead;
		length --;
		return returnValue;
	}
}

/**
 * 	Looks at the value of a Node in the Queue without dequeueing it.
 * 	Used in the printQueue() method.
 * 
 * 	@param nodeToPeek The pointer of the Node to get the value of.
 * 	@return Returns the value of the Node at the pointer in param.
 * */
 
int Queue :: peek(Node * nodeToPeek){
	return (*nodeToPeek).getValue();
}

/**
 * 	Prints the Queue in order without changing the Queue.
 * */
 
void Queue :: printQueue(){
	int staticLength = length;
	for(int i = 0; i < staticLength; i ++){
		int numToDequeue = dequeue();
		cout << numToDequeue << "\n";
		enqueue(numToDequeue);
	}
}

/**
 * 	Sorts the Queue using the Radix algorithm. Uses a tempSortQueue to 
 * 	store sorts from each tens place sort. Only sorts numbers up to 
 * 	4 digits long. 
 * */

void Queue :: radixSort(){
	Queue* tempSortQueue = new Queue;
	int staticLength = length;
	for(int i = 1; i < 1001; i = i * 10){
		for(int j = 0; j < 10; j++){
			staticLength = length;
			for (int k = 0; k < staticLength; k++){
				if(length > 0){
					int numToTest = dequeue();
					int numToTestModified = numToTest / i;
					if((numToTestModified % 10) == j){
						(*tempSortQueue).enqueue(numToTest);
					}
					else{
					enqueue(numToTest);
					}
				}
			}
		}
		while((*tempSortQueue).length > 0){
			int oneSortNum = (*tempSortQueue).dequeue();
			enqueue(oneSortNum);
		}
	}
	delete tempSortQueue;
}

/**
 * 	Reads the file "data.txt" and enqueues the items in that file in
 * 	the order they are present in that file. Stops input if reaches a
 * 	negative number or the end of the file.
 * */
 	
void Queue :: readFromFile(){
	//Code inspired by: http://www.cplusplus.com/doc/tutorial/files/
		string line;
		ifstream inputFile;
		inputFile.open("data.txt");
		int intFromFile;
		while(getline(inputFile, line)){
			stringstream convert(line);
			if( !(convert >> intFromFile)){
				intFromFile = 0;
				cout << "Could not convert File to integers";
			}
			else if(intFromFile >= 0){
				enqueue(intFromFile);
			}
			else{
				break;
			}
		}
	}
	
/**
 * This method tests the radixSort, Queue, and Node	objects.
 * **/
		

int main(){
	
	
	/*The commented out code was used for testing.
	Node node1(1),node2(2),node3(3), returnNode;
	node1.print();
	node2.print();
	node3.print();
	returnNode.print();
	node1.setValue(4);
	node1.print();
	node1.linkNode(&node2);
	node2.linkNode(&node3);
	returnNode.setValue((*(node2.getNextNode())).getValue());
	returnNode.print();
	
	/*
	 * OUTPUT SHOULD BE:
	 * 1
	 * 2
	 * 3
	 * -1
	 * 4
	 * 3
	 * 
	cout << "\n";
	Queue testQueue, testQueue1, testQueue2;
	testQueue.enqueue(4);
	testQueue.enqueue(3);
	testQueue.enqueue(2);
	testQueue.enqueue(1);

	testQueue.printQueue();
	testQueue.dequeue();
	testQueue.dequeue();
	cout << "\n";
	testQueue.printQueue();
	/*
	 * OUTPUT SHOULD BE:
	 * 4
	 * 3
	 * 2
	 * 1
	 * 
	 * 2
	 * 1
	 * 
	cout << "\n";
	testQueue.enqueue(3);
	testQueue.enqueue(4);
	testQueue.radixSort();
	testQueue.printQueue();
	
	/*Output should be:
	 * 1
	 * 2
	 * 3
	 * 4
	 * 
	cout << "\n";
	testQueue.enqueue(324);
	testQueue.enqueue(6346);
	testQueue.enqueue(1000);
	testQueue.enqueue(5);
	testQueue.radixSort();
	testQueue.printQueue();
	
	/* Output should be:
	 * 1
	 * 2
	 * 3
	 * 4
	 * 5
	 * 324
	 * 1000
	 * 6346
	 * 
	
	
	/*TEST FOR READ FROM FILE
	
	cout << "\n";
	cout << "\n";
	cout << "\n";
	
	testQueue2.readFromFile();
	testQueue2.radixSort();
	testQueue2.printQueue();
	
	*/
	Queue sortedQueue;
	sortedQueue.readFromFile();
	sortedQueue.radixSort();
	sortedQueue.printQueue();
	
	return 0;
}
