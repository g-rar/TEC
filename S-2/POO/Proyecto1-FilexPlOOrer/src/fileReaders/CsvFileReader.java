package fileReaders;

import java.io.IOException;

public class CsvFileReader extends FatherFileReader {

    @Override
    public String toPlainText(String path) throws IOException {
        String fileContent = this.getFileContent(path);
        fileContent=fileContent.replaceAll("[;]+", " ");
        fileContent=fileContent.replaceAll("\\n", " ");
        
        return fileContent;
    }
       
}
