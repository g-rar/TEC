package com.example.lopez.picz;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;


public class MenuActivity extends AppCompatActivity {
    public static final String EXTRA_MESSAGE = "com.example.lopez.picz.MESSAGE";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);
    }

    /**Called whe the user taps the Send Button*/
    public void goToStories(View view){
        //Do something in response to button
        Intent intent = new Intent(this, StoriesActivity.class);
        startActivity(intent);
    }

    public void addStory(View view){
        Intent intent = new Intent(this, AddStoryActivity.class);
        startActivity(intent);
    }

    public void closeApp(View view){
        finish();
        System.exit(0);
    }


}
