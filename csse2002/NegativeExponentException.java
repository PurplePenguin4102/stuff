package prac3;

/** An exception used to indicate that the exponent of a term is negative. **/
@SuppressWarnings("serial")
public class NegativeExponentException extends RuntimeException {

	public NegativeExponentException() {
		super();
	}

	public NegativeExponentException(String s) {
		super(s);
	}
}
