package indexer;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import fileReaders.TextFileReader;

import org.json.*;
import com.google.gson.*;

public class IndexIO {

	public void saveIndex(Indexer pIndexer, String pDirectory) throws IOException {
		JSONObject jsonObject = new JSONObject(pIndexer);
		String jsonText = jsonObject.toString();
		File jsonFile = new File(pDirectory + pIndexer.getName() + ".json");
		FileWriter writer = new FileWriter(jsonFile);
		writer.write(jsonText);
		writer.close();

	}

	public Indexer loadIndex(String indexPath) throws IOException {
		String jsonString = new TextFileReader().getFileContent(indexPath);
		Gson gson = new GsonBuilder().create();
		JsonElement root = new JsonParser().parse(jsonString);
		Indexer indexer = gson.fromJson(root, Indexer.class);
		return indexer;
	}
}