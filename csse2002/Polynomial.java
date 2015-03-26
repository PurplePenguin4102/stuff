package prac3;

import java.util.ArrayList;

import prac3.Term;

/**
 * Represents an immutable polynomial with integer coefficients (and a single
 * indeterminate "x"). A typical polynomial is 5x^2 + 3x + 2.
 */
public class Polynomial {

	// a list of terms in the polynomial
	private ArrayList<Term> terms = new ArrayList<Term>();

	/*
	 * invariant:
	 * 
	 * terms != null
	 * 
	 * && terms does not contain null terms or terms with zero coefficients
	 * 
	 * && terms does not contain more than one term with the same exponent
	 * 
	 * && terms is ordered by the exponent of its terms in ascending order.
	 */

	/** Constructs a new zero polynomial. */
	public Polynomial() {
		// do nothing because we won't store terms with zero coefficients
	}

	/**
	 * Constructs a new monomial with the given exponent and coefficient.
	 * 
	 * @param coefficient
	 *            the coefficient
	 * @param exponent
	 *            the exponent
	 * @throws NegativeExponentException
	 *             if exponent < 0
	 */
	public Polynomial(int coefficient, int exponent)
			throws NegativeExponentException {
		if (exponent < 0) {
			throw new NegativeExponentException();
		}
		if (coefficient != 0) {
			terms.add(new Term(coefficient, exponent));
		}
	}

	// THE IMPLEMENTATION OF THIS METHOD CONTAINS A BUG: IT DOESN'T
	// PRESERVE THE INVARIANT
	/**
	 * Returns a new polynomial that is the result of adding p to this. Both
	 * this and parameter p should remain unchanged by this operation.
	 * 
	 * @param p
	 *            the polynomial to be added to this one
	 * @return a new polynomial that is is the result of adding p to this
	 */
	public Polynomial add(Polynomial p) {
		// the polynomial to be returned, initialised to 0
		Polynomial result = new Polynomial();
		/*
		 * Add each of the terms in this and p to result.terms in exponent
		 * order. (We essentially traverse both ordered lists of terms
		 * simultaneously, merging the terms into a new ordered list.)
		 */
		int i = 0; // current index into this.terms
		int j = 0; // current index into p.terms
		while (i < terms.size() && j < p.terms.size()) {
			if (terms.get(i).getExponent() == p.terms.get(j).getExponent()) {
				// the exponents of the terms are equal, so we add them together
				// before including them in result.terms
				Term nt = terms.get(i).addTerm(p.terms.get(j));
				result.terms.add(nt);
				i++;
				j++;
			}
			else if (this.terms.get(i).getExponent() < p.terms.get(j)
					.getExponent()) {
				// we append the smaller of the two terms onto result.terms
				result.terms.add(this.terms.get(i));
				i++;
			}
			else {
				// we append the smaller of the two terms onto result.terms
				result.terms.add(p.terms.get(j));
				j++;
			}
		}
		// add the remainder of terms in this to the result
		while (i < terms.size()) {
			result.terms.add(terms.get(i));
			i++;
		}
		// add the remainder of terms in p to the result
		while (j < p.terms.size()) {
			result.terms.add(p.terms.get(j));
			j++;
		}
		
		for (int ind = 0; ind < result.terms.size(); ind++){
			if (result.terms.get(ind).getCoefficient() == 0 && result.terms.get(ind).getExponent() == 0) {
				result.terms.remove(ind);
			}
		}
		
		return result;
	}

	/**
	 * Returns a new polynomial that is the result of subtracting p from this.
	 * Both this and parameter p should remain unchanged by this operation.
	 * 
	 * @param p
	 *            the polynomial to be subtracted from this one
	 * @return a new polynomial that is is the result of subtracting p from this
	 */
	public Polynomial subtract(Polynomial p) {
		Polynomial result = new Polynomial();
		Polynomial pneg = new Polynomial();
		for (int i = 0; i < p.terms.size(); i++){
			Term negterm = p.terms.get(i).negate();
			pneg.terms.add(i, negterm);
		}
		result = this.add(pneg);
		
		return result;
	}

	/**
	 * <p>
	 * Returns the string representation of the polynomial.
	 * </p>
	 * 
	 * <p>
	 * The zero polynomial is represented by the string "0". The string
	 * representation of a non-zero polynomial is a list of the non-zero terms
	 * in the polynomial in descending order of exponent concatenated together
	 * by a single plus operator with a single space on either side (i.e.
	 * " + ").
	 * </p>
	 * 
	 * <p>
	 * There shouldn't be more than one term with the same exponent in the
	 * string representation, i.e. we would write "3x^4 + 2x + 3" instead of
	 * "2x^4 + 1x^4 + 2x + 3"
	 * </p>
	 * 
	 * <p>
	 * A term with a non-zero coefficient a and exponent b is written "a" if b
	 * is zero, "ax" if b is one, and "ax^b" otherwise.
	 * </p>
	 * 
	 * <p>
	 * (Note that this representation isn't as nice as it could be. For example,
	 * we write "1x^2" instead of "x^2", and "3x^2 + -5x" instead of "3x^2 - 5x"
	 * etc. We are keeping it simple on purpose!)
	 * </p>
	 */
	public String toString() {
		if (terms.size() == 0) {
			return "0";
		}
		// the string representation under construction
		String s = "" + terms.get(terms.size() - 1);
		// add terms in descending order of exponent
		for (int i = terms.size() - 2; i >= 0; i--) {
			s = s + " + " + terms.get(i);
		}
		return s;
	}

	/**
	 * Determines whether this Polynomial is internally consistent (i.e. it
	 * satisfies its class invariant). This method should only be used for
	 * testing the implementation of the class.
	 * 
	 * @return true if this polynomial is internally consistent, and false
	 *         otherwise.
	 */

	public boolean checkInv() {
		if (terms == null){
			return false;
		}
		for (int i = 0; i < terms.size(); i++){
			if (!terms.get(i).checkInv()){
				return false;
			}
			if (terms.get(i) == null){
				return false;
			}
			
			Term t1 = terms.get(i);
			int e1 = t1.getExponent();
			for (int j = i; j < terms.size(); j++){
				Term t2 = terms.get(j);
				int e2 = t2.getExponent();
				if (e1 == e2 && t1 != t2){
					return false;
					}
				if (e2 < e1 && j < i){
					System.out.println("fail here");
					return false;
				    }
			}
		}
		
		return true;
	}

}
