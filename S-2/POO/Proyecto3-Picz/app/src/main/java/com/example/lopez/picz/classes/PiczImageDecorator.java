package com.example.lopez.picz.classes;

import android.graphics.Bitmap;

public abstract class PiczImageDecorator implements PiczImage {

    protected PiczImage image;

    public PiczImageDecorator(PiczImage pImg){
        image = pImg;
    }

    public void setBitmap(Bitmap bm){
        image.setBitmap(bm);
    }

    public Bitmap getBitMap(){
        return image.getBitMap();
    }

}
