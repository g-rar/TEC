package com.example.lopez.picz.room;

import android.arch.persistence.room.ColumnInfo;
import android.arch.persistence.room.Entity;
import android.arch.persistence.room.PrimaryKey;
import android.graphics.Bitmap;
import android.support.annotation.NonNull;


@Entity(tableName = "piczStories")
public class PiczStory {

    @PrimaryKey
    private int id;

    @ColumnInfo
    private String storyText;
    @ColumnInfo
    private String image;


    public PiczStory() {}

    public PiczStory (int id, String text, String pImage){
        //this.id = id;
        storyText = text;
        image = pImage;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getImage(){
        return image;
    }

    public String getStoryText() {
        return storyText;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public void setStoryText(String storyText) {
        this.storyText = storyText;
    }
}
