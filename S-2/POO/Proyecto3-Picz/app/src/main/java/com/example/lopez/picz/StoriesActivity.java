package com.example.lopez.picz;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Base64;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;
import android.graphics.BitmapFactory;

import com.example.lopez.picz.room.AppDataBase;
import com.example.lopez.picz.room.PiczStory;

import java.util.List;

public class StoriesActivity extends AppCompatActivity {

    private static final BitmapFactory BitmapFactory = new BitmapFactory();
    private static AppDataBase db;
    private static TextView message;
    private static LinearLayout linearLayout;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_stories);

        db = AppDataBase.getAppDatabase(getApplicationContext());
        List<PiczStory> stories = db.piczStoryDAO().getAllStories();

        Toast.makeText(StoriesActivity.this, "Hay: " + stories.size() + " historias", Toast.LENGTH_LONG).show();
        message = findViewById(R.id.storiesTitleTextView);

        if(stories.size() == 0 ){
            message.setText(R.string.no_stories_found);
            return;
        }
        message.setText(R.string.stories_found);

        linearLayout = findViewById(R.id.storiesLinearLayout);
        for (int i = 0; i < stories.size(); i++) {
            PiczStory storyValue = stories.get(i);

            String storyImageStr = storyValue.getImage();
            Bitmap storyImage = stringToBitmap(storyImageStr);
            ImageView imageView = new ImageView(this);
            imageView.setImageBitmap(storyImage);
            linearLayout.addView(imageView);

            TextView textView = new TextView(this);
            textView.setText(storyValue.getStoryText());
            linearLayout.addView(textView);
        }


    }

    private Bitmap stringToBitmap(String string){
        try {
            byte [] encodeByte=Base64.decode(string,Base64.DEFAULT);
            Bitmap bitmap=BitmapFactory.decodeByteArray(encodeByte, 0, encodeByte.length);
            return bitmap;
        } catch(Exception e) {
            e.getMessage();
            return null;
        }
    }
}
