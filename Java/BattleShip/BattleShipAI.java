/*
* Author: Daniel Graham
* Purpose: CSC 300 Battleship Project
* Date: 10/1/14
*/

import java.util.*;

/**
 * This contains the AI which is an extension of the Player object. The AI is relatively smart.
 * @author Daniel
 *
 */
public class BattleShipAI extends BattleShipPlayer{
	Stack<int[]> huntStack;
	String pursueDirection;
	int[] huntCoords, lastKnownHit;
	boolean huntMode;
	boolean pursueMode;
	boolean hitShip;
	
	/**
	 * Constructor for the AI. Adds a few features from the Player.
	 */
	public BattleShipAI(){
		super("R2D2");
		huntStack = new Stack<int[]>();
		huntCoords = new int[2];
		lastKnownHit = new int[2];
		huntMode = false;
		pursueMode = false;
	}
	
	/**
	 * Plays a turn, however different from the Player object play turn. Since there is no user to input, the AI undergoes 3 phases. 
	 * 1. Random shooting. The AI tries to find a ship.
	 * 2. Once a ship is found, AI activates hunt phase. Fires on four spaces in a cross intersecting the last hit point.
	 * 3. When two spaces are adjacently hit, they form a path that the AI attacks until it reaches the end, a previously hit place,
	 * or does not hit a ship.
	 * 
	 * @return value Feedback if successful turn.
	 */
	public boolean playTurn(){
		int xCoord, yCoord;
		int[] totalCoord;
		boolean fireSuccess, hitShip;
		do{
		totalCoord = getNextCoord();
		xCoord = totalCoord[0];
		yCoord = totalCoord[1];
		fireSuccess = fire(xCoord, yCoord);
		if(pursueMode && !fireSuccess){
			pursueMode = false;
		}
		}while(!fireSuccess);
		hitShip = opponentBoard.getSpaceAt(xCoord, yCoord).getContainShip();
		if(pursueMode && !(hitShip)){
			pursueMode = false;
		}
		if(hitShip){
		    if(!pursueMode && !huntMode){
			    hunt(xCoord, yCoord);
		    }
		    else if(!pursueMode && huntMode){
		    	pursueMode = true;
		    	pursueDirection = getDirection(xCoord, yCoord);
		    }
		    if(pursueMode){
		    	pursueOffBoard(xCoord,yCoord);
		    }
		    setLastKnownHit(xCoord, yCoord);
		}
		if(huntStack.empty()){
			huntMode = false;
		}
		updateOpponentNumShipsLeft();
		checkWinner();
		return isWinner();
	}
	
	/**
	 * Checks if the pursue path is going to continue off the board and prevents it from continuing to shoot.
	 * 
	 * @param x Current x coordinate.
	 * @param y Current y coordinate.
	 */
	public void pursueOffBoard(int x, int y){
		if(x <= 1 && pursueDirection.equals("Left")){
			pursueMode = false;
		}
		else if(x >= 10 && pursueDirection.equals("Right")){
			pursueMode = false;
		}
		else if(y <= 1 && pursueDirection.equals("Up")){
			pursueMode = false;
		}
		else if(y >= 10 && pursueDirection.equals("Down")){
			pursueMode = false;
		}
	}
	
	/**
	 * Helper method for the pursue phase. Determines which direction a ship that has been hit twice is oriented and signals
	 * the pursue method to traverse that direction.
	 * 
	 * @param x Current X
	 * @param y Current Y
	 * @return value The direction to be passed to the pursue method.
	 */
	public String getDirection(int x, int y){
		int originX, originY;
		originX = huntCoords[0];
		originY = huntCoords[1];
		if( (x == originX) && (y == (originY - 1))){
			return "Up";
		}
		else if( (x == originX) && (y == (originY + 1))){
			return "Down";
		}
		else if( (x == (originX - 1)) && (y == originY)){
			return "Left";
		}
		else if( (x == (originX + 1)) && (y == originY)){
			return "Right";
		}
		return "ERROR";		
	}
	
	public BattleShipBoard getOpponentBoard(){
		return opponentBoard;
	}
	
	public boolean getHitShip(){
		return hitShip;
	}
	
	/**
	 * Sets a ship as hit and initiates the pursueMode.
	 * 
	 * @param toSet
	 */
	public void setHitShip(boolean toSet){
		hitShip = toSet;
		if(hitShip && huntMode){
			pursueMode = true;
		}
		else if(!hitShip && pursueMode){
			pursueMode = false;
		}
	}
	
	public boolean isHunting(){
		return huntMode;
	}
	
	public boolean isPursueing(){
		return pursueMode;
	}
	
	public void setHuntCoords(int x, int y){
		huntCoords[0] = x;
		huntCoords[1] = y;
	}
	public void setLastKnownHit(int x, int y){
		lastKnownHit[0] = x;
		lastKnownHit[1] = y;
	}
	
	public int[] getLastKnownHit(){
		return lastKnownHit;
	}
	
	/**
	 * This is the brunt of the AI. This method is called every turn, but it is in a different state depending on what ships it has hit.
	 * 
	 * @return target The coordinates to STRIKE!
	 */
	public int[] getNextCoord(){
		if(pursueMode){
			return pursue(pursueDirection);
		}
		else if(huntMode && (!huntStack.isEmpty())){
			int[] target = (int[]) huntStack.pop();
			return target;
		}
		else{
			Random rand = new Random();
			int[] target = {rand.nextInt(10) + 1, rand.nextInt(10) + 1};
			return target;
		}
	}
	
	/**
	 * The hunt method pushes the possible ship locations on a stack for use by the getNextCoord method.
	 * 
	 * @param x
	 * @param y
	 */
	public void hunt(int x, int y){
		int[] toUp = new int[2];
		int[] toDown = new int[2];
		int[] toLeft = new int[2];
		int[] toRight = new int[2];
		toUp[0] = x;
		toUp[1] = y - 1;
		toDown[0] = x;
		toDown[1] = y + 1;
		toLeft[0] = x - 1;
		toLeft[1] = y;
		toRight[0] = x + 1;
		toRight[1] = y;
		huntStack.push(toUp);
		huntStack.push(toDown);
		huntStack.push(toLeft);
		huntStack.push(toRight);
		lastKnownHit[0] = x;
		lastKnownHit[1] = y;
		huntMode = true;
		setHuntCoords(x,y);
	}
	/**
	 * The method called when in the pursue State. Traverses a direction until told to stop by helper method above.
	 * 
	 * @param direction Where to traverse
	 * @return pursueCoord The coordinates used in getNextCoord method.
	 */
	public int[] pursue(String direction){
		int[] pursueCoord = new int[2];
		int[] previousHit = getLastKnownHit();
		switch(direction){
		case "Up":
			pursueCoord[0] = previousHit[0];
			pursueCoord[1] = previousHit[1] - 1;
			break;
		case "Down":
			pursueCoord[0] = previousHit[0];
			pursueCoord[1] = previousHit[1] + 1;
			break;
		case "Right":
			pursueCoord[0] = previousHit[0] + 1;
			pursueCoord[1] = previousHit[1];
			break;
		case "Left":
			pursueCoord[0] = previousHit[0] - 1;
			pursueCoord[1] = previousHit[1];
			break;
		}
		return pursueCoord;
	}
	
	/**
	 * This method is different from the player reset because I have to also reset the board manually with clearBoard().
	 */
	public void resetPlayer(){
		huntStack = new Stack<int[]>();
		huntCoords = new int[2];
		lastKnownHit = new int[2];
		huntMode = false;
		pursueMode = false;
		clearBoard();
	}
	
}
	
