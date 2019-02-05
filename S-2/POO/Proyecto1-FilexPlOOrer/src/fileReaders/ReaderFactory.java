package fileReaders;

public class ReaderFactory implements IReadable{
	public static FatherFileReader classify(String path) {
		
		for(int i = 0 ; i<ACCEPTED_FILE_TYPES.length ; i++) 
			if(path.endsWith(ACCEPTED_FILE_TYPES[i]))
				return FILE_READERS[i];
		
		return null;
	}
}