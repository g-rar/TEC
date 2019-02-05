package app;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import org.json.JSONObject;

import fileReaders.TextFileReader;

public class CommandDataSaver {

	private File f = new File("Data.json");
	private JSONObject json;
	private String calc = "";
	private String saveDataDir = "";
	private String indexerPath = "";

	public CommandDataSaver() {
		try {
			if (!f.exists()) {
				f.createNewFile();
				updateData();
			}
			updateJSON();

		} catch (IOException e) {
			e.printStackTrace();
		}
	}

	public void updateJSON() {
		try {
			json = new JSONObject(new TextFileReader().getFileContent("Data.json"));
			setCalc(json.getString("calc"));
			setSaveDataDir(json.getString("saveDataDir"));
			setIndexerPath(json.getString("indexerPath"));
		} catch (IOException e) {
			System.out.println(
					"\n Algo salió mal a la hora de cargar los datos del programa. Esta es la información del error:");
			e.printStackTrace();
		}
	}
	
	public void updateData() throws IOException {
		json = new JSONObject(this);
		String jcdText = json.toString();
		FileWriter writer = new FileWriter(f);
		writer.write(jcdText);
		writer.close();
	}

	public String getCalc() {
		return calc;
	}

	public void setCalc(String calc) {
		this.calc = calc;
	}

	public String getSaveDataDir() {
		return saveDataDir;
	}

	public void setSaveDataDir(String saveDataDir) {
		this.saveDataDir = saveDataDir;
	}

	public String getIndexerPath() {
		return indexerPath;
	}

	public void setIndexerPath(String indexerPath) {
		this.indexerPath = indexerPath;
	}

}
