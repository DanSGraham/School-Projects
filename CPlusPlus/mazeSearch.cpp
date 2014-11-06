/**
 *  This program is meant to generate a maze of characters and using
 *  breadth first search, determine the if the maze has an exit.
 * @author Daniel Graham
 * @version 1.0 10/17/2014
 * */
 
 #include <iostream>
 #include <stdlib.h>
 #include <ctime>

 
 using namespace std;
 
 /**
  * Class of Location objects. Each object has x,y coordinates and a
  * char associated with them. 
  * 
  * @author Daniel Graham
  * */
 
class Location{
        int x;
        int y;
        char item;
    public:
		Location();
        int getX();
        int getY();
        void setX(int);
        void setY(int);
        char getItem();
        void setItem(char);
};

/**
 * Constructor for a Location object. Sets initial positions and chars.
 * */

Location :: Location(){
	x = 0;
	y = 0;
	item = '-';
}


/**
 * Returns x coordinate of Location object.
 * */

int Location :: getX(){
	return x;
}

/**
 * Returns y coordinate of Location object.
 * */

int Location :: getY(){
	return y;
}


/**
 * Sets the value of x to xToSet.
 * 
 * @param xToSet the integer to set x value.
 * */

void Location :: setX(int xToSet){
	x = xToSet;
}

/**
 * Sets the value of y to yToSet.
 * 
 * @param yToSet the integer to set y value.
 * */

void Location :: setY(int yToSet){
	y = yToSet;
}

/**
 * Returns the character stored as item.
 * */

char Location :: getItem(){
	return item;
}

/**
 * Sets item to itemToSet.
 * 
 * @param itemToSet the character to set item.
 * */

void Location :: setItem(char itemToSet){
	item = itemToSet;
}

/**
 * Implements a Node object with Location pointers as values and a link 
 * to the next node in series. Will be used for the Queue implementation
 * This Node class is a modification of the Node class in radixSort.cpp
 * */

class Node{
	Location * value;
	Node * link;
  public:
	Node();
	Node (Location*);
	void setValue(Location*);
	void setLink(Node *);
	Node * getLink();
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

Node * Node :: getLink(){
	return link;
}

/**
 * Returns the value stored in the Node.
 * 
 * @return value The value stored in the Node.
 * */

Location * Node :: getValue(){
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
		int getLength();
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

/**
 * Returns the current length of the Queue object.
 * */

int Queue :: getLength(){
	return length;
} 

/**
 * Class to create a maze using location objects and search that maze
 * using breadth first search and a queue implementation.
 * 
 * @author Daniel Graham
 * */

class Maze{
        Location * mazeArray[40][50];
        Location * locationOfU;
        Location * locationOfX;
        Queue * searchQueue;
    public:
        Maze();
        void printMaze();
        bool searchMaze();
        void enqueueLocations(int, int);
        Location * getLocation(int, int);
    };
   
   
/**
 * Constructor for the Maze Object. Initializes  size to 50 x 40 and 
 * fills the two dimensional array of Locations.
 * */

Maze :: Maze(){
	srand(time(NULL));
	int arrayXSize = 50;
	int arrayYSize = 40;
	locationOfU = new Location();
	locationOfX = new Location();
	for(int n = 0; n < arrayYSize; n++){
		for(int m = 0; m < arrayXSize; m++){
			mazeArray[n][m] = new Location();
		}
	}
	
    (*locationOfU).setX((rand() % 48) + 1);
    (*locationOfU).setY(rand() % 38 + 1);
    (*locationOfU).setItem('U');
    int oneDLocationOfX = (rand() % 175);
    for(int i = 0; i < 40; i++){
        for(int j = 0; j < 50; j++){
            
            if((i <= 0 || i >= 39) || (j <= 0 || j >= 49)){
                if(oneDLocationOfX <= 0){
                    (*mazeArray[i][j]).setItem('X');
                    oneDLocationOfX = 10000000; //will never be <= 0
                }
                else{
                    (*mazeArray[i][j]).setItem('W');
                }
                oneDLocationOfX --;
            }
            else{
				if((rand() % 10) <= 5){
					 (*mazeArray[i][j]).setItem('W');
				 }
			 }
            (*mazeArray[i][j]).setY(i);
            (*mazeArray[i][j]).setX(j);
        }
    }
    mazeArray[(*locationOfU).getY()][(*locationOfU).getX()] = locationOfU;
}
    
    
/**
 * Prints the maze as is to the terminal.
 * */

void Maze :: printMaze(){
    
    for(int i = 0; i < 40; i++){
        for(int j = 0; j < 50; j++){
            cout << (*mazeArray[i][j]).getItem();
        }
        cout << "\n";
    }
}

/**
 * Returns the Location object at x,y in the mazeArray.
 * 
 * @param x coordinate in the mazeArray of the Location.
 * @param y coordinate in the mazeArray of the Location.
 * @return mazeArray the Location object at x,y in the mazeArray.
 * 
 * */

Location * Maze :: getLocation(int x, int y){
	return mazeArray[y][x];
}

/**
 * Uses breadth first search and a queue implementation to determine
 * if there is a path from U to X with no Ws in the way.
 * 
 * @return value whether or not the maze has an exit.
 * */

bool Maze :: searchMaze(){
	searchQueue = new Queue();
	int originX = (*locationOfU).getX();
	int originY = (*locationOfU).getY();
	enqueueLocations(originX, originY);
	while((*searchQueue).getLength() != 0){
		Location * nextQueue = (*searchQueue).dequeue();
		if((*nextQueue).getItem() == 'X'){
			delete searchQueue;
			return true;
		}
		enqueueLocations((*nextQueue).getX(), (*nextQueue).getY());
	}
	delete searchQueue;
	return false;
	}


/**
 * Enqueues Locations to the queue to be searched in the searchMaze
 * method. 
 * 
 * @param x the x coordinate of the origin Location to enqueue around.
 * @param y the y coordinate of the origin Location to enqueue around.
 * */

void Maze :: enqueueLocations(int x, int y){
	Location * possLocations[4] = {getLocation(x, y - 1), getLocation(x, y + 1), getLocation(x - 1, y), getLocation(x + 1, y)};
	for(int i = 0; i < 4; i++){
		Location * testLoc = possLocations[i];
		if((*testLoc).getItem() == '-' || (*testLoc).getItem() == 'X'){
			(*searchQueue).enqueue(possLocations[i]);
			if((*testLoc).getItem() == '-'){
				(*testLoc).setItem(' ');
			}
		}
	}
}

	
/**
 * Runs the maze program one time, initializing the a random Maze and
 * checking if the maze is escapable.
 * */	

int main(){
    Maze* testMaze = new Maze();
    (*testMaze).printMaze();
    if((*testMaze).searchMaze()){
		cout << "Escaped the Maze!!!\n";
	}
	else{
		cout <<"There is NO Escape from the Maze of Doom\n";
	}
    return 0;
}
