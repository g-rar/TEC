package app;

import java.io.File;
import java.io.IOException;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import calculators.CalculatorFactory;
import calculators.VecCalculator;
import indexer.Indexer;
import util.ArraySorter;
import indexer.IndexIO;

public class Facade {

	private Indexer index;
	private VecCalculator calc;
	private String dataSaveDir;
	private CalculatorFactory calcFactory = new CalculatorFactory();
	private IndexIO indexIO = new IndexIO();
	private ArraySorter fileSor = new ArraySorter();

	public void index(String pPath) throws SQLException, InterruptedException, IOException {
		index = new Indexer(pPath);
	}

	public void setIndexer(String indexPath) throws IOException {
		index = indexIO.loadIndex(indexPath);
	}

	public String getIndexer() {
		return index.getName();
	}

	public void setCalculator(String pCalc) throws IOException {
		calc = calcFactory.getCalculator(pCalc);
	}

	public String getCalculator() {
		return calc.toString();
	}

	public void saveIndex() throws Exception {
		if (dataSaveDir != null) {
			indexIO.saveIndex(index, dataSaveDir);
		} else {
			throw new Exception();
		}
	}

	public void setDataSaveDir(String pPath) throws IOException {
		File f = new File(pPath);
		if (!(f.exists() & f.isDirectory()))
			throw new IOException();
		if (!pPath.endsWith("\\"))
			pPath = pPath + "\\";
		dataSaveDir = pPath;
	}

	public String[] searchQuery(String pQuery) throws IOException, NullPointerException {
		if (index != null & calc != null & pQuery != "") {
			double[] indexedQuery = index.indexQuery(pQuery).get(0); 
			List<Double> results = new ArrayList<Double>();
			for (double[] vector : index.getFileVectors()) {
				results.add(calc.compareVectors(vector, indexedQuery)); 
			}
			String[] tFilePaths = new String[index.getFilePaths().size()];
			for(int i = 0 ; i < tFilePaths.length ; i++) {
				tFilePaths[i] = index.getFilePaths().get(i);
			}
			return fileSor.numStrSort(results, tFilePaths, calc.zeroIsEquality());
		}
		throw new NullPointerException();
	}

}
