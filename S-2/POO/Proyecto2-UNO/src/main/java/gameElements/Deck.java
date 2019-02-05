/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package gameElements;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 *
 * @author lopez
 */
public class Deck {
    List<Card> deck;

    public Deck(int numberOfPlayers, String[] pSymbols, char[] pQuantities, String[] pColors){
        deck = new ArrayList<Card>();
        int decksToMake = (numberOfPlayers / 10) + 1;
        
        for(int i = 0 ; i < decksToMake ; i++){
            for(String color: pColors){
                for(int j = 0 ; j < pSymbols.length ; j++){
                    for(int w = 0 ; w < pQuantities[j]; w++){
                        Card newCard = new Card(pSymbols[j], color);
                        deck.add(newCard);
                    }
                }
            }
        }
    }
    
    public boolean isEmpty(){
        return deck.isEmpty();
    }
    
    public void setDeck(List<Card> deck) {
        this.deck = deck;
    }

    public List<Card> getDeck() {
        return deck;
    }
    
    public Card drawCard(){
        Random rand = new Random();
        int n = rand.nextInt(deck.size());
        return deck.remove(n);
    }
    
    public void addCard(Card pCard){
        deck.add(pCard);
    }
}
