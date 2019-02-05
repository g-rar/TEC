package fileReaders;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public abstract class FatherFileReader {

	public String getFileContent(String path) throws IOException {
		BufferedReader reader = new BufferedReader(new FileReader(path));
		String returnValue = "";
		String line;

		while ((line = reader.readLine()) != null) {
			returnValue = returnValue + line + "\n";
		}
		reader.close();
		return returnValue;

	}

	public abstract String toPlainText(String pPath) throws IOException;

}
