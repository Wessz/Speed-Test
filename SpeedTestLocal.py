import speedtest

speed = speedtest.Speedtest()

def bytes_to_mb (bytes):
    KB = 1024
    MB = KB * 1024
    return int (bytes/MB)

speed_download = speed.download()
speed_upload = speed.upload()
server = speed.get_best_server()
ip_address_name = server['host'].split(':')[0]
ip_address = speed.results.client['ip']

print(f"Download: {bytes_to_mb(speed_download)}MB")
print(f"Upload: {bytes_to_mb(speed_upload)}MB")
print(f"IP_Name_Server: {ip_address_name}")
print(f"IP: {ip_address}")