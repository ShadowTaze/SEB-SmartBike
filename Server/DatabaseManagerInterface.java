import java.util.HashMap;
public interface DatabaseManagerInterface{
	public void addMeasurement(String type, String data) throws Exception;
	public String getMeasurmentEntities() throws Exception;
	public String getMeasurmentEntities(String type) throws Exception;
	public String getMeasurmentTypes() throws Exception;
	public HashMap<String, String> getSystemState() throws Exception;
	public void setSystemState(HashMap<String, String> state) throws Exception;
	public void newRide() throws Exception;
	public void exit() throws Exception;
}