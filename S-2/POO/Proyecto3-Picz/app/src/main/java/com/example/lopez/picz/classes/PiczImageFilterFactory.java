package com.example.lopez.picz.classes;

import android.graphics.Bitmap;


public class PiczImageFilterFactory {

    public static PiczImage getInstance(int type, PiczImage pImage, int param, int param2){
        switch (type){
            case 1:
                float factor = (float) (param / 100.0);
                return new PiczBWImage(pImage, factor);
            case 2:
                return new PiczBurlImage(pImage, param);
            case 3:
                return new PiczAbsoluteBWImage(pImage, param);
            case 4:
                double sigma= param/10;
                double lambda=param2/10;
                return new PiczUnSharpenedImage(pImage, sigma, lambda);
        }
        return null;
    }
}
