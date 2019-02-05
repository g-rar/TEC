package com.example.lopez.picz.classes;

import android.graphics.Bitmap;
import android.graphics.Color;

public class PiczAbsoluteBWImage extends PiczImageDecorator implements PiczImage {

    public PiczAbsoluteBWImage(PiczImage pImg, float factor) {

        //El super tiene que ser la primera directiva, luego se saca el bitmap
        super(pImg);
        Bitmap imageBM = this.getBitMap();

        //Se hace una copia del bitmap que podemos modificar, si tratamos de
        //modificar la original nos tira una exception.

        Bitmap newImage = imageBM.copy(imageBM.getConfig(), true);

        //A continuacion, hacemos las modificaciones a la imagen para añadir el filtro
        for(int y = 0 ; y < newImage.getHeight(); y++ ){
            for (int x = 0; x < newImage.getWidth(); x++) {
                if(x%2==0){
                    int pixel = newImage.getPixel(x, y);
                    int r = (pixel & 0x00FF0000) >> 16;
                    int g = (pixel & 0x0000ff00) >> 8;
                    int b = (pixel & 0x000000FF);
                    int n = (r + g + b) / 3;

                    if(n>128){
                        newImage.setPixel(x, y, Color.WHITE);
                    }
                    else{
                        newImage.setPixel(x, y, Color.BLACK);
                    }
                }
            }
        }

        //Por ultimo establecemos el bitmap generado como el bitmap de todos.
        this.setBitmap(newImage);

    }
}
