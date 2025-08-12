package com.globalsoftwaresupport;

public class App {

	public static void main(String[] args) {
		
		String text = "My name is Kevin and I like software engineering!";
		
		FrequencyAnalysis analysis = new FrequencyAnalysis();
		analysis.showFrequencies(text);
	}
}
