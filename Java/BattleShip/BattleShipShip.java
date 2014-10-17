/*
* Author: Daniel Graham
* Purpose: CSC 300 Battleship Project
* Date: 10/1/14
*/
//package Battleship;


/**
 * This class represents Ship objects on the BattleShipBoard object. It contains information about the Ship Objects.
 * @author Daniel
 *
 */
public class BattleShipShip{
	
	int[][] coords;     //The Ship coordinates are held in a [2][shipLength] size array. X coordinates are [0] and Y coordinates are [1].
	String type;
	boolean sunk;
	int hits;
	int coordsIndex;
	int length;
	String orientation;
	/**
	 * This is the constructor for the Ship Object. inputType should never be incorrect, because whenever this method is called,
	 * it is called with a known inputType.
	 * 
	 * @param inputType The name of the ship to be created (ex. Aircraft Carrier)
	 */
	public BattleShipShip(String inputType){
		hits = 0;
		sunk = false;
		type = inputType;
		coordsIndex = 0;
		switch (inputType){
			
			case "Aircraft Carrier": coords = new int[2][5];
			length = 5;
				break;
				
			case "Battleship": coords = new int[2][4];
			length = 4;
				break;
				
			case "Submarine": coords = new int[2][3];
			length = 3;
				break;
				
			case "Destroyer": coords = new int[2][3];
			length = 3;
				break;
			case "Patrol Boat": coords = new int[2][2];
			length = 2;
				break;		
			default:
				System.out.println("Incorrect Input Type");
		}
	}
	
	/**
	 * Typical get method.
	 * 
	 * @return length the size of the Ship.
	 */
	public int getLength(){
		return length;
	}
	
	/**
	 * Helper method for the setCoords method. Confirms that the ship can actually be placed where the setCoords attempts to set.
	 * 
	 * @param x Horizontal coordinate of ship.
	 * @param y Vertical coordinate of ship.
	 * @return boolean value  Acts as a check if the ship may be placed there. False indicates that ship has incorrect placement.
	 */
	public boolean checkCoords(int x, int y) {
		if(x >= 11 || (y >= 11) || (x < 1) || (y < 1)){ //Checks if ship coords are out of the board bounds.
				return false;
				}
		/*
		 * The following conditionals check that the ships are placed in a straight line by determining an orientation, and then ensuring
		 * that the ships follow that orientation.
		 */
		else if (coordsIndex != 0) {
			if(coordsIndex == 1){
				if(coords[1][coordsIndex - 1] == y) {
					orientation = "Horizontal";
				}
				else if(coords[0][coordsIndex -1] == x) {
					orientation = "Vertical";
				}
				else{
					System.out.println("Cannot determine ship orientation");
					return false;
				}
			}
			else if(orientation.equals("Horizontal") && (!((coords[0][coordsIndex-1] == (x - 1) ||coords[0][coordsIndex-1] == (x + 1)) && (coords[1][coordsIndex-1] == y)))){
				return false;
			}
			else if(orientation.equals("Vertical") && (!((coords[1][coordsIndex-1] == (y - 1) || coords[1][coordsIndex-1] == (y + 1)) && (coords[0][coordsIndex-1] == x)))){
				return false;
			}
		}
		return true;
	}
	
	/**
	 * Basic set method. Sets the coordinates of the ship after checking through checkCoords method.
	 * 
	 * @param x Horizontal coordinate of ship.
	 * @param y Vertical coordinate of ship.
	 * @return boolean value A value confirming if it was successful in adding ship.
	 */
	public boolean setCoords(int x, int y){
		if(!checkCoords(x,y)){
			System.out.println("Error: Incorrect ship placement coordinates.");
			return false;
		}
		else{
		//could check for out of bounds here.
		coords[0][coordsIndex] = x;
		coords[1][coordsIndex] = y;
		coordsIndex++;
		return true;
		}
	}
	
	/**
	 * Basic set method. Changes value of sunk.
	 * 
	 * @param didItSink If ship is damaged fully, it wil be true.
	 */
	public void setSunk(boolean didItSink){
		sunk = didItSink;
	}
	
	/**
	 * Basic get method.
	 * @return sunk
	 */
	public boolean isSunk(){
		return sunk;
	}
	
	/**
	 * Basic get method.
	 * @return type
	 */
	public String getType(){
		return type;
	}
	
	public int[][] getCoords(){
		return coords;
	}

	/**
	 * Increments the hit counter and changes ship to sunk if hits is enough.
	 */
	public void damageShip(){
		hits ++;
		sinkShip();
	}
	
	public int getHits(){
		return hits;
	}
	
	/**
	 * Changes value of sunk if the ship has aggregated enough hits to sink.
	 */
	public void sinkShip(){
		switch(type){
		
		case "Aircraft Carrier": if(hits >= 5){
			sunk = true;
		};
		break;
		
	case "Battleship": if(hits >= 4){
		sunk = true;
	};
		break;
		
	case "Submarine":
	case "Destroyer":
		if(hits >= 3){
			sunk = true;
		};
		break;
		
	case "Patrol Boat": if(hits >= 2){
		sunk = true;
	};
		break;
		}
	}
	
	/**
	 * Returns a string to be printed on the board.
	 * @return returnString Is the string returned.
	 */
	public String toString(){
		String returnString = "Error RETURNING SHIP";
		switch (type){
			
			case "Aircraft Carrier": returnString = "A";
				break;
				
			case "Battleship": returnString = "B";
				break;
				
			case "Submarine": returnString = "S";
				break;
				
			case "Destroyer": returnString = "D";
				break;
			case "Patrol Boat": returnString = "P";
				break;
			
		}
	return returnString;
	}
		
}
