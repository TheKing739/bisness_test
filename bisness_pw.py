#-------------------------------------------------암호화 코드-------------------------------------------------------------
from cryptography.fernet import Fernet

key = b"Y2f5d05REHFL9JhXZ1bkVjMxztYlwJ34uxvqWC1eEAw="  # 배포 전 만든 키(아래 주석에 생성 코드 있음.)

fernet = Fernet(key)

email = "test@email.com"
expiry = "2025-07-31" 
hwid = "E7C08C1F-XXXX"  # 구매자 PC의 HWID

data = f"{email}|{expiry}|{hwid}"
token = fernet.encrypt(data.encode()).decode()

print("라이선스 키:", token)

#--------------------------------------------------------------------------------------------------------------
