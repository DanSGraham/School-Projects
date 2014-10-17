/*
* Author: Daniel Graham
* Purpose: CSC 300 Battleship Project
* Date: 10/1/14
*/
//package Battleship;


import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.regex.PatternSyntaxException;

/**
 * This class does the output of the game. It runs all the players together and keeps track of if a game has completed. 
 * Also sets up the boards and actually plays the game.
 * @author Daniel
 *
 */
public class BattleShipGame{
	
	private static final String TEXT_FILE_PATH = "C:\\Users\\Daniel\\Desktop\\BatmanBoard.txt";
	private BattleShipPlayer[] players;
	
	/**
	 * Constructor for the game. This actually also plays the game.
	 */
	public BattleShipGame(){
		Scanner inputScanner = new Scanner(System.in);
		players = new BattleShipPlayer[2];
		boolean playAgain = false;
		String gameType;
		boolean correctInputType;
		do{
			System.out.println("Would you like a one player game or a two player game?");
			gameType = inputScanner.nextLine();

			if(gameType.equals("one player")){
				correctInputType = true;
			}
			else if(gameType.equals("two player")){
				correctInputType = true;
			}
			else{
				System.out.println("Please enter either 'one player' or 'two player'.");
				correctInputType = false;
			}
			}while (!correctInputType);
		do{
			if(gameType.equals("one player")){
				setupOnePlayer(inputScanner, playAgain);
			}
			else if(gameType.equals("two player")){
				setupTwoPlayers(inputScanner, playAgain);
				twoPlayerPass(5);
			}
			int i = -1;
			int playerNum = i;
			boolean isWinner;
			do{
				i++;
				playerNum = i % 2;
				/*
				 * The following conditional checks if the player is facing an AI. If so, the AI must be cast and invoke a different playTurn method.
				 */
				if(players[playerNum] instanceof BattleShipAI){
					BattleShipAI aiPlayer = (BattleShipAI) players[playerNum];
					isWinner = aiPlayer.playTurn();
				}
				else{
					isWinner = players[playerNum].playTurn();
					if(gameType.equals("two player")){
						twoPlayerPass(5);
					}
				}
				}while(!isWinner);
			System.out.println(players[playerNum].getName() + " is the winner! Congrats!\n");
			System.out.print("Would you like to play again? ");
			String playString = inputScanner.nextLine();
			if((playString.equalsIgnoreCase("yes")) || (playString.equalsIgnoreCase("y"))){
				playAgain = true;
			}
			else{
				playAgain = false;
			}
			/*
			 * The following lines refresh the game for a successive playthrough.
			 */
			players[0].resetPlayer();
			players[1].resetPlayer();
			players[0].setOpponent(players[1]);
			players[1].setOpponent(players[0]);
		}while(playAgain);
		}
	
	/**
	 * Sets up a game for one player facing an AI.
	 * 
	 * @param inputScanner One scanner applies to the entire BattleshipGame.
	 * @param secondTime The method only invokes certain features if the game is being played more than once.
	 */
	public void setupOnePlayer(Scanner inputScanner, boolean secondTime){
		if(!secondTime){
			System.out.print("Please enter your name:");
			String playerName = inputScanner.nextLine();
			BattleShipPlayer player1 = new BattleShipPlayer(playerName);
			BattleShipAI computerPlayer = new BattleShipAI();
			players[0] = player1;
			players[1] = computerPlayer;
			player1.setOpponent(computerPlayer);
			computerPlayer.setOpponent(player1);
		}
		System.out.println(players[0].getName() + ", please setup your board.");
		System.out.print("Would you like to generate a random game board? ");
		String randomString = inputScanner.nextLine();
		if((randomString.equalsIgnoreCase("yes")) || (randomString.equalsIgnoreCase("y"))){
			players[0].generateRandomBoard();
		}
		else{
			for(int i = 0; i < 5; i++){
				players[0].readShipsFromConsole();
				System.out.println(players[0].getBattleShipBoard());
			}
		}
		if(!secondTime){
			players[1].readShipsToBoard(TEXT_FILE_PATH);
		}
		else{
			players[1].generateRandomBoard();
		}
	}
	
	/**
	 * Sets up a two player game. 
	 * @param inputScanner Scanner is conserved through the BattleShipGame.
	 * @param secondTime Method only uses certain features when invoked more than once.
	 */
	public void setupTwoPlayers(Scanner inputScanner, boolean secondTime){
		if(!secondTime){
			System.out.print("Please enter your name, Player 1: ");
			String player1Name = inputScanner.nextLine();
			System.out.print("Please enter your name, Player 2: ");
			String player2Name = inputScanner.nextLine();
			BattleShipPlayer player1 = new BattleShipPlayer(player1Name);
			BattleShipPlayer player2 = new BattleShipPlayer(player2Name);
			players[0] = player1;
			players[1] = player2;
			player1.setOpponent(player2);
			player2.setOpponent(player1);
		}
		System.out.println(players[0].getName() + ", please setup your board.");
		System.out.print("Would you like to generate a random game board? ");
		String randomString = inputScanner.nextLine();
		if((randomString.equalsIgnoreCase("yes")) || (randomString.equalsIgnoreCase("y"))){
			players[0].generateRandomBoard();
		}
		else{
			for(int i = 0; i < 5; i++){
				players[0].readShipsFromConsole();
				System.out.println(players[0].getBattleShipBoard());
			}
		}
		twoPlayerPass(5);
		System.out.println(players[1].getName() + ", please setup your board.");
		System.out.print("Would you like to generate a random game board? ");
		randomString = inputScanner.nextLine();
		if((randomString.equalsIgnoreCase("yes")) || (randomString.equalsIgnoreCase("y"))){
			players[1].generateRandomBoard();
		}
		else{
			for(int i = 0; i < 5; i++){
				players[1].readShipsFromConsole();
				System.out.println(players[1].getBattleShipBoard());
			}
		}
	}
	
	/**
	 * This allows for multiple players to play on the same screen. By giving time between turns, the players can trade off the laptop, 
	 * or who is looking at the screen. I found the sleep code at:http://stackoverflow.com/questions/3342651/how-can-i-delay-a-java-program-for-a-few-seconds
	 * 
	 * @param timeDelay Can be adjusted to shorten the time delay of between turns. Time in seconds.
	 */
	public void twoPlayerPass(int timeDelay){
		System.out.println("Opponent's board will appear in " + timeDelay * 2 + " seconds. Please do not peek!\n\n");
		try{
			Thread.sleep(1000 * timeDelay);
		}
		catch(InterruptedException e){
			Thread.currentThread().interrupt();
		}
		for(int i = 0; i < 50; i++){
			System.out.println("\n");
		}
		System.out.println("Opponent's board will appear in " + timeDelay + " seconds. Please do not peek!\n\n");
		try{
			Thread.sleep(1000 * timeDelay);
		}
		catch(InterruptedException e){
			Thread.currentThread().interrupt();
		}
	}
	
	/**
	 * Actually runs the game.
	 * @param args none
	 */
	public static void main(String[] args){
		
		new BattleShipGame();
	}
	
	
}	
