package parser;

import java.util.ArrayList;
import java.util.List;

public class Parser {

	public String[] parse(String fileText) {

		String[] rawTokenizedTerms = fileText.replaceAll("[\\W&&[^\\s]&&[^\\ñáéíóúÑÁÉÍÓÚ]]", "").split("[\\s]"); // to get individual terms
		List<String> termsList = new ArrayList<String>();
		for (String elem : rawTokenizedTerms) {
			if (!elem.equals("")) {
				termsList.add(elem);
			}
		}
		String[] tokenizedTerms = new String[termsList.size()];
		tokenizedTerms = termsList.toArray(tokenizedTerms);
		return tokenizedTerms;
	}
}
