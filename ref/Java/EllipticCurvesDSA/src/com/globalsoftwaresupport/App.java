package com.globalsoftwaresupport;

import java.io.IOException;
import java.security.GeneralSecurityException;
import java.security.KeyPair;
import java.security.Security;
import java.util.Base64;

import org.bouncycastle.jce.provider.BouncyCastleProvider;
import org.bouncycastle.operator.OperatorCreationException;

public class App {

	public static void main(String[] args) {
		
		// define the provider (BC)
		Security.addProvider(new BouncyCastleProvider());

		KeyPair keys = CryptographyHelper.generateKeys();
		
		try {
			System.out.println(CertificateBuilder.makeV1Certificate(keys.getPrivate(), keys.getPublic()));
		} catch (OperatorCreationException | GeneralSecurityException | IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

}
