package com.globalsoftwaresupport;

import java.math.BigInteger;

public class App {

	public static void main(String[] args) {
		
		FermatPrimeTest algorithm = new FermatPrimeTest();
		System.out.println(algorithm.isPrime(BigInteger.valueOf(100000000), 10));
	}
}