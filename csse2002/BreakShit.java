package prac3;

import prac3.Polynomial;
import prac3.Term;

import java.util.ArrayList;

import org.junit.Assert;

public class BreakShit {

	public static void main(String[] args) {
		Polynomial p1;
		Polynomial p2;
		Polynomial actual;
		p1 = new Polynomial(4, 2);
		p2 = new Polynomial(4, 2);
		Polynomial p3 = new Polynomial(5,3);
		actual = p1.add(p3.subtract(p2));
		Assert.assertEquals("5x^3", actual.toString());
		Assert.assertTrue("Invariant check failed", actual.checkInv());

	}

}
