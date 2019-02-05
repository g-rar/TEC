package indexer;

import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import calculators.TFIDFCalculator;
import fileReaders.FatherFileReader;
import fileReaders.Parser;
import fileReaders.ReaderFactory;
import util.FileFinder;

public class Indexer {
	
	private String name;
	private List<String> allTerms = new ArrayList<String>();
	private List<String> filePaths = new ArrayList<String>();
	private List<double[]> fileVectors = new ArrayList<double[]>();
	
	public Indexer(String pPath) throws IOException, SQLException, InterruptedException {
		indexFolder(pPath);
	}
	
	public Indexer(String pName, List<String> pAllTerms, List<String> pFilePaths, List<double[]> pFileVectors) {
		setName(pName);
		setAllTerms(pAllTerms);
		setFilePaths(pFilePaths);
		setFileVectors(pFileVectors);
	}
	
	public String getName() {
		return name;
	}
	
	public void setName(String pName) {
		name = pName;
	}
	
	public String[] getAllTerms(){
		String[] returnValue = new String[allTerms.size()];
		returnValue = allTerms.toArray(returnValue);
		return returnValue;
	}
	
	public void setAllTerms(List<String> pAllTerms) {
		allTerms = pAllTerms;
	}
	
	
	public List<double[]> getFileVectors(){
		return fileVectors;
	}
	
	public void setFileVectors(List<double[]> pFileVectors) {
		fileVectors = pFileVectors;
	}
	
	public List<String> getFilePaths(){
		return filePaths;
	}
	
	public void setFilePaths(List<String> pPaths) {
		filePaths = pPaths;
	}
	
	
	private void indexFolder(String pPath) throws SQLException, InterruptedException, IOException {
		
		String[] name = pPath.split("\\\\");
		FileFinder ff = new FileFinder();
		TFIDFCalculator calc = new TFIDFCalculator();
		List<String> paths = ff.getAllFilePaths(pPath);
			if(paths == null) return;
		List<String> preAllTerms = new ArrayList<String>();
		List<String> preFilePaths = new ArrayList<String>();
		List<String[]> parsedFiles = new ArrayList<String[]>();
		for (int x = 0 ; x<paths.size();x++) {
			//Classify and parse file
			String[] pf = parseFile(paths.get(x));
			if(pf != null) {
				parsedFiles.add(pf);
				preFilePaths.add(paths.get(x));
				for(String term : pf) {
					if(!preAllTerms.contains(term.toLowerCase())) {
						preAllTerms.add(term.toLowerCase());
					}
				}
			}
			
		}
		setName(name[name.length - 1]);
		setAllTerms(preAllTerms);
		setFilePaths(preFilePaths);
		setFileVectors(calc.calculatetfidf(parsedFiles, allTerms));
	}
	
	private String[] parseFile(String pPath) throws IOException {
		Parser dp = new Parser();
		FatherFileReader reader = ReaderFactory.classify(pPath);
		if(reader!= null) {
			String fileContent = reader.toPlainText(pPath);
			String[] parsedFile = dp.parse(fileContent);
			if(parsedFile.length != 0) {
				return parsedFile;
			}
		}
		return null;
	}
	
	public List<double[]> indexQuery(String query) throws IOException {
		
		if(allTerms.isEmpty()) throw new IOException();
		
		TFIDFCalculator calc = new TFIDFCalculator();
		Parser qp = new Parser();
		String[] allTermsArray = new String[allTerms.size()];
		allTermsArray = allTerms.toArray(allTermsArray);		
		String[] parsedQuery = qp.parse(query.toLowerCase());
		List<String[]> pParsedQuery = new ArrayList<String[]>();
		pParsedQuery.add(parsedQuery);
		
		List<double[]> queryVector = calc.calculatetfidf(pParsedQuery, allTerms);
		
		return queryVector;		
	}

}
