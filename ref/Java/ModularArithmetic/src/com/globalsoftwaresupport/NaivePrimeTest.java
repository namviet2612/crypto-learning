package com.globalsoftwaresupport;

public class NaivePrimeTest {

	public boolean isPrime(int n) {
		
		if(n < 2) return false;
		
		// if(n == 2) return true;
		
		if(n % 2 == 0) return false;
		
		// we have already checked numbers < 3
		// finding primes up to N we just have to check numbers up to sqrt(N)
		// increment by 2 because we have already considered even numbers
		for(int i=3;i<=Math.floor(Math.sqrt(n));i+=2)
			if(n % i == 0) 	
				return false;	
			
		return true;		
	}
}
