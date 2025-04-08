import time
import asyncio
from bleak import BleakClient, BleakScanner

class BluetoothConnection:
    def __init__(self):
        self.client = None
        self.connected = False
        self.target_name = "ESP32-BT"
        self.characteristic_uuid = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"  # ESP32 UART service
        self.received_data = bytearray()

    async def _connect(self):
        devices = await BleakScanner.discover()
        for d in devices:
            if d.name == self.target_name:
                self.client = BleakClient(d.address)
                await self.client.connect()
                self.connected = True
                print(f"成功連接到{self.target_name}")
                return True
        return False

    def connect(self):
        max_retries = 3
        retry_count = 0
        while retry_count < max_retries:
            try:
                print(f"嘗試連接到{self.target_name}... (第{retry_count + 1}次)")
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                result = loop.run_until_complete(self._connect())
                loop.close()
                if result:
                    return True
                print(f"找不到{self.target_name}設備")
                retry_count += 1
                if retry_count < max_retries:
                    print("等待3秒後重試...")
                    time.sleep(3)
            except Exception as e:
                print(f"連接錯誤: {e}")
                retry_count += 1
                if retry_count < max_retries:
                    print("等待3秒後重試...")
                    time.sleep(3)
        print("已達到最大重試次數，連接失敗")
        return False

    async def _disconnect(self):
        if self.client:
            await self.client.disconnect()
            self.connected = False

    def disconnect(self):
        if self.client:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self._disconnect())
            loop.close()

    async def _write(self, data):
        if self.connected:
            await self.client.write_gatt_char(self.characteristic_uuid, data)

    def write(self, data):
        if self.connected:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self._write(data))
            loop.close()

    async def _read(self):
        if self.connected:
            return await self.client.read_gatt_char(self.characteristic_uuid)
        return None

    def readline(self):
        if self.connected:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            data = loop.run_until_complete(self._read())
            loop.close()
            return data
        return None

    @property
    def in_waiting(self):
        return self.connected

bt = BluetoothConnection()
ser = bt  # 使用藍牙連接替代串口連接
time.sleep(2)
#控制電路
def up():
    ser.write(b'up\n')
    time.sleep(0.1)
def down():
    ser.write(b'down\n')
    time.sleep(0.1)
def laft():
    ser.write(b'laft\n')
    time.sleep(0.1)
def right():
    ser.write(b'right\n')
    time.sleep(0.1)

    ser.write(b'right\n')
    time.sleep(0.1)
def teastup():
    ser.write(b'teastup\n')
    time.sleep(0.1)
def teastdown():
        ser.write(b'teastdown\n')
        time.sleep(0.1)