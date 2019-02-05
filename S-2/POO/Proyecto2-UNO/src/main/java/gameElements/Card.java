/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package gameElements;

/**
 *
 * @author lopez
 */
public class Card {
    
    private String symbol;
    private String color;

    public Card(String symbol, String color) {
        this.symbol = symbol;
        this.color = color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getColor() {
        return color;
    }
    
    public void setSymbol(String pSymbol){
        symbol = pSymbol;
    }
    
    public String getSymbol(){
        return symbol;
    }
    
    @Override
    public String toString(){
        return symbol + " " + color;
    }
}
