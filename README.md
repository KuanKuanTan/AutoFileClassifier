# AutoFileClassifier 

您可以透過此程式選擇一個資料夾或磁碟來分類檔案，程式會自動將檔案分類並移動整理資料夾。

# 說明:

## 步驟:
1. 下載所有檔案  [Download ZIP](https://https://github.com/KuanKuanTan/AutoFileClassifier/archive/refs/heads/main.zip)
2. 確保能導入以下模型(應該只有customtkinter預設沒有安裝):
    1. customtkinter `pip install customtkinter`
    2. tkinter 
    3. requests
    4. re
    5. string
    6. os
    7. shutil
3. 申請(註冊)免費的[uClassify](https://uclassify.com/)，已獲得金鑰。
    1. 進入註冊頁面
    2. 完成註冊後進入管理中心的API Keys
    3. 複製讀取(Read)的金鑰
    4. 執行`main.py`，按下setting，在跳出視窗中的輸入方塊貼上金鑰，並按下儲存
       ![token示意圖](https://hackmd.io/_uploads/HyZfRDsm0.png)
4.  完成前置作業，使用時執行程式後點選**Select Folder**並選擇要整理的資料夾，選擇完成後按下**Start**便開始整理，整理完成後會跳出視窗通知整理成功，5秒後會自動關閉。
   
    ![success示意圖](https://hackmd.io/_uploads/r1Libuim0.png)
    
    ↑ 成功視窗示意圖

## 原理:
程式最初會掃描所選的資料夾中檔案和資料夾的**檔案名稱(資料夾名稱)**，並將所得到的檔案名稱(資料夾名稱)進行處理，把非文字的符號全部轉換成空白字元(例:text_text.txt→text text txt)以利辨識。接著會將其名稱透過uClssify的API透過機器學習模型進行分類主題，並將該檔案移至所屬主題的資料夾(此資料夾會依照主題名稱自動建立)。


## 聲明:
本專案供學術研究用，機器學習模型所分類的主題沒有很細，且模型沒有訓練中文，歸檔不一定會正確，請不要輕易的嘗試你有在用的資料夾，如果電腦毀了不負責任。
