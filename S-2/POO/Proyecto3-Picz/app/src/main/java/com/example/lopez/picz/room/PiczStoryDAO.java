package com.example.lopez.picz.room;

import android.arch.persistence.room.Dao;
import android.arch.persistence.room.Insert;
import android.arch.persistence.room.Query;

import java.util.List;

@Dao
public interface PiczStoryDAO {

    @Insert
    void addStory(PiczStory story);

    @Query("SELECT * FROM piczStories")
    List<PiczStory> getAllStories();

}
