package fileReaders;

public interface IReadable {
	
	public final String[] ACCEPTED_FILE_TYPES = {
			".txt", 
			".json",
			".csv",
			".xml",
			".html"};
	
	public final FatherFileReader[] FILE_READERS = {
			new TextFileReader(), 
			new JsonFileReader(),
			new CsvFileReader(),
			new XmlFileReader(),
			new XmlFileReader()};

}
