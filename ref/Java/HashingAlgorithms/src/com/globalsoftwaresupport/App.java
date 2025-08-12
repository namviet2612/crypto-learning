package com.globalsoftwaresupport;

public class App {

	public static void main(String[] args) {
		
		SHA256 sha = new SHA256();
		
		String message = "Hashing algorithms are crucial in cryptography!";
		
		System.out.println(sha.digest(message));
	}
}