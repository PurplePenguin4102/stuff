package tutorial1;

public class IntArray {
	
	public static void sum(int[] a){
		// adds the elements of int array a
		int ans = 0;
		for (int i: a)
			ans += i;
		System.out.println(ans);
	}

	public static void countItem(int v, int[] a){
		// counts the number of times v appears in array a
		int ans = 0;
		for (int i: a)
			if (v == i)
				ans += 1;
		System.out.println(ans);
	}
	
	public static void sumArray(int[] a, int[] b, int[] c){
		// pointwise adds the elements of a to the elements of b to make array c
		for (int i = 0; i < a.length; i++)
			c[i] = a[i] + b[i];
		for (int j: c)
			System.out.println(j);
	}
	
	public static void prefix(String s1, String s2){
		// determines whether or not s1 is a prefix in s2
		int tru = 1;
		for (int i = 0; i < s1.length(); i++)
			if (s1.charAt(i) == s2.charAt(i)){
				tru = 1;
			}
			else {
				tru = 0;
				break;
			}
		System.out.println(tru);
		
	}
	
	public static void main(String[] args) {
		// In the main method we want to instanciate our questions and parse through 
		// the methods that print out the solutions to tutorial 1
		// Question 1:
        int [] a1 = {1,2,3,4,5};
        IntArray.sum(a1);
        
        // Question 2:
        int [] a2 = {0,1,1,0,0,0,1,0,1,0,1,1,1,0,0,0};
        IntArray.countItem(1,a2);
        
        // Question 3:
        int [] a3 = {1,2,3,4,5};
        int [] b3 = {1,2,3,4,5};
        int [] c3 = {0,0,0,0,0};
        IntArray.sumArray(a3,b3,c3);
        
        // Question 4:
        String s1 = "lol";
        String s2 = "Rollerskates";
        String s3 = "lollerskates";
        IntArray.prefix(s1,s2);
        IntArray.prefix(s1,s3);
	}

	
}
