import java.security.MessageDigest;
import java.security.SecureRandom;
import java.util.Base64;

public class IdentityVault {

    // 1. Generate a secure, high-entropy 16-byte cryptographic salt
    public static String generateSalt() {
        SecureRandom random = new SecureRandom();
        byte[] saltBytes = new byte[16];
        random.nextBytes(saltBytes);
        return Base64.getEncoder().encodeToString(saltBytes);
    }

    // 2. Hash the raw password combined with the unique salt using SHA-256
    public static String computeSHA256(String password, String salt) {
        try {
            MessageDigest digest = MessageDigest.getInstance("SHA-256");
            
            // Combine salt and password to stop pre-computed rainbow table attacks
            String combinedInput = salt + password;
            byte[] hashBytes = digest.digest(combinedInput.getBytes("UTF-8"));
            
            // Convert byte array into readable hexadecimal format
            StringBuilder hexString = new StringBuilder();
            for (byte b : hashBytes) {
                String hex = Integer.toHexString(0xff & b);
                if (hex.length() == 1) hexString.append('0');
                hexString.append(hex);
            }
            return hexString.toString();
            
        } catch (Exception e) {
            throw new RuntimeException("Cryptographic hashing algorithm execution failed.", e);
        }
    }

        public static void main(String[] args) {
        String inputPassword = "K_S_Krishna_Karthik_SRFP_2026";
        System.out.println("[INFO] Original Plaintext Password: " + inputPassword);

        // Simulate Account Creation Phase
        String generatedSalt = generateSalt();
        String savedHash = computeSHA256(inputPassword, generatedSalt);
        
        System.out.println("\n[SQL] Simulating SQL Insertion Operations...");
        System.out.println("💾 [SQL Field] Cryptographic Salt: " + generatedSalt);
        System.out.println("💾 [SQL Field] Secure Hex Hash:    " + savedHash);

        // Simulate Login Verification Phase
        System.out.println("\n[AUTH] Simulating Authentication Attempt...");
        String loginAttemptHash = computeSHA256("K_S_Krishna_Karthik_SRFP_2026", generatedSalt);
        
        if (loginAttemptHash.equals(savedHash)) {
            System.out.println("[SUCCESS] Access Granted: Tokens match system constraints.");
        } else {
            System.out.println("[ERROR] Access Denied: Invalid credentials.");
        }
    }

}
