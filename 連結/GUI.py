import tkinter as tk
import definition
import time
import numpy as np
from PIL import Image, ImageTk

def update_data():
    # 這個函數將定期更新 updata 變數和圖像
    current_time = time.strftime("%H:%M:%S")
    updata.set(current_time)
    update_image()
    window.after(1000, update_data)  # 每秒更新一次

def update_image():
    # 這個函數用於更新圖像
    # 這裡可以添加從ESP32接收數據並轉換為圖像的邏輯
    # 暫時使用一個示例圖像（100x100的灰度圖）
    image_data = np.random.randint(0, 255, (100, 100), dtype=np.uint8)
    image = Image.fromarray(image_data)
    photo = ImageTk.PhotoImage(image)
    canvas.delete("all")
    canvas.create_image(100, 100, image=photo)
    canvas.image = photo  # 保持引用以防止垃圾回收

def GUI():
    global window, updata, canvas
    # 視窗
    window = tk.Tk()
    window.title("監控視窗")
    window.minsize(400, 500)

    # 創建左側按鈕框架
    button_frame = tk.Frame(window)
    button_frame.pack(side=tk.LEFT, padx=10, pady=10)

    # 初始化 updata 為 StringVar
    updata = tk.StringVar()
    updata.set("Initializing...")

    # 按鈕
    upbtn = tk.Button(button_frame, text="up", command=definition.up)
    downbtn = tk.Button(button_frame, text="down", command=definition.down)
    laftbtn = tk.Button(button_frame, text="laft", command=definition.laft)
    rightbtn = tk.Button(button_frame, text="right", command=definition.right)
    teastupbnt = tk.Button(button_frame, text="teastup", command=definition.teastup)
    teastdownbnt = tk.Button(button_frame, text="teastdown", command=definition.teastdown)
    datatext = tk.Label(button_frame, textvariable=updata)

    upbtn.pack(pady=2)
    downbtn.pack(pady=2)
    laftbtn.pack(pady=2)
    rightbtn.pack(pady=2)
    teastupbnt.pack(pady=2)
    teastdownbnt.pack(pady=2)
    datatext.pack(pady=10)

    # 創建右側圖像顯示區域
    image_frame = tk.Frame(window)
    image_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

    # 創建Canvas用於顯示圖像
    canvas = tk.Canvas(image_frame, width=200, height=200, bg='white')
    canvas.pack(padx=5, pady=5)

    # 開始更新數據和圖像
    update_data()

    window.mainloop()
