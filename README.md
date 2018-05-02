Assignment I

作業：利用機器學習的線性學習解碼圖片<br>
環境：python<br>
套件：PIL,numpy<br>

此次作業需先讓電腦學習係數w1,w2,w3<br>
因為我們將透過這三個係數進行解碼的動作<br>
以下圖片分別為：E, key1, key2, I<br>
![Alt text](https://i.imgur.com/MVuxpAd.png)<br>
![Alt text](https://i.imgur.com/rVmENhi.png)<br>
![Alt text](https://i.imgur.com/Kgkiw8l.png)<br>
![Alt text](https://i.imgur.com/2pCFI43.png)<br>

其中E為key1, key2, I分別乘上w1, w2, w3在疊在一起的結果<br>
表示式為：E = key1Xw1 + key2Xw2 + IXw3<br>
所以我們需要透過逼近法讓機器去學習，並得到三個w分別的值<br>
然後我們會載入另一張加密的圖Eprime<br>
![Alt text](https://i.imgur.com/tYxXyCP.png)<br>
透過一樣的表示式，將w分別帶入並進行解碼<br>

python：<br>
![Alt text](https://i.imgur.com/dTzAdOE.jpg)<br>
這個部分我先將所有圖片開檔，並用numpy轉成二維數字陣列<br>
為了方便學習時的for迴圈進行，這邊用numpy裡的flatten函式將數字陣列打成一維<br>

![Alt text](https://i.imgur.com/ao0pbdu.jpg)<br>
再來進入學習的部分<br>
我將五張圖片分別傳進函式Learning<br>
![Alt text](https://i.imgur.com/zywAXa9.jpg)<br>
並宣告w陣列存放三個w的值(初始為0)及一個極小值apha<br>

其中在我的象素中(WXH)，我們讓每一張圖的第x象素開始學習<br>
a存放三張圖片(key1, key2, I)的第x個象素乘上各自對應的w值<br>
照理來說，這個值要等於E的第x個象素的值，因此我們利用E-a來找誤差並存放到e<br>
然後我們將目前的w值進行微調，這邊會用到先前宣告的極小值和我們得到的誤差進行調整<br>
使用極小值的關係是為了要更精確地逼近解答<br>

我們將重複這個步驟直到學習到最準確的w值<br>
以下為學習到的w1, w2, w3<br>
![Alt text](https://i.imgur.com/WFLYFDu.jpg)<br>

學到w後，我們將利用這三個w值再帶入來得到Eprime的原始圖片<br>
我宣告了一個長度為HXW的陣列ans，用來存放計算到的值<br>
原式為：Eprime = key1Xw1 + key2Xw2 + ansXw2<br>
為了得到ans的值，所以將式子轉為：ans = (Eprime - key1Xw1 - key2Xw2) / w3<br>
再用reshpae的函示將ans轉回正確的HXW的二維陣列<br>
![Alt text](https://i.imgur.com/BArkb08.jpg)<br>

將最後的ans轉回圖片的結果如下：<br>
![Alt text](https://i.imgur.com/yiQFMeH.jpg)<br>

遇到的問題：<br>
1. 步驟中應該需要利用一個while確定學習的過程中不會因為始終學不到w值而形成無窮迴圈，但是我加上while後程式卻出現error,所以先mark起來<br>
2. 想要將ans圖片存為jpg或png檔案，但是一直無法正確存檔<br>

