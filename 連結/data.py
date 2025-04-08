import definition
import time

counter = 0
callback = None
MAX_RETRIES = 3
RETRY_DELAY = 3

def data():
    global callback
    retry_count = 0
    
    while retry_count < MAX_RETRIES:
        try:
            # 嘗試連接藍牙設備
            if not definition.bt.connected:
                print(f"嘗試連接藍牙設備... (第{retry_count + 1}次)")
                if not definition.bt.connect():
                    print("無法連接到ESP32藍牙設備")
                    retry_count += 1
                    if retry_count < MAX_RETRIES:
                        print(f"等待{RETRY_DELAY}秒後重試...")
                        time.sleep(RETRY_DELAY)
                    continue
            
            print("藍牙連接成功，等待數據...")
            while counter == 0:
                if definition.bt.in_waiting:
                    data_raw = definition.bt.readline()  # 讀取數據
                    try:
                        data = data_raw.decode()  # 解碼數據
                        callback = str(data)
                        return callback
                    except UnicodeDecodeError:
                        print("數據解碼錯誤，重試中...")
                        time.sleep(1)
                        continue
                time.sleep(0.1)  # 避免CPU過度使用
                
        except KeyboardInterrupt:
            print("使用者中斷連接")
            definition.bt.disconnect()
            break
        except Exception as e:
            print(f"錯誤：{e}")
            definition.bt.disconnect()
            retry_count += 1
            if retry_count < MAX_RETRIES:
                print(f"等待{RETRY_DELAY}秒後重試...")
                time.sleep(RETRY_DELAY)
            
    print("已達到最大重試次數，連接失敗")
    return None
