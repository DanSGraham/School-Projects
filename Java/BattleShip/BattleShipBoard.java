/*
* Author: Daniel Graham
* Purpose: CSC 300 Battleship Project
* Date: 10/1/14
*/
//package Battleship;


import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

/**
 * This class contains the board object. The board holds ship objects and consists of BoardSpaces. Players often interact with the board.
 * @author Daniel
 *
 */
public class BattleShipBoard{
	
	private BattleShipBoardSpace[][] board;
	private BattleShipShip[] ships;
	private int shipIndex;
	private static final int TOTALSHIPS = 5;
	
	/**
	 * Constructor for the board. Creates a blank board.
	 */
	public BattleShipBoard(){
		shipIndex = 0;
		board = new BattleShipBoardSpace[11][11];
		ships = new BattleShipShip[TOTALSHIPS];
		for(int i = 0; i < 11; i++){
			for(int j = 0; j < 11; j++){
				board[i][j] = new BattleShipBoardSpace();
				if (i > 0){
					board[i][0].setNum(i);
				}
				if (i == 0 && j > 0){
					board[0][j].setLetter((char) ((j-1)+'A')); //This loop sets the characters of the spaces using ascii code.
				}
			}
		}
	}

	/**
	 * Checks the board if ship object is already placed somewhere.
	 * 
	 * @param ship The ship to be tested if on board already.
	 * @return onBoard If the ship is already on Board = true.
	 */
	public boolean isShipOnBoard(BattleShipShip ship){
		boolean onBoard = false;
		for(int i = 0; i < ships.length; i++){
			if(ships[i] != null){
				if(ships[i].getType().equals(ship.getType())){
					onBoard = true;
				}
			}
		}
		return onBoard;
	}
	
	/**
	 * This method adds ships to the board. Only adds ships with already correct coordinates determined by higher up method, so does
	 * not need to handle edge cases.
	 * 
	 * @param shipToAdd The ship object to add to the board.
	 * @return value Feedback if the function was successful.
	 */
	public boolean addShip(BattleShipShip shipToAdd){  
		int[][] shipCoordinates = shipToAdd.getCoords();
		if(!isShipOnBoard(shipToAdd)){
		for(int i = 0; i < shipCoordinates[0].length; i++){
			board[shipCoordinates[1][i]][shipCoordinates[0][i]].setContainShip(true);
			board[shipCoordinates[1][i]][shipCoordinates[0][i]].setBattleShipInSpace(shipToAdd);
			}
		ships[shipIndex] = shipToAdd;
		shipIndex++;
		return true;
		}
		else{
			System.out.println(shipToAdd.getType() + " already on board");
			return false;
		}
	}
	
	/**
	 * Returns the BoardSpace at x,y.
	 * @param x
	 * @param y
	 * @return
	 */
	public BattleShipBoardSpace getSpaceAt(int x, int y){
		return board[y][x];
	}
	
	/**
	 * Checks if a space has been hit and if so, returns the ship hit.
	 * @param x
	 * @param y
	 * @return shipHit If the space at this coordinate has a ship and was hit, it returns the ship. Else it returns null.
	 */
	public BattleShipShip checkIfHit(int x, int y){
		//Maybe combine into fire.
		BattleShipShip shipHit;
		if(board[y][x].hitShip()){
			shipHit = board[y][x].getBattleShipInSpace();
			return shipHit;
		}
		else{
			return null;
		}
	}
	
	/**
	 * Gets the ship at a certain location. Ship must be in space to return it.
	 * @param x
	 * @param y
	 * @return shipInSpace At board x,y.
	 */
	public BattleShipShip getShipAt(int x, int y){
		return board[y][x].getBattleShipInSpace();
	}

	
	public BattleShipShip[] getShipsOnBoard(){
		return ships;
	}
	
	/**
	 * Converts a board object into a string with characters instead of ships.
	 */
	public String toString(){
		int number;
		boolean isHit;
		char letter;
		//Stringbuilder.
		String printString = "  ";
		for(int i = 0; i < 11; i++){
			for(int j = 0; j < 11; j++){
				letter = board[i][j].getLetter();
				number = board[i][j].getNum();
				isHit = board[i][j].getPreviouslyHit();
				if(letter != 'Z'){
					printString += letter;
				}
				else if(number != 0 && number < 10){
					printString += "  " + number;
				}
				else if(number == 10){
					printString += " " + number;
				}
				else if(isHit){
					if(board[i][j].hitShip()){
						printString += 'X';
					}
					else{
						printString += 'O';
					}
				}
				else if (board[i][j].getContainShip()){
					printString += board[i][j].getBattleShipInSpace();
				}
				else{
					printString += " ";
				}
			}
			printString += '\n';
		}
		return printString;
	}
	
}
	
	
