package gameElements;

import java.util.ArrayList;
import java.util.List;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author lopez
 */
public class Player {
    private List<Card> mano;
    private String Id;
    
    public Player(String Id){
        this.Id = Id;
        this.mano = new ArrayList<Card>();
    }

    public void setId(String Id) {
        this.Id = Id;
    }

    public String getId() {
        return Id;
    }
    
    public void setMano(List<Card> mano) {
        this.mano = mano;
    }

    public List<Card> getMano() {
        return mano;
    }

    public void drawCard(Card pCard){
        this.mano.add(pCard);
    }
    
    public Card playCard(Card pCard){
        Card returnValue = null;
        for(int i = 0 ; i < mano.size() ; i++){
            if(mano.get(i).equals(pCard)){
                returnValue = mano.remove(i);
            }
        }
        return returnValue;
    }
}
