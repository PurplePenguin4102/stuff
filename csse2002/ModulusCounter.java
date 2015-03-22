package week3;

public class ModulusCounter {
	private static int i = 0;
	private static int max = 0;
	
	
	public static void ModulusCounter(int n){
		max = n;
	}
	
	public static void increment(){
		if (i < max)
			i++;
		else
			i = 0;
	}
	public static void main(String[] args) {
		ModulusCounter(4);
		increment();
		increment();
		System.out.println(i);
		increment();
		System.out.println(i);
		increment();
		System.out.println(i);
		increment();
		System.out.println(i);
		
		
	}

}
