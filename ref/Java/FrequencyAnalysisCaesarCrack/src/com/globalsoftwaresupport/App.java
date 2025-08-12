package com.globalsoftwaresupport;

public class App {

	public static void main(String[] args) {
		
		String cipher = "WHJXKWOJSBJUOESXJKXNJSJKWJKJFYAUSXQJKBJKJBYPCFKAOJOXQSXOOAJKCJKJWDVCSXKCSYXKVJMYWZKXHJKXNJWHJWKSXJSXCOAOBCBJKAOJKVQYASCRWBJKXNJWKMRSXOJVOKAXSXQ";
		CrackCaesar cracker = new CrackCaesar();
		cracker.crackCaesar(cipher);
	}
}
