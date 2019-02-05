package calculators;

import java.io.IOException;

public class CalculatorFactory {
	
	String[] calcStrings = {"cosine",
			"manhattan"};
	VecCalculator[] calculators = { new CosSimilarityCalculator(),
			new ManhattanDisCalculator()};
	
	public VecCalculator getCalculator(String pCalc) throws IOException {
		for(int i = 0 ; i < calcStrings.length ; i++) {
			if(calcStrings[i].equals(pCalc)) {
				return calculators[i];
			}
		}
		throw new IOException("'" + pCalc + "' no es una calculadora aceptada.");
	}
	
}
