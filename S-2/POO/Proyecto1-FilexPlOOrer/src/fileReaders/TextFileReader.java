package fileReaders;

import java.io.IOException;

public class TextFileReader extends FatherFileReader {
		
	@Override
	public String toPlainText(String path) throws IOException {
		return this.getFileContent(path);
	}
	
	

}
