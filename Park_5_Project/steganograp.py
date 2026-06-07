import argparse
import sys
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

from PIL import Image
from pathlib import Path


class Steganography:
    DELIMITER = b"<<END>>"

    def __init__(self, image_path:str):
        self.image_path = image_path
        self.img = Image.open(image_path).convert("RGB")
        self.pixels = list(self.img.getdata())
    
    def _bytes_to_bits(self, data:bytes) -> list:
       bits = []
       for byte in data:
        for i in range(7,-1,-1):
            bits.append((byte >> i) & 1)
       return bits

    def _bits_to_bytes(self, bits:list) -> bytes:
        result = bytearray()
        for i in range(0,len(bits),8):
            byte = 0
            for bit in bits[i:i+8]:
                byte = (byte << 1) | bit
            result.append(byte)
        return bytes(result)
    
    def _kapasitas(self) -> int:
        return len(self.pixels) * 3 // 8 
    
    def embed(self, secret_path:str, output_path:str):
        data = Path(secret_path).read_bytes() + self.DELIMITER

        if len(data) > self._kapasitas():
            print(f"Error: Data terlalu besar untuk disembunyikan dalam gambar ini. Kapasitas maksimum adalah {self._kapasitas()} bytes.")
            sys.exit(1)
        bits = self._bytes_to_bits(data)
        new_pixels = list(self.pixels)
        bit_index = 0
        for i, (r, g, b) in enumerate(self.pixels):
            if bit_index >= len(bits):
                break
            channels = [r, g, b]
            for j in range(3):
                if bit_index < len(bits):
                    channels[j] = (channels[j] & ~1) | bits[bit_index]
                    bit_index += 1
            new_pixels[i] = tuple(channels)

        output_image = Image.new("RGB", self.img.size)
        output_image.putdata(new_pixels)
        output_image.save(output_path,format="PNG")
        print(f"Data berhasil disembunyikan dalam {secret_path} dan disimpan sebagai {output_path}")
        print(f"Ukuran data yang disembunyikan: {len(data)} bytes")
        print(f"Kapasitas maksimum gambar: {self._kapasitas()} bytes")


def main():
    parser = argparse.ArgumentParser(description="Steganography Tool")
    parser.add_argument("--image", help="Path to the image file (PNG format)")
    parser.add_argument("--secret", help="Path to the secret file to embed")
    parser.add_argument("--output", help="Path to save the output image (PNG format)")
    args = parser.parse_args()
    steg = Steganography(args.image)
    steg.embed(args.secret, args.output)

if __name__ == "__main__":
    main()