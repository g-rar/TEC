package com.example.lopez.picz;

import android.content.Intent;
import android.graphics.Bitmap;
import android.net.Uri;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Base64;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.SeekBar;
import android.widget.Spinner;
import android.widget.Toast;


import com.example.lopez.picz.classes.PiczBasicImage;
import com.example.lopez.picz.classes.PiczImage;
import com.example.lopez.picz.classes.PiczImageFilterFactory;
import com.example.lopez.picz.room.AppDataBase;
import com.example.lopez.picz.room.PiczStory;

import java.io.ByteArrayOutputStream;
import java.io.IOException;

public class EditStoryActivity extends AppCompatActivity {
    private ImageView imagePreview;
    private Spinner spinner;
    private SeekBar seekBar;
    private SeekBar seekBar2;
    private EditText editText;
    private static Uri imagePreviewUri;
    private static PiczImage image;
    private static AppDataBase db;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_edit_story);
        Intent intent = getIntent();
        imagePreviewUri = Uri.parse(intent.getStringExtra("imageUri"));
        imagePreview = findViewById(R.id.previewImage);
        db = AppDataBase.getAppDatabase(getApplicationContext());

        Bitmap imageBM = null;
        try {
            imageBM = MediaStore.Images.Media.getBitmap(this.getContentResolver(), imagePreviewUri);
        } catch (IOException e) {
            e.printStackTrace();
        }
        image = new PiczBasicImage(imageBM);
        imagePreview.setImageBitmap(image.getBitMap());

    }

    public void addFilterToImage(View view){
        spinner = findViewById(R.id.spinner);
        seekBar = findViewById(R.id.seekBar);

        seekBar2 = findViewById(R.id.seekBar2);
        int selectedFilter = spinner.getSelectedItemPosition();
        int param = seekBar.getProgress();
        int param2 = seekBar2.getProgress();
        if(selectedFilter != 0){
            image = PiczImageFilterFactory.getInstance(selectedFilter, image, param,param2);
            imagePreview.setImageBitmap(image.getBitMap());
            Toast.makeText(EditStoryActivity.this, R.string.filter_applied, Toast.LENGTH_SHORT).show();
        }else {
            Toast.makeText(EditStoryActivity.this, R.string.no_filter_selected, Toast.LENGTH_SHORT).show();
        }
    }

    public void removeFilters(View view){
        Bitmap imageBM = null;
        try {
            imageBM = MediaStore.Images.Media.getBitmap(this.getContentResolver(), imagePreviewUri);
        } catch (IOException e) {
            e.printStackTrace();
        }
        image = new PiczBasicImage(imageBM);
        imagePreview.setImageBitmap(image.getBitMap());
        Toast.makeText(EditStoryActivity.this, getResources().getString(R.string.image_filters_removed), Toast.LENGTH_LONG).show();
    }



    public void saveData(View view){
        editText = findViewById(R.id.storyEditText);
        String storyText =  editText.getText().toString();

        ByteArrayOutputStream baos=new  ByteArrayOutputStream();
        image.getBitMap().compress(Bitmap.CompressFormat.PNG,100, baos);
        byte [] b=baos.toByteArray();
        String storyPicture = Base64.encodeToString(b, Base64.DEFAULT);

        PiczStory newStory = new PiczStory();
        newStory.setImage(storyPicture);
        newStory.setStoryText(storyText);
        newStory.setId(newStory.hashCode());

        try {

            this.db.piczStoryDAO().addStory(newStory);
            Toast.makeText(EditStoryActivity.this, "The story has been loaded", Toast.LENGTH_SHORT).show();
        } catch(Exception e){
            Toast.makeText(EditStoryActivity.this, e.getMessage(), Toast.LENGTH_SHORT).show();
        }
    }

}
