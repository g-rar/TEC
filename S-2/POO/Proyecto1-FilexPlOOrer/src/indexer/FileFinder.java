package indexer;

import java.io.File;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import fileReaders.IReadable;

public class FileFinder implements IReadable{
	
	public List<String> getAllFilePaths(String directorio) throws SQLException, InterruptedException {
		
		File f = new File(directorio);
		File[] ficheros = f.listFiles();
		List<String> filePaths = new ArrayList<String>();
		for (int x = 0; x < ficheros.length; x++) {
			if (ficheros[x].isDirectory()) {
				filePaths.addAll(getAllFilePaths(ficheros[x].getPath()));
			} else {
				for(String type : ACCEPTED_FILE_TYPES) {
					if(ficheros[x].getName().endsWith(type))
						filePaths.add(ficheros[x].getPath());
				}
			}
		}
		return filePaths;
	}

}
