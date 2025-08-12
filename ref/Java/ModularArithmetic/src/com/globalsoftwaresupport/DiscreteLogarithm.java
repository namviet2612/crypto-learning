package com.globalsoftwaresupport;

import java.math.BigInteger;

public class DiscreteLogarithm {

	// THIS IS SLOW !!!
	public BigInteger discreteLogarithm(BigInteger a, BigInteger b, BigInteger m) {
		
		// we try all the values of the exponent one by one until we find it
		BigInteger c = new BigInteger("1");
		
		// if b^c mod m = a it means we find the right c exponent
		while(b.modPow(c, m).compareTo(a) != 0)
			// if the exponent is not right we consider the next one
			c = c.add(BigInteger.ONE);
		
		return c;
	}
	
	// IT IS FAST
	// modular exponentiation: we just have to use the formula (b^c) mod m
	public BigInteger modularExponentiation(BigInteger b, BigInteger c, BigInteger m) {
		return b.modPow(c, m);
	}
	
}
