package calculators;

public class ManhattanDisCalculator extends VecCalculator {
	
	

	@Override
	public double compareVectors(double[] docVector1, double[] docVector2) {
		double result = 0.0;
		
		for(int i = 0 ; i < docVector1.length ; i++) {
			result += Math.abs(docVector1[i] - docVector2[i]);
		}
		
		return result;
	}

	@Override
	public boolean zeroIsEquality() {
		return true;
	}

}
