package com.globalsoftwaresupport;

public class ModularInverse {

	public int calculate(int a, int m) {
		
		// this is the brute-force approach so we check all possible values in 
		// the range [0, m-1]
		// running time seems to be O(m) linear but it is actually
		// exponential in the number of input bits
		for(int inv=0;inv<m;++inv) 
			if((a*inv) % m == 1)
				return inv;
		
		// there is no modular inverse (a is not a coprime to m)
		return -1;
	}
}
