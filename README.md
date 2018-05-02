Assignment I

作業：利用機器學習的線性學習解碼圖片
環境：python
套件：PIL,numpy

此次作業需先讓電腦學習係數w1,w2,w3
因為我們將透過這三個係數進行解碼的動作
以下圖片分別為：E, key1, key2, I
![Alt text](https://i.imgur.com/MVuxpAd.png)
![Alt text](https://i.imgur.com/rVmENhi.png)
![Alt text](https://i.imgur.com/Kgkiw8l.png)
![Alt text](https://i.imgur.com/2pCFI43.png)

其中E為key1, key2, I分別乘上w1, w2, w3在疊在一起的結果
表示式為：E = key1Xw1 + key2Xw2 + IXw3
所以我們需要透過逼近法讓機器去學習，並得到三個w分別的值
然後我們會載入另一張加密的圖Eprime
![Alt text](https://i.imgur.com/tYxXyCP.png)
透過一樣的表示式，將w分別帶入並進行解碼

python：
![Alt text](https://i.imgur.com/dTzAdOE.jpg)
這個部分我先將所有圖片開檔，並用numpy轉成二維數字陣列
為了方便學習時的for迴圈進行，這邊用numpy裡的flatten函式將數字陣列打成一維

![Alt text](https://i.imgur.com/ao0pbdu.jpg)
再來進入學習的部分
我將五張圖片分別傳進函式Learning
![Alt text](https://i.imgur.com/zywAXa9.jpg)
並宣告w陣列存放三個w的值(初始為0)及一個極小值apha

其中在我的象素中(WXH)，我們讓每一張圖的第x象素開始學習
a存放三張圖片(key1, key2, I)的第x個象素乘上各自對應的w值
照理來說，這個值要等於E的第x個象素的值，因此我們利用E-a來找誤差並存放到e
然後我們將目前的w值進行微調，這邊會用到先前宣告的極小值和我們得到的誤差進行調整
使用極小值的關係是為了要更精確地逼近解答

我們將重複這個步驟直到學習到最準確的w值
以下為學習到的w1, w2, w3
![Alt text](https://i.imgur.com/WFLYFDu.jpg)

學到w後，我們將利用這三個w值再帶入來得到Eprime的原始圖片
我宣告了一個長度為HXW的陣列ans，用來存放計算到的值
原式為：Eprime = key1Xw1 + key2Xw2 + ansXw2
為了得到ans的值，所以將式子轉為：ans = (Eprime - key1Xw1 - key2Xw2) / w3
再用reshpae的函示將ans轉回正確的HXW的二維陣列
![Alt text](https://i.imgur.com/BArkb08.jpg)

將最後的ans轉回圖片的結果如下：
![Alt text](https://i.imgur.com/yiQFMeH.jpg)

遇到的問題：
1. 步驟中應該需要利用一個while確定學習的過程中不會因為始終學不到w值而形成無窮迴圈，但是我加上while後程式卻出現error,所以先mark起來
2. 想要將ans圖片存為jpg或png檔案，但是一直無法正確存檔

