package util;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import calculators.VecCalculator;
import indexer.Indexer;

public class ArraySorter {

	public String[] vecSort(Indexer pIndex, VecCalculator pCalc, String pQuery) throws IOException {
		double[] indexedQuery = pIndex.indexQuery(pQuery).get(0);
		List<Double> results = new ArrayList<Double>();
		for (double[] vector : pIndex.getFileVectors()) {
			results.add(pCalc.compareVectors(vector, indexedQuery));
		}
		
		String[] sortedPaths = new String[results.size()];
		for(int i = 0 ; i < results.size() ; i++) {
			int position = getIndexOfHigher(results);
			sortedPaths[i] = pIndex.getFilePaths().get(position);
			results.remove(position);
			results.add(position, 0.0);
		}
		return sortedPaths;
		
	}
	
	private int getIndexOfHigher(List<Double> pList) {
		double higher = 0.0;
		for(double num : pList) {
			if(num>higher) {
				higher = num;
			}
		}
		return pList.indexOf(higher);
	}

	public String[] numStrSort(List<Double> values, String[] arrayToSort, boolean inverse) {
		
		if(values.size() != arrayToSort.length) {
			return null;
		}
		
		String[] sorted = new String[arrayToSort.length];
		for(int i = 0 ; i < values.size() ; i++) {
			int position = getIndexOfHigher(values);
			sorted[i] = arrayToSort[position];
			values.remove(position);
			values.add(position, 0.0);
		}
		
		if(inverse) { //este jjj
			String[] inversed = sorted;
			for (int i = 0 ; i < inversed.length ; i++) {
				sorted[i] = inversed[inversed.length - i - 1];
			}
		}
		
		return sorted;
	}
	
}
