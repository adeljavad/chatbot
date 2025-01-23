import rarfile
import base64

def encode_rar_to_text(rar_path, output_text_path):
    """
    فایل RAR را به یک متن base64 تبدیل می‌کند.
    
    :param rar_path: مسیر فایل RAR
    :param output_text_path: مسیر ذخیره فایل متنی خروجی
    """
    # خواندن فایل RAR به صورت بایت‌ها
    with open(rar_path, 'rb') as rar_file:
        rar_bytes = rar_file.read()
    
    # تبدیل بایت‌ها به base64 (متن)
    encoded_text = base64.b64encode(rar_bytes).decode('utf-8')
    
    # ذخیره متن در فایل خروجی
    with open(output_text_path, 'w') as text_file:
        text_file.write(encoded_text)

    print(f"فایل RAR به متن تبدیل و در {output_text_path} ذخیره شد.")

def decode_text_to_rar(text_path, output_rar_path):
    """
    متن base64 را به فایل RAR تبدیل می‌کند.
    
    :param text_path: مسیر فایل متنی حاوی متن base64
    :param output_rar_path: مسیر ذخیره فایل RAR خروجی
    """
    # خواندن متن از فایل
    with open(text_path, 'r') as text_file:
        encoded_text = text_file.read()
    
    # تبدیل متن به بایت‌ها
    rar_bytes = base64.b64decode(encoded_text.encode('utf-8'))
    
    # ذخیره بایت‌ها به عنوان فایل RAR
    with open(output_rar_path, 'wb') as rar_file:
        rar_file.write(rar_bytes)

    print(f"متن به فایل RAR تبدیل و در {output_rar_path} ذخیره شد.")

# مثال استفاده
if __name__ == "__main__":
    # مسیر فایل RAR ورودی
    input_rar_path = 'example.rar'
    
    # مسیر فایل متنی خروجی (encoded)
    output_text_path = 'a.txt'
    
    # مسیر فایل RAR خروجی (decoded)
    output_rar_path = 'decoded_output.rar'
    
    # تبدیل فایل RAR به متن
    # encode_rar_to_text(input_rar_path, output_text_path)
    
    # تبدیل متن به فایل RAR
    decode_text_to_rar(output_text_path, output_rar_path)