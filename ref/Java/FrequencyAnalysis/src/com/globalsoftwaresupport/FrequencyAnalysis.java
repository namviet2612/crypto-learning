package com.globalsoftwaresupport;

import java.util.HashMap;
import java.util.Map;

public class FrequencyAnalysis {

	private String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	
	// the method to do frequency analysis: we just count the 
	// occurrences of the given characters
	private Map<Character, Integer> run(String text) {
		
		// the text we analyze
		text = text.toUpperCase();
		
		// we use a HashMap to store the letter-frequency pairs
		Map<Character, Integer> frequencies = new HashMap<>();
		
		// initialize the HashMap with all the letters of the ALPHABET
		// and of course with frequencies 0
		for(int i=0;i<ALPHABET.length();++i)
			frequencies.put(ALPHABET.charAt(i), 0);
		
		for(int i=0;i<text.length();++i) {
			
			char c = text.charAt(i);
			
			// we keep incrementing the occurrence of the given letter if 
			// it is present in the ALPHABET
			if(ALPHABET.indexOf(c) != -1)
				frequencies.put(c, frequencies.get(c)+1);
		}
		
		return frequencies;
	}
	
	public void showFrequencies(String text) {
		
		Map<Character, Integer> frequencies = run(text);
		
		for(Map.Entry<Character, Integer> entry : frequencies.entrySet()) {
			System.out.format("Character %s has frequency: %s%n", 
					entry.getKey(), entry.getValue());
		}
	}
}
