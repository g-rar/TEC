package com.example.lopez.picz;

import android.content.Intent;
import android.net.Uri;
import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

//import com.example.lopez.picz.classes.MovieDatabase;

public class AddStoryActivity extends AppCompatActivity {
    private static final int PICK_IMAGE_REQUEST = 100;
    private static final int CAMERA_REQUEST = 9999;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_story);
    }

    public void fromGalery(View view){
        Intent photoPickerIntent = new Intent(Intent.ACTION_PICK);
        photoPickerIntent.setType("image/*");
        startActivityForResult(photoPickerIntent, PICK_IMAGE_REQUEST);
    }

    public void takePic(View view){
        Intent takePictureIntent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
        startActivityForResult(takePictureIntent, CAMERA_REQUEST);

    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data){
        switch (requestCode){
            case PICK_IMAGE_REQUEST:
                if(resultCode == RESULT_OK){
                    Uri selectedImage = data.getData();
                    Intent intent = new Intent(this, EditStoryActivity.class);
                    intent.putExtra("imageUri", selectedImage.toString());
                    startActivity(intent);
                }
                break;
            case CAMERA_REQUEST:
                if(resultCode == RESULT_OK){
                    Uri selectedImage = data.getData();
                    Intent intent = new Intent(this, EditStoryActivity.class);
                    intent.putExtra("imageUri", selectedImage.toString());
                    startActivity(intent);
                }
                break;
        }
    }
}
