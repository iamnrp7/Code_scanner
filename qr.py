import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

def scan_qr_code(image_path):
    try:
        image = Image.open(image_path)
        decoded_objects = decode(image)

        if decoded_objects:
            for obj in decoded_objects:
                data = obj.data.decode('utf-8')
                print(f"QR Code Data: {data}")
        else:
            print("No QR codes found in the image.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    image_path = r"C:\Users\nihar\Downloads\qrcode.png"
    scan_qr_code(image_path)
