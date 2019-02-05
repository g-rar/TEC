package com.example.lopez.picz.classes;

import android.graphics.Bitmap;

public class PiczBasicImage implements PiczImage {
    protected Bitmap image;

    public PiczBasicImage(Bitmap image) {
        this.image = image;
    }


    @Override
    public Bitmap getBitMap() {
        return image;
    }

    @Override
    public void setBitmap(Bitmap bm) {
        image = bm;
    }


}
