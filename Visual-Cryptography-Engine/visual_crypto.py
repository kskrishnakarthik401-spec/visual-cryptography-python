import random
from PIL import Image

def generate_shares(image_path):
    # 1. Load the secret image and convert it to absolute Black & White (Binary)
    img = Image.open(image_path).convert('1')
    width, height = img.size
    
    # 2. Create two new blank images twice the size for the 2x2 sub-pixels
    share1 = Image.new('1', (width * 2, height * 2))
    share2 = Image.new('1', (width * 2, height * 2))
    
    # 3. Define the sub-pixel patterns (0 = white/transparent, 1 = black)
    # Pattern A and Pattern B are complements of each other
    pattern_A = [(1, 0), 
                 (0, 1)]
    pattern_B = [(0, 1), 
                 (1, 0)]
    
    # 4. Loop through every pixel of the original secret image
    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            
            # Coin toss to randomize the shares so individual shares look like noise
            flip = random.choice([True, False])
            
            if pixel == 255: # Pixel is WHITE
                # For white, both shares get the EXACT SAME pattern
                chosen_p1 = pattern_A if flip else pattern_B
                chosen_p2 = pattern_A if flip else pattern_B
            else: # Pixel is BLACK
                # For black, shares get OPPOSITE patterns
                chosen_p1 = pattern_A if flip else pattern_B
                chosen_p2 = pattern_B if flip else pattern_A
            
            # 5. Write the 2x2 sub-pixels into Share 1 and Share 2
            for i in range(2):
                for j in range(2):
                    share1.putpixel((x*2 + i, y*2 + j), chosen_p1[i][j])
                    share2.putpixel((x*2 + i, y*2 + j), chosen_p2[i][j])
                    
    # Save the output shares
    share1.save("share1.png")
    share2.save("share2.png")
    print("Shares generated successfully!")

def reconstruct_secret(share1_path, share2_path):
    s1 = Image.open(share1_path).convert('L')
    s2 = Image.open(share2_path).convert('L')
    
    # Digitally overlay the shares
    reconstructed = Image.blend(s1, s2, 0.5)
    
    # ENHANCEMENT: Boost contrast to eliminate the gray overlay
    # Any pixel lighter than mid-gray (128) becomes pure white (255)
    # This acts like placing the transparency sheets physically over a light box
    enhanced = reconstructed.point(lambda p: 255 if p > 140 else 0, mode='1')
    
    enhanced.save("reconstructed_secret_clear.png")
    print("Highly visible secret saved as reconstructed_secret_clear.png!")

# Run the project
if __name__ == "__main__":
    # Update this path to where your file actually lives on your PC
    generate_shares(r"C:\Users\K S KRISHNA KARTHIK\Downloads\secret.png")
    reconstruct_secret("share1.png", "share2.png")
