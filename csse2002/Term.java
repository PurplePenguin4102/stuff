package prac3;

/**
 * An immutable class representing a term in a polynomial (with a single
 * indeterminate "x"). A term has an integer coefficient and a non-negative
 * integer exponent. A typical term is "3x^2".
 **/
public class Term {

	private int coefficient; // the coefficient of the term
	private int exponent; // the exponent of the term

	/*
	 * Invariant: the exponent is non-negative && if the coefficient is zero,
	 * then so is the exponent (e.g. we can't have 0x^9, only 0)
	 */

	/**
	 * Creates a new Term with the given coefficient and exponent. If the
	 * coefficient is zero, then the exponent is set to the default value of
	 * zero (creating the zero term).
	 * 
	 * @param coefficient
	 *            the coefficient of the new term
	 * @param exponent
	 *            the non-negative exponent of the new term
	 * @throws NegativeExponentException
	 *             if exponent < 0
	 */
	public Term(int coefficient, int exponent) {
		if (exponent < 0) {
			throw new NegativeExponentException();
		}
		this.coefficient = coefficient;
		this.exponent = (coefficient == 0 ? 0 : exponent);
	}

	/**
	 * Returns the coefficient of the term,
	 * 
	 * @return the coefficient of the term
	 */
	public int getCoefficient() {
		return coefficient;
	}

	/**
	 * Returns the exponent of the term,
	 * 
	 * @return the exponent of the term
	 */
	public int getExponent() {
		return exponent;
	}

	/**
	 * Takes a term with the same exponent as this, and returns a new term that
	 * is equal to this plus the parameter term.
	 * 
	 * @param term
	 *            the term to be added to this one
	 * @return a new term that is equal to this plus parameter term
	 */
	public Term addTerm(Term term) {
		if (coefficient == -term.coefficient) {
			return new Term(0, 0);
		} else {
			return new Term(coefficient + term.coefficient, exponent);
		}
	}

	/**
	 * Takes a term with the same exponent as this, and returns a new term that
	 * is equal to this term minus the parameter term.
	 * 
	 * @param term
	 *            the term to be added to this one
	 * @return a new term equal to this minus parameter term
	 */
	public Term subtract(Term term) {
		if (coefficient == term.coefficient) {
			return new Term(0, 0);
		} else {
			return new Term(coefficient - term.coefficient, exponent);
		}
	}

	/**
	 * Returns a new term that is the negation of this one. E.g. if this term
	 * were "3x^5" we would return the term corresponding to "-3x^5".
	 * 
	 * @return a new term equal to the negation of this
	 */
	public Term negate() {
		return new Term(-coefficient, exponent);
	}

	/**
	 * <p>
	 * Returns the string representation of the term.
	 * </p>
	 * 
	 * <p>
	 * All terms having a zero coefficient are represented by the string "0". A
	 * term with a non-zero coefficient c and an exponent n is represented by
	 * the string "c" if n is zero, "cx" if n is one, and "cx^n" otherwise.
	 * </p>
	 * 
	 * <p>
	 * (Note that this representation isn't as nice as it could be: e.g. we
	 * write "1x^2" for the term with coefficient 1 and exponent 2.)
	 * <p>
	 */
	public String toString() {

		if (coefficient == 0) {
			return "0";
		} else {
			return coefficient + getExponentString();
		}
	}

	/** Returns a string representation of the exponent-part of the term. **/
	private String getExponentString() {
		switch (exponent) {
		case 0:
			return "";
		case 1:
			return "x";
		default:
			return "x^" + exponent;
		}
	}

	/**
	 * Determines whether this Term is internally consistent (i.e. it satisfies
	 * its class invariant). This method should only be used for testing the
	 * implementation of the class.
	 * 
	 * @return true if this polynomial is internally consistent, and false
	 *         otherwise.
	 */
	public boolean checkInv() {
		return ((exponent >= 0) && ((coefficient == 0 && exponent == 0) || coefficient != 0));
	}

	/*
	 * NOTE: Since this is an immutable datatype we should be overriding equals
	 * and hashCode. We will learn about this in the week 4 lectures.
	 */
}
