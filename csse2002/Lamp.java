package week3;

import java.util.Map;
import java.util.HashMap;

public class Lamp {
	private HashMap<String, String> setting = new HashMap<String, String>();
	private String state = "OFF";
	
	public Lamp(){
		setting.put("OFF", "LOW");
		setting.put("LOW", "MEDIUM");
		setting.put("MEDIUM", "HIGH");
		setting.put("HIGH", "OFF");
	}
	
	public void poke(){
		state = setting.get(state);
	}
	
	public HashMap<String, String> read(){
		return setting;
	}
	
	public String look(){
		return state;
	}
	
//	public static void main(String[] args) {
//		System.out.println(state);
//		Lamp();
//		poke();
//		System.out.println(state);
//		poke();
//		poke();
//		System.out.println(state);
//	}

}
