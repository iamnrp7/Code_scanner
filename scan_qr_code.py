from PIL import Image
from pyzbar.pyzbar import decode

def scan_qr_code(image_path):
    try:
        image = Image.open(image_path)
        decoded_objects = decode(image)

        qr_code_results = []  # Initialize a list to store results

        if decoded_objects:
            for obj in decoded_objects:
                data = obj.data.decode('utf-8')
                qr_code_results.append(data)  # Append the result to the list

        if qr_code_results:
            return qr_code_results  # Return the list of results
        else:
            return ["No QR codes found in the image"]

    except Exception as e:
        return ["An error occurred: " + str(e)]
