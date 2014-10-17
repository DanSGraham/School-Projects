/**
 *  This program is meant to 
 * @author Daniel Graham
 * @version 1.0 10/17/2014
 * */
 
 #include <iostream>
 #include <stdlib.h>
 
 using namespace std;
 
class Location{
        int x;
        int y;
        char item;
    public:
        int getX();
        int getY();
        void setX(int);
        void setY(int);
        char getItem();
        void setItem(char);
        Location* getNorth();
        Location* getEast();
        Location* getSouth();
        Location* getWest();
};

/**
 * Implements a Node object with Location pointers as values and a link 
 * to the next node in series. Will be used for the Queue implementation
 * This Node class is a modification of the Node class in radixSort.cpp
 * */

class Node{
	Location* value;
	Node* link;
  public:
	Node();
	Node (Location*);
	void setValue(Location*);
	void setLink(Node *);
	Node* getLink();
	void print();
	Location* getValue();
};

/**
 * Constructs a generic Node. Does not have a link, and the default
 * value is NULL.
 * */

Node :: Node(){
	value = NULL;
}

/** 
 * Constructs a Node to a specified value. Does not have a link.
 * 
 * @param startNum The initial value of the value variable for a Node.
 * */

Node :: Node(Location* startNum){
	value = startNum;
}

/**
 * Changes the value of the Node object from its initial value to loc.
 * 
 * @param num The new value of the value variable.
 * */

void Node :: setValue(Location* loc){
	value = loc;
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

Location* Node :: getValue(){
	return value;
}

/**
 * Prints the item of the Location stored in the Node to the screen.
 * */

void Node :: print(){
	cout << (*getValue()).getItem() << "\n";
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
 * Implements a Location queue with the preceeding Node objects. Allows 
 * basic enqueue and dequeue options, but is limited to Location objects
 * This Queue is a modification of the Queue class in radixSort.cpp.
 * */

class Queue{
		int length;
		Node * queueHead, * queueTail;
	public:
		Queue();
		void enqueue(Location*);
		Location* dequeue();
	};
	
/**
*   Constructs an empty Queue with a length of 0.
* */
	
Queue :: Queue(){
	length = 0;
}

/**
 * 	Enqueues a Location onto the Queue using a Node. Also sets the 
 * 	pointers to the tail (and head in an initially empty list) to the 
 * 	correct positions. The method also increments the length variable 
 * 	and sets links correctly.
 * 
 * @param locToEnqueue The Location to enqueue to the Queue.
 * */
	
void Queue :: enqueue(Location* locToEnqueue){
	Node * nodeToEnqueue = new Node(locToEnqueue);
	
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
 * @return returnValue Either NULL if the Queue is empty, or Location
 * 					   at the head of the Queue.
 * */

Location* Queue :: dequeue(){
	Node * newHead;
	if (length == 0){
		cout << "Queue EMPTY!\n";
		return NULL;
	}
	else{
		Location* returnValue = (*queueHead).getValue();
		newHead = (*queueHead).getLink();
		delete queueHead;
		queueHead = newHead;
		length --;
		return returnValue;
	}
}

  

class Maze{
        Location* mazeArray[40][50];
        Location* locationOfU;
        Location* locationOfX;
    public:
        Maze();
        void printMaze();
        bool searchMaze();
    };
    
Maze :: Maze(){
    (*locationOfU).setX(rand() % 48 + 1);
    (*locationOfU).setY(rand() % 38 + 1);
    (*locationOfU).setItem('U');
    
    //Confirm the oneDLocationOfX process.
    int oneDLocationOfX = (rand() % 175);
    
    for(int i = 0; i < 40; i++){
        for(int j = 0; j < 50; j++){
            
            if((i <= 0 || i >= 39) || (j <= 0 || j >= 49)){
                if(oneDLocationOfX <= 0){
                    (*mazeArray[i][j]).setItem('X');
                    oneDLocationOfX = 1000;
                }
                else{
                    (*mazeArray[i][j]).setItem('W');
                }
                oneDLocationOfX --;
            }
            else if( i != (*locationOfU).getY() && j != (*locationOfU).getY()){
                (*mazeArray[i][j]).setItem('-');
                }
            (*mazeArray[i][j]).setY(i);
            (*mazeArray[i][j]).setX(j);
        }
    }
}
    
void Maze :: printMaze(){
    
    for(int i = 0; i < 40; i++){
        for(int j = 0; j < 50; j++){
            cout << (*mazeArray[i][j]).getItem();
        }
        cout << "\n";
    }
}

int main(){
    Maze* testMaze = new Maze();
    (*testMaze).printMaze();
    return 0;
}
