/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package game;

import gameElements.Card;
import gameElements.Deck;
import gameElements.Player;
import java.util.List;
import tda.CircularList;

/**
 *
 * @author lopez
 */
public class GameTable {
    protected static final GameTable instance = new GameTable();
    protected boolean started;
    protected Card lastCard;
    protected CircularList<Player> jugadores;
    protected Player turnPlayer;
    protected boolean rotation;
    protected Deck deck;
    protected IUNOGameInterface gameinterface;
    private GameRules gameRules;
    
    private GameTable(){
        started = false;
        lastCard = null;
        jugadores = new CircularList<Player>();
        turnPlayer = null;
        rotation = false;
        deck = null;
        gameRules = new GameRules(this);
    }
    
    public static GameTable getInstance(IUNOGameInterface gameInterface){
        return instance;
    }
    
    public int getNPlayers(){
        return jugadores.getSize();
    }
    
    public String[] getPlayers(){
        int jsize = jugadores.getSize();
        String[] retValue = new String[jsize];
        for (int i = 0; i < jsize ; i++) {
            retValue[i] = jugadores.getValue(i).getId();
        }
        return retValue;
    }
    
    public String getTurnPlayer(){
        return jugadores.getValue(0).getId();
    }
    
    public String getNextTurnPlayer(){
        int value = rotation ? jugadores.getSize() : 1 ;
        return jugadores.getValue(value).getId();
    }
    
    public void setInterface(IUNOGameInterface punointerface){
        gameinterface = punointerface;
    }
    
    public boolean isStarted(){
        return started;
    }
    
    public String[] getCards(String playerID){
        String[] cartasStr = null;
        List<Card> cartas;
        for (int i = 0; i < jugadores.getSize(); i++) {
            Player player = jugadores.getValue(i);
            if(player.getId().equals(playerID)){
                cartas = player.getMano();
                cartasStr = new String[cartas.size()];
                for (int j = 0; j < cartasStr.length; j++) {
                    cartasStr[j] = cartas.get(j).toString();
                }
                break;
            }
            
        }
        return cartasStr;
    }
    
    public boolean isPlaying(String playerID){
        for (int i = 0 ; i < jugadores.getSize() ; i++){
            if(jugadores.getValue(i).getId().equals(playerID)){
                return true;
            }
        }
        return false;
    }
    
    public void joinPlayer(String playerID){
        if (!(started | isPlaying(playerID))) jugadores.add(new Player(playerID));
    }
    
    public void startGame(){
        if(started) return;
        deck = new Deck(jugadores.getSize(), 
                gameRules.getSymbols(), 
                gameRules.getQuantities(), 
                gameRules.getColors());
        for(int i = 0 ; i < jugadores.getSize() ; i++){
            for(int j = 0 ; j < 7 ; j++){
                jugadores.getValue(i).drawCard(deck.drawCard());
            }
        }
        lastCard = deck.drawCard();
        jugadores.scramble(10);
        turnPlayer = jugadores.getValue(0);
        started = true;
    }
    
    public void nextTurn(){
        jugadores.rotate(1, rotation);
        turnPlayer = jugadores.getValue(0);
    }
    
    public void playCard(Card pCard, String pPlayerID){
        if(gameRules.validPlay(pCard) & pPlayerID.equals(turnPlayer.getId())){
            System.out.println("**************** " + turnPlayer.getId() + " l: " + lastCard.toString() + " n:" + pCard.toString());
            lastCard = pCard;
            turnPlayer.playCard(pCard);
            nextTurn();
            gameRules.playCard(pCard);
        }
    }
    
    public String getGameState(){
        if(! started)
            return "not started";
        String lastCardStr = lastCard.toString();
        String turnPlayerStr = turnPlayer.getId();
        String playersStr = "";
        for(int i = 0 ; i < jugadores.getSize() ; i++){
            Player jug = jugadores.getValue(i);
            String playerStr = jug.getId() + ": [";
            playerStr += jug.getMano().get(0).toString();
            
            for( int j = 1 ; j < jug.getMano().size() ; j++ ){
                playerStr +=  ",\n " + jug.getMano().get(j).toString();
            }
            
            playersStr += playerStr + "] ,\n";
        }
        playersStr = playersStr.substring(0, playersStr.length() - 3);
        String result = "{turnPlayer: " + turnPlayerStr + "\n"
                + "lastCard : " + lastCardStr + ", \n"
                + "players: [" + playersStr + " ]\n" + "}";
        return result;
    }
    
    
}
