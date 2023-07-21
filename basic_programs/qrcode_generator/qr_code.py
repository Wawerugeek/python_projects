#!/usr/bin/python3

import qrcode

def generate_qr_code(url, save_path):
    qr = qrcode(version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="blue", back_color="white")
    img.save(save_path)
    
if __name__ == "__main__":
    website_url = "https://github.com/Wawerugeek"
    qr_code_path = "qrcode_example.png"
    generate_qr_code(website_url, qr_code_path)
