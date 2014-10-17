/*
* Author: Daniel Graham
* Purpose: CSC 300 Battleship Project
* Date: 10/1/14
*/
//package Battleship;

/**
 * This class contains the BoardSpace objects. These objects make up a board.
 * @author Daniel
 *
 */
public class BattleShipBoardSpace{
	private boolean containShip, previouslyHit;
	private char letter;
	private int num;
	private BattleShipShip shipWithinSpace;
	
	/**
	 * Constructor for a boardSpace. Z and 0 are dummy values.
	 */
	public BattleShipBoardSpace(){
		containShip = false;
		previouslyHit = false;
		letter = 'Z';
		num = 0;

	}
	
	/*
	 * These methods are very short, and most speak for themselves. 
	 * The board space is designed to be very simple,
	 * it is the most basic structure in the game.
	 */
	public void setBattleShipInSpace(BattleShipShip ship){
		shipWithinSpace = ship;
		containShip = true;
	}
	
	public BattleShipShip getBattleShipInSpace(){
		return shipWithinSpace;
	}
		
	public void setContainShip(boolean ship){
		containShip = ship;
	}
	
	public boolean getContainShip(){
		return containShip;
	}
	
	public void setPreviouslyHit(boolean hit){
		previouslyHit = hit;
		if(hitShip()){
			shipWithinSpace.damageShip();
		}
	}
	
	public boolean getPreviouslyHit(){
		return previouslyHit;
	}
	
	public boolean hitShip(){
		return previouslyHit && containShip;
	}
	
	public void setNum(int number){
		num = number;
	}
	
	public int getNum(){
		return num;
	}
	
	public void setLetter(char newLetter){
		letter = newLetter;
	}
	
	public char getLetter(){
		return letter;
	}
	
	/**
	 * Returns the space as a string to be printed with the board.
	 */
	public String toString(){
		String returnString = "";
		if(hitShip()){
			return "X";
		}
		else if(getPreviouslyHit()){
			return "O";
		}
		else if(letter != 'Z'){
			return returnString + letter;
		}
		else if(num != 0){
			return returnString + num;
		}
		else if(getContainShip()){
			return "" + shipWithinSpace;
		}
		else{
			return " ";
		}
	}
	
}
