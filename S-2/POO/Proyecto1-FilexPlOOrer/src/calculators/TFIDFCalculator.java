package calculators;

import java.util.ArrayList;
import java.util.List;

public class TFIDFCalculator {
	
	public List<double[]> calculatetfidf(List<String[]> pParsedFiles, List<String> AllTerms) {
        double tf; //term frequency
        double idf; //inverse document frequency
        double tfidf; //term frequency inverse document frequency
        List<double[]> tfidfDocsVector = new ArrayList<double[]>();
        
        for (String[] fileTerms : pParsedFiles) {
            double[] tfidfvectors = new double[AllTerms.size()];
            int count = 0;
            for (String term : AllTerms) {
                tf = this.calculateTF(fileTerms, term);
                idf = this.calculateIDF(pParsedFiles, term);
                tfidf = tf * idf;
                tfidfvectors[count] = tfidf;
                count++;
            }
            tfidfDocsVector.add(tfidfvectors);  //storing document vectors;
        }
        return tfidfDocsVector;
    }
	
	public double calculateTF(String[] pFileTerms, String pTermToCheck) {
		
		double count = 0;
		for(String s: pFileTerms) {
			if(s.equalsIgnoreCase(pTermToCheck)) 
				count++;
		}
		return count / pFileTerms.length;
	}
	
	public double calculateIDF(List<String[]> pParsedFiles, String pTermToCheck) {
		
		double count = 0;
		for(String[] ss : pParsedFiles)
			for(String s : ss) 
				if(s.equalsIgnoreCase(pTermToCheck)) {
					count++;
					break;
				}
		
		return 1 + Math.log(pParsedFiles.size() / 1+count);
	} 
}
