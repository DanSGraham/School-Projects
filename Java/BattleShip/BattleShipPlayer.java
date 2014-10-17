/*
* Author: Daniel Graham
* Purpose: CSC 300 Battleship Project
* Date: 10/1/14
*/
//package Battleship;

import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;

/**
 * This class contains the Player objects. Players have many complex methods, such as fire, takeTurn,
 *  and inputShips. This is the main acting class in the game. Players do a majority of the action.
 * @author Daniel
 *
 */
public class BattleShipPlayer{
	boolean winner;
	BattleShipBoard playersBoard;
	int numShipsLeft;
	String playerName;
	BattleShipPlayer opponent;
	BattleShipBoard opponentBoard;
	
	/**
	 * Constructor for Player.
	 * 
	 * @param inputPlayerName The string that will be the players name.
	 */
	public BattleShipPlayer(String inputPlayerName){
		playerName = inputPlayerName;
		winner = false;
		playersBoard = new BattleShipBoard();
		numShipsLeft = 5;
	}
	
	public String getName(){
		return playerName;
	}
	
	/**
	 * Checks if winner.
	 * 
	 * @return value 
	 */
	public boolean isWinner(){
		return winner;
	}
	
	/**
	 * Initializes the opponent for a player and the opponentBoard variable.
	 * 
	 * @param opponentToSet The opponent of whichever player this is. Both players must set each other as opponents.
	 */
	public void setOpponent(BattleShipPlayer opponentToSet){
		opponent = opponentToSet;
		opponentBoard = opponent.getBattleShipBoard();
	}
	
	/**
	 * Sets winner.
	 * @param isWinner
	 */
	public void setWinner(boolean isWinner){
		winner = isWinner;
	}
	
	/**
	 * Fires on the opponentsBoard. Checks for the coordinates to be correct and then changes Ship, and/or BoardSpaces on opponentsBoard.
	 * Also gives some output on what kind of a shot it was.
	 * 
	 * @param x Horizontal coordinate of target.
	 * @param y Vertical coordinate of target.
	 * @return value The value is to determine whether the shot could be placed correctly or not. If not, the user may try again.
	 */
	public boolean fire(int x, int y){
		if(x > 10 || y > 10 || x < 1 || y < 1){
			System.out.println("You cannot fire outside of the board!");
			return false;
		}
		BattleShipBoardSpace poFireSpace = opponentBoard.getSpaceAt(x, y);
		if(poFireSpace.getPreviouslyHit()){
			System.out.println("You already fired on that location!");
			return false;
		}
		else{
			poFireSpace.setPreviouslyHit(true);
			if(poFireSpace.getContainShip()){
				BattleShipShip shipDamaged = poFireSpace.getBattleShipInSpace();
				if(shipDamaged.isSunk()){
					System.out.println("You sunk " + opponent.getName() + "'s " + shipDamaged.getType() + "!");
				}
				else{
					System.out.println("You hit " + opponent.getName() + "'s " + shipDamaged.getType() + "!");
				}
			}
			else{
				System.out.println(playerName + " missed!");
			}
			return true;
		}
	}
		
	/**
	 * This method is useful for preparing the board for subsequent games. Completely wipes the current board and instantiates a new
	 * board which is blank.
	 */
	public void clearBoard(){
		playersBoard = new BattleShipBoard();
	}
	
	/**
	 * This is used to update the opponents ships list after a successful sinking. 
	 */
	public void updateOpponentNumShipsLeft(){
		BattleShipShip[] totalShips = opponentBoard.getShipsOnBoard();
		int shipsLeft = 0;
		for (int i = 0; i < totalShips.length; i++){
			if(!(totalShips[i].isSunk())){
				shipsLeft ++;
			}
			}
		opponent.setNumShipsLeft(shipsLeft);
	}
	
	/**
	 * Used mainly in the updateOpponentNumShipsLeft method. Sets value of numShipsLeft.
	 * @param totalShipsLeft Given by the updateOpponentNumShipsLeft method.
	 */
	public void setNumShipsLeft(int totalShipsLeft){
		numShipsLeft = totalShipsLeft;
	}
	
	/**
	 * Must be called after every turn in conjunction with updateOpponentNumShipsLeft() in order to accurately determine end of game.
	 */
	public void checkWinner(){
		if(opponent.numShipsLeft <= 0){
			winner = true;
		}
	}
	
	public BattleShipBoard getBattleShipBoard(){
		return playersBoard;
	}
	
	/**
	 * Reads a text file, formatted correctly (I have included an example), to the board. Initializes all ships and adds them after determining their 
	 * coordinates.
	 * 
	 * @param shipTextFile File which must be formatted correctly. The file must have spaces filling to at least the J column. More spaces will not hurt.
	 * @return value Gives feedback if the method was successful.
	 */
	public boolean readShipsToBoard(String shipTextFile){ 
			BattleShipShip AirC, Destroyer, Sub, PatrolBoat, BS;
			/*
			 * The following boolean variables help determine if adding to the board was successful.
			 */
			boolean success = true;
			boolean coordsSuccess = true;
			boolean addSuccess = true;
			AirC = new BattleShipShip("Aircraft Carrier");
			BS = new BattleShipShip("Battleship");
			Destroyer = new BattleShipShip("Destroyer");
			Sub = new BattleShipShip("Submarine");
			PatrolBoat = new BattleShipShip("Patrol Boat");
			try{
			File file = new File(shipTextFile);
			Scanner shipFile = new Scanner(file);
			int rowNum = 0;
			while(shipFile.hasNextLine()){
				String inputLine = shipFile.nextLine();
				if (inputLine.charAt(0) != ' '){ //This skips the first line which contains identifying letters.
					for (int columnNum = 1; columnNum < 11; columnNum++){ //If no spaces filling the board, will throw an index out of bounds exception.
						char shipChar = inputLine.charAt(columnNum);
						switch(shipChar) {
							case 'A':
								coordsSuccess = AirC.setCoords(columnNum, rowNum);
								
							break;
							
							case 'B':
								coordsSuccess = BS.setCoords(columnNum, rowNum);
								
							break;
							
							case 'D':
								coordsSuccess = Destroyer.setCoords(columnNum, rowNum);
	
							break;
							
							case 'S':	
								
								coordsSuccess = Sub.setCoords(columnNum, rowNum);

							break;
							
							case 'P':
								
								coordsSuccess = PatrolBoat.setCoords(columnNum, rowNum);
							
							break;
						}
						if(!coordsSuccess){
							success = false;
						}
					}
				}
				rowNum++;		
			}
			shipFile.close();
			addSuccess = playersBoard.addShip(AirC);
			if(!addSuccess){
				success = false;
			}
			addSuccess = playersBoard.addShip(BS);
			if(!addSuccess){
				success = false;
			}
			addSuccess = playersBoard.addShip(Destroyer);
			if(!addSuccess){
				success = false;
			}
			addSuccess = playersBoard.addShip(Sub);
			if(!addSuccess){
				success = false;
			}
			addSuccess = playersBoard.addShip(PatrolBoat);
			if(!addSuccess){
				success = false;
			}
			return success;
			}
			catch (FileNotFoundException e){
				System.out.println(e);
				return false;
			}
		}
	
	/**
	 * This is a helper method for the readShipsFromConsole method. Ensures that user input is valid and can be translated
	 * to useful coordinates later.
	 * 
	 * @param inputs A two item array with the x coordinate as inputs[0] and y coordinate as inputs[1]
	 * @return incorrectInput To check if the input is correct. If coordinates are not correct/valid returns false.
	 */
	public boolean checkCoordinateInput(String[] inputs){
		int startXCoord, startYCoord;
		boolean incorrectInput = false;
		switch(inputs[0]){
		case "A":
			startXCoord = 1;
			break;
		case "B":
			startXCoord = 2;
			break;
		case "C":
			startXCoord = 3;
			break;
		case "D":
			startXCoord = 4;
			break;
		case "E":
			startXCoord = 5;
			break;
		case "F":
			startXCoord = 6;
			break;
		case "G":
			startXCoord = 7;
			break;
		case "H":
			startXCoord = 8;
			break;
		case "I":
			startXCoord = 9;
			break;
		case "J":
			startXCoord = 10;
			break;
		default:
			incorrectInput = true;
			System.out.println("Your first coordinate is invalid. Please try again.");
			break;
			}
		try{
			startYCoord = Integer.parseInt(inputs[1]);
		}
		catch(NumberFormatException e){
			incorrectInput = true;
			System.out.println("Your second coordinate is invalid. Please try again");
		}
		catch(IndexOutOfBoundsException f){
			System.out.println("Your coordinates are invalid. Please try again");
			incorrectInput = true;
		}
		return incorrectInput;
	}
	
	/**
	 * Helper method for readShipsFromConsole method. Add ships in any available direction, instead of at each coordinate.
	 * 
	 * @param x Horizontal coordinate of start point.
	 * @param y Vertical coordinate of start point.
	 * @param shipToAdd Ship object that will be added to the board with this method.
	 * @param direction Indicates which available direction the ship will be placed along on the baord.
	 */
	public void addShipDirectional(int x, int y, BattleShipShip shipToAdd, String direction){
		int pathLength = shipToAdd.getLength();
		/*
		 * The following switch statement converts from a direction
		 *  to actual coordinates and sets the ship to those coordinates
		 */
		switch(direction){
		case "Up":
			for(int i = 0; i < pathLength; i++){
					shipToAdd.setCoords(x, y - i);
			}
			playersBoard.addShip(shipToAdd);
			break;
		case "Down":
			for(int i = 0; i < pathLength; i++){
					shipToAdd.setCoords(x, y + i);
				}
			playersBoard.addShip(shipToAdd);
			break;
		case "Left":
			for(int i = 0; i < pathLength; i++){
					shipToAdd.setCoords(x - i, y);
				}
			playersBoard.addShip(shipToAdd);
			break;
		case "Right":
			for(int i = 0; i < pathLength; i++){
					shipToAdd.setCoords(x + i, y);
				}
			playersBoard.addShip(shipToAdd);
			break;
		}
	}
	
	/**
	 * Helper to readShipsFromConsole method. Ensures that the initial coordinates are valid to place a ship.
	 * The initial coordinates must not have a ship in them and must have a path to place the ship on.
	 * 
	 * @param x Horizontal coordinate of initial placement.
	 * @param y Vertical coordinate of initial placement
	 * @param shipToCheck Ship object to place on the board.
	 * @return validDirections A list of possible directions to be used in addShipDirectional method.
	 */
	public String[] checkStartCoordinates(int x, int y, BattleShipShip shipToCheck){
		String[] validDirections = {"Valid","Not Valid", "Not Valid", "Not Valid"};
		boolean validCoords = shipToCheck.setCoords(x, y);
		if(!validCoords){
			validDirections[0] = "Not Valid";
		}
		else{
			BattleShipBoardSpace poSpace = playersBoard.getSpaceAt(x, y);
			if(poSpace.getContainShip()){
				validDirections[0] = "Not Valid";
				System.out.println("This coordinate already contains your " + poSpace.getBattleShipInSpace().getType());
			}
		}
		if(validDirections[0] != "Not Valid"){
			validDirections = checkDirection(x, y, shipToCheck);
		}
			return validDirections;
	}
	
	/**
	 *Helper to readShipsFromConsole method.
	 * Checks if the potential path to place a ship is clear of obstacles and is on the board.
	 * 
	 * @param x Horizontal coordinate of potential ship starting position.
	 * @param y Vertical coordinate of potential ship starting position.
	 * @param pathSize Equal to the length of ship which will be placed on the path. 
	 * @param direction Determined by the checkDirection method
	 * @return value To give feedback on if the path is clear. If not, it will not be a possible path
	 * 				 to place a ship.
	 */
	public boolean isClear(int x, int y, int pathSize, String direction){
		switch(direction){
		case "Up":
			for(int i = 0; i < pathSize; i++){
				if(y - i >= 11 || y - i <= 0){
					return false;
				}
				BattleShipBoardSpace poSpace = playersBoard.getSpaceAt(x, y - i);
				if(poSpace.getContainShip()){
					return false;
				}
			}
			return true;
		case "Down":
				for(int i = 0; i < pathSize; i++){
					if(y + i >= 11 || y + i <= 0){
						return false;
					}
						BattleShipBoardSpace poSpace = playersBoard.getSpaceAt(x, y + i);
						if(poSpace.getContainShip()){
							return false;
						}
					}
				return true;
		case "Left":
				for(int i = 0; i < pathSize; i++){
					if(x - i >= 11 || x - i <= 0){
						return false;
					}
						BattleShipBoardSpace poSpace = playersBoard.getSpaceAt(x - i, y);
						if(poSpace.getContainShip()){
							return false;
						}
					}
				return true;
		case "Right":
				for(int i = 0; i < pathSize; i++){
					if(x + i >= 11 || x + i <= 0){
						return false;
					}
						BattleShipBoardSpace poSpace = playersBoard.getSpaceAt(x + i, y);
						if(poSpace.getContainShip()){
							return false;
						}
					}
				return true;
		default:
			return false;
		}
	}
	
	/**
	 * Helper method to readShipsFromConsole method. Looks for things in the way of a ship using the isClear method.
	 *
	 * @param startX Initial x coordinate of ship front.
	 * @param startY Initial y coordinate of ship front.
	 * @param shipToTry Ship object to place on board.
	 * @return validDirections[] A list of possible directions. Some items are "Not Valid" but are ignored in later methods.
	 */
	public String[] checkDirection(int startX, int startY, BattleShipShip shipToTry){
		String[] validDirections = {"Up", "Down", "Left", "Right"};
		int shipLength = shipToTry.getLength();
		for(int i = 0; i < validDirections.length; i++){
			if(!(isClear(startX, startY, shipLength, validDirections[i]))){
				validDirections[i] = "Not Valid";
			}
		}
		return validDirections;
	}
	
	/**
	 * Helper method for readShipsToBoard method. Confirms that the user actually entered a ship from the list.
	 * 
	 * @param shipToTry A ship object instantiated to a possibly incorrect type.
	 * @return shipCorrect Give feedback about whether method was correct.
	 */
	public boolean checkShipInput(BattleShipShip shipToTry){
		String[] shipsList = {"Aircraft Carrier", "Battleship", "Destroyer","Submarine", "Patrol Boat"};
		boolean shipCorrect = false;
		for(int i = 0; i < shipsList.length; i++){
			if(shipToTry.getType().equals(shipsList[i])){
				shipCorrect = true;
			}
		}
		return shipCorrect;
	}
	
	/**
	 * Helper method to readShipsToBoard method. Ensures that a ship being added is not already on the board.\
	 * 
	 * @param shipToTry A ship object that may be incorrect.
	 * @return alreadyOnBoard Give user feedback on where the input was problematic.
	 */
	public boolean shipAlreadyOnBoard(BattleShipShip shipToTry){
		boolean alreadyOnBoard = false;
		BattleShipShip[] shipsOnBoard = playersBoard.getShipsOnBoard();
		for(int j = 0; j < shipsOnBoard.length; j++){
			if (shipsOnBoard[j] != null){
				if(shipToTry.getType().equals(shipsOnBoard[j].getType())){
					alreadyOnBoard = true;
					System.out.println("You have already placed your " + shipToTry.getType() + ". Please place a different ship");
				}
			}
		}
		return alreadyOnBoard;
	}
	
	/**
	 * Reads user input from console to add one ship to board. Uses above helpers to specify correct input.
	 */
	public void readShipsFromConsole(){
		int startXCoord, startYCoord;
		String[] shipsList = {"Aircraft Carrier", "Battleship", "Destroyer","Submarine", "Patrol Boat"};
		Scanner shipsScanner = new Scanner(System.in);
		String ship;
		BattleShipShip shipToAdd;
		boolean isInputCorrect;
		boolean isOnBoard;
		do {
			System.out.print("Which ship would you like to place? (Aircraft Carrier, Battleship, Destroyer, Submarine, or Patrol Boat)");
			ship = shipsScanner.nextLine();
			shipToAdd = new BattleShipShip(ship);
			isInputCorrect = checkShipInput(shipToAdd);
			isOnBoard = shipAlreadyOnBoard(shipToAdd);
		}while((!isInputCorrect) || (isOnBoard));
		boolean incorrectCoords = false;
		boolean incorrectInput = true;
		boolean noPath = false;
		String directionString;
		String[] coords;
		String [] poDirections;
		int numPaths;
		//The following nested loops make me wish for a GOTO.
		do{ //I would GOTO here...
			directionString = "";
			numPaths = 0;
			do{  //Remove this do loop...
			System.out.print("Please enter the coordinates of the front of your " + ship + ".(ex. A,1)");
			String usrInput = shipsScanner.nextLine();
			coords = usrInput.split(",");
			incorrectInput = checkCoordinateInput(coords);
			}while(incorrectInput); //One GOTO would be from here...
			char tempInput = coords[0].charAt(0);
			startXCoord = tempInput - 'A' + 1;
			startYCoord = Integer.parseInt(coords[1]);
			poDirections = checkDirection(startXCoord, startYCoord, shipToAdd);
			for(int i = 0; i < poDirections.length; i++){
				if(poDirections[i].equals("Up") || poDirections[i].equals("Down") || poDirections[i].equals("Left") || poDirections[i].equals("Right")){
					numPaths ++;
					directionString += poDirections[i] + " ";
				}
			}
			if (numPaths <= 0){
				System.out.println("Your ship will not fit here!"); //The other GOTO would go here. Both would GOTO the place mentioned above. Having them removes the need for two loops.
			}
		}while(numPaths <= 0);
		boolean isCorrectDirectionInput;
		String shipDirection;
		do{
		System.out.println("Which direction will the tail of your ship point from the starting coordinate? " + directionString);
		shipDirection = shipsScanner.nextLine();
		isCorrectDirectionInput = false;
		for(int j = 0; j < poDirections.length; j++){
			if(shipDirection.equals(poDirections[j])){
				isCorrectDirectionInput = true;
			}
		}
		if(!isCorrectDirectionInput){
			System.out.println("Please select one of the available directions");
		}
		}while(!isCorrectDirectionInput);
		addShipDirectional(startXCoord, startYCoord, shipToAdd, shipDirection);
		
	}
	
	
	/**
	 * Prints both your and opponent boards side by side with the opponent board not showing his boats.
	 */
	public void printBothBoards(){
		String printString = "   Your board      Opponent's board  \n\n";
		for(int i = 0; i < 11; i++){
			String ownLine = "";
			String enemyLine = "";
			if(i < 10){
				printString += "  ";
			}
			else{
				printString += " ";
			}
			for(int j = 0; j < 11; j++){
				String enemySpace = "" + opponentBoard.getSpaceAt(j, i);
				if(i > 0){
					/*
					 * The following conditional converts the opponent ship icons into blank spaces visually.
					 */
				if(enemySpace.equals("A") || enemySpace.equals("B") || enemySpace.equals("D") || enemySpace.equals("S") || enemySpace.equals("P")){
					enemySpace = " ";
				}
				}
				ownLine += playersBoard.getSpaceAt(j, i);
				enemyLine += enemySpace;
				}
			if(i < 10){
			printString += ownLine + "       " + enemyLine + "\n";
			}
			else{
				printString += ownLine + "      " + enemyLine + "\n";
			}

		}
		System.out.println(printString);
	}
	
	/**
	 * This method is based off of the readShipsFromConsole method, but does not rely on user input. It was primarily developed for the AI to use,
	 * but lazy gamers can use it too.
	 */
	public void generateRandomBoard(){
		Random rand = new Random();
		for(int i = 0; i < 5; i++){
			int startXCoord, startYCoord;
			String[] shipsList = {"Aircraft Carrier", "Battleship", "Destroyer","Submarine", "Patrol Boat"};
			String ship = shipsList[i];
			BattleShipShip shipToAdd;
			shipToAdd = new BattleShipShip(ship);
			String [] poDirections;
			int numPaths;
			//This is an example of where in intuitively want a goto statement. 
			do{
				numPaths = 0;
				startXCoord = rand.nextInt(10) + 1;
				startYCoord = rand.nextInt(10) + 1;
				poDirections = checkDirection(startXCoord, startYCoord, shipToAdd);
				for(int j = 0; j < poDirections.length; j++){
					if(poDirections[j].equals("Up") || poDirections[j].equals("Down") || poDirections[j].equals("Left") || poDirections[j].equals("Right")){
						numPaths ++;
					}
				}
			}while(numPaths <= 0);
			String shipDirection;
			do{
				shipDirection = poDirections[rand.nextInt(4)];
			}while(shipDirection.equals("Not Valid"));
			addShipDirectional(startXCoord, startYCoord, shipToAdd, shipDirection);
			}
	}
	
	
	/**
	 * This is where the player actually takes his turn. He fires and the game checks if he has won.Also has fairly strict console input requirements.
	 * @return value Gives feedback on if the turn just played ended the game.
	 */
	public boolean playTurn(){
		//Returns whether the game is over.
			Scanner fireScanner = new Scanner(System.in);
			boolean inputCorrect;
			boolean fireSuccess;
			int xCoord, yCoord;
			printBothBoards();
			do{
				xCoord = 0;
				yCoord = 0;
				do{
					inputCorrect = true;
					System.out.print(getName() + ", where would you like to fire? (ex D,4):");
					String fireString = fireScanner.nextLine();
					try{
					String[] fireCoordsString = fireString.split(",");
					char xCoordChar = fireCoordsString[0].charAt(0);
					xCoord = xCoordChar - 'A' + 1;
					yCoord = Integer.parseInt(fireCoordsString[1]);
					}
					catch(IndexOutOfBoundsException e){
						inputCorrect = false;
						System.out.println("Something is wrong with your input. Make sure you remembered the comma!");
					}
					catch(NumberFormatException a){
						inputCorrect = false;
						System.out.println("Something is wrong with your input. Did you enter a positive integer for the second coordinate value?");
					}	
					}while(!inputCorrect);
				fireSuccess = fire(xCoord, yCoord);
				}while(!fireSuccess);
				updateOpponentNumShipsLeft();
				checkWinner();
				return isWinner();
	}
	
	/**
	 * Allows for the game to reset if the player chooses to play again. Refreshes all values for the player object to default.
	 */
	public void resetPlayer(){
		winner = false;
		playersBoard = new BattleShipBoard();
		numShipsLeft = 5;
	}

}



		
		
		
