import speedtest

speed = speedtest.Speetest()

def bytes_to_mb (bytes):
    KB = 1024
    MB = KB * 1024
    return int (bytes/MB)

speed_download = speed.download()
speed_upload = speed.speed_upload()
server = speed.get_best_server()
ip_address = server['host'].split(':')[0]

print(f"Download: {bytes_to_mb(speed_download)}MB")
print(f"Upload: {bytes_to_mb(speed_upload)}MB")
print(f"IP: {ip_address}")