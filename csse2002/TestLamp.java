package week3;

import static org.junit.Assert.*;

import java.util.HashMap;

import org.junit.Assert;
import org.junit.Test;

public class TestLamp {
	
	private Lamp l;
	
	@Test
	public void testLamp() {
		l = new Lamp();
		HashMap<String, String> setting = l.read();
		int i = setting.size();
		System.out.println(i);
		Assert.assertEquals(4, i);
		Assert.assertEquals("OFF", l.look());
	}

	@Test
	public void testPoke() {
		l = new Lamp();
		String s = l.look();
		l.poke();
		s = l.look();
		Assert.assertEquals("LOW", s);
		l.poke();
		s = l.look();
		Assert.assertEquals("MEDIUM", s);
		
		
	}

}
