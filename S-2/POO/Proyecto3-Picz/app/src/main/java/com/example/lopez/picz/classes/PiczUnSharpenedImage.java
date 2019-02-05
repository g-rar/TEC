package com.example.lopez.picz.classes;

import android.graphics.Bitmap;
import android.graphics.Color;

import java.util.ArrayList;
import java.util.List;

public class PiczUnSharpenedImage extends PiczImageDecorator implements PiczImage {

    private final int KERNEL_SIZE = 7;
    private final int KERNEL_HALF = 3;
    private List<List<Double>> kernel;

    public PiczUnSharpenedImage(PiczImage pImg, double sigma, double lambda) {
        super(pImg);
        kernel = generateKernel(KERNEL_SIZE, sigma);
        Bitmap oImage = this.getBitMap();
        Bitmap newImage = oImage.copy(oImage.getConfig(), true);
        for (int y = 0; y < oImage.getHeight(); y++) {
            for (int x = 0; x < oImage.getWidth(); x++) {
                int newPixel = kernelizePixel(x, y , oImage, lambda);
                newImage.setPixel(x,y, newPixel);
            }
        }
        this.setBitmap(newImage);
    }

    private List<List<Double>> generateKernel(int pSize, double sigma){
        List<List<Double>> result = new ArrayList<>();
        for (int row = 0 ; row < pSize ; row++){
            result.add(new ArrayList<Double>());
            for (int colum = 0 ; colum < pSize ; colum ++){
                double x = colum - (pSize/2);
                double y = row - (pSize/2);
                double f = (-1 / (Math.PI * Math.pow(sigma, 4)))
                        * (1 - (x*x + y*y)/((2*sigma*sigma)))
                        * Math.pow(Math.E,-(x*x + y*y)/(2*sigma*sigma)) * 100;
                result.get(row).add(f);
            }
        }

        return result;
    }

    private int kernelizePixel(int x , int y , Bitmap bm, double lambda){
        double sumR, sumG, sumB;
        sumR = sumG = sumB = 0;
        int kUsed = KERNEL_SIZE;

        //for a 9x9 kernel, the loop goes from -4 to 4 in its last iteration
        for (int ky = -(KERNEL_HALF) ; ky <= KERNEL_HALF; ky++){
            for (int kx = -(KERNEL_HALF) ; kx <= KERNEL_HALF ; kx++){

                if (x + kx < 0 | x + kx >= bm.getWidth() | y + ky >= bm.getHeight() | y + ky < 0){
                    kUsed -= 1;
                    continue;
                }
                int pixel = bm.getPixel(x + kx, y + ky);
                double kernelValue = kernel.get(ky + KERNEL_HALF).get(kx + KERNEL_HALF);
                sumR += Color.red(pixel) * kernelValue;
                sumG += Color.green(pixel) * kernelValue;
                sumB += Color.blue(pixel) * kernelValue;
            }
        }

        int pixel = bm.getPixel(x, y);

        int nR = (int) (Color.red(pixel) + lambda * ((float)sumR/kUsed));
        int nG = (int) (Color.green(pixel) + lambda * ((float)sumG/kUsed));
        int nB = (int) (Color.blue(pixel) + lambda * ((float)sumB/kUsed));
        int newPixel = Color.argb(Color.alpha(pixel), nR, nG, nB);

        return newPixel;
    }
}