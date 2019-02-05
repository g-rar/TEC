/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package game;

import gameElements.Card;
import java.util.HashMap;

/**
 *
 * @author lopez
 */
public class GameRules {
    
    private String[] Symbols;//cards of the game
    private char[] Quantities; //amount of cards per color 
    private String[] Colors;
    private GameTable table;
    private HashMap<String, Runnable> gameMoves;
    
    
    public GameRules(GameTable pTable){
        this.Symbols = new String[]{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "t", "r", "s", "w", "f"};
        this.Quantities = new char[]{ 1,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,   1,   1};
        this.Colors = new String[]{"Rojo", "Verde", "Azul", "Amarillo"};
        table = pTable;
        gameMoves = new HashMap<>();
        gameMoves.put("t", () -> takeTwo());
        gameMoves.put("r", () -> reverse());
        gameMoves.put("s", () -> skipTurn());
        gameMoves.put("w", () -> wildCard());
        gameMoves.put("f", () -> wildTakeFour());
    }

    public String[] getSymbols() {
        return Symbols;
    }

    public char[] getQuantities() {
        return Quantities;
    }

    public String[] getColors() {
        return Colors;
    }
    
    public boolean validPlay(Card pCard){
        boolean returnValue = false;
        Card last = table.lastCard;
        if(last.getColor().equals(pCard.getColor()) | last.getSymbol().equals(pCard.getSymbol()) |
                pCard.getSymbol().equals("w") | pCard.getSymbol().equals("f")){
            returnValue = true;
        }
        return returnValue;
    }
    
    public void playCard(Card pCard){
        if(gameMoves.containsKey(pCard.getSymbol())){
            gameMoves.get(pCard.getSymbol()).run();
        }
    }
    
    public void takeTwo(){
        table.turnPlayer.drawCard(table.deck.drawCard());
        table.turnPlayer.drawCard(table.deck.drawCard());
        skipTurn();
    }
    
    public void skipTurn(){
        table.nextTurn();
    }

    private void reverse() {
        table.rotation = ! table.rotation;
    }

    private void wildCard() {
        String newColor = table.gameinterface.getColorChange();
        table.lastCard.setColor(newColor);
    }

    private void wildTakeFour() {
        wildCard();
        table.turnPlayer.drawCard(table.deck.drawCard());
        table.turnPlayer.drawCard(table.deck.drawCard());
        takeTwo();
    }

    
}
