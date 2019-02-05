package fileReaders;

import java.io.IOException;

public class XmlFileReader extends FatherFileReader {

    @Override
    public String toPlainText(String path) throws IOException {
        String fileContent = this.getFileContent(path);
        return XmlParse(fileContent);
        
    }
    
    private String XmlParse(String value){
        
        int len = value.length()-1;
        int i=0;
        int primero=0;
        int segundo=0;
        while(i<=len){
            i=0;
            while(value.charAt(i)!= '<'){
                i++;
                if (i>len){
                    break;}}
            
            if (i>len){break;}
            
            primero=i;
            
            while(value.charAt(i)!= '>')i++;
            segundo=i+1;
            
            value=value.replace(value.substring(primero, segundo)," ");
            len = value.length()-1;
            i++;
        }
        
        String replaceAll = value.replaceAll("\\s+", " ");
        //System.out.println(replaceAll+"\n*************************************************************\n");
        replaceAll=replaceAll.replaceAll("^\\s", "");
        //System.out.println(replaceAll+"\n*************************************************************\n");
        
        return replaceAll;
    } 
    
}
