package com.example.lopez.picz.classes;

import android.graphics.Bitmap;

public class PiczBWImage extends PiczImageDecorator implements PiczImage {

    public PiczBWImage(PiczImage pImg, float factor) {

        //El super tiene que ser la primera directiva, luego se saca el bitmap
        super(pImg);
        Bitmap imageBM = this.getBitMap();

        //Se hace una copia del bitmap que podemos modificar, si tratamos de
        //modificar la original nos tira una exception.

        Bitmap newImage = imageBM.copy(imageBM.getConfig(), true);

        //A continuacion, hacemos las modificaciones a la imagen para añadir el filtro
        for(int y = 0 ; y < newImage.getHeight(); y++ ){
            for (int x = 0; x < newImage.getWidth(); x++) {
                int pixel = newImage.getPixel(x, y);
                int r = (pixel & 0x00FF0000) >> 16;
                int g = (pixel & 0x0000ff00) >> 8;
                int b = (pixel & 0x000000FF);
                int n = (r + g + b) / 3;
                int rr = n + (int) ((r - n) * factor);
                int gg = n + (int) ((g - n) * factor);
                int bb = n + (int) ((b - n) * factor);
                int result = (pixel & 0xFF000000) | (rr << 16) | (gg << 8) | bb;
                newImage.setPixel(x, y, result);

            }
        }

        //Por ultimo establecemos el bitmap generado como el bitmap de todos.
        this.setBitmap(newImage);

    }
}
