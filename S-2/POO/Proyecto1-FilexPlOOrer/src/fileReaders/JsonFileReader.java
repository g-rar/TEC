package fileReaders;
import java.io.IOException;
import org.json.* ;

public class JsonFileReader extends FatherFileReader {
		
	@Override
	public String toPlainText(String path) throws IOException {

		String fileContent = this.getFileContent(path);
		JSONObject jsonObject = new JSONObject(fileContent);
		return jsonObjToStr(jsonObject);
	}
	
	private String jsonObjToStr(JSONObject pJObject) {
		
		String returnValue = "";
		JSONArray jsonArray = pJObject.names();
		
		for(int i = 0 ; i<jsonArray.length(); i++) {
			String key = jsonArray.getString(i);
			Object value = pJObject.get(key);
			returnValue = returnValue + " " + jsonIFs(value);
		}
		return returnValue;
	}
	
	private String jsonArrToStr(JSONArray pJArray) {
		String returnValue = "";
		for(int i = 0; i<pJArray.length() ; i++) {
			Object value = pJArray.get(i);
			returnValue = returnValue + " " + jsonIFs(value);
		}
		
		return returnValue;
	}
	
	private String jsonIFs(Object value) {
		if(!(value instanceof JSONArray | value instanceof JSONObject)) {
			return value.toString();
		} else if (value instanceof JSONArray) {
			return jsonArrToStr((JSONArray) value);
		} else {
			return jsonObjToStr((JSONObject)value);
		}
	}
	
	

}
