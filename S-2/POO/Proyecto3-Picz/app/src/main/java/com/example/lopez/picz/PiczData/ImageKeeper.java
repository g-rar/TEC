package com.example.lopez.picz.PiczData;

import com.example.lopez.picz.classes.PiczImage;

public class ImageKeeper {
    public PiczImage piczImage;

    private static final ImageKeeper INSTANCE = new ImageKeeper();

    private ImageKeeper() {}

    public static ImageKeeper getInstance() {
        return INSTANCE;
    }

    public void setPiczImage(PiczImage piczImage){
        this.piczImage = piczImage;
    }

    public PiczImage getPiczImage(){
        return piczImage;
    }
}
