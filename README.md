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
2. 想要將ans圖片存為jpg或png檔案，但是一直無法正確存檔<br><br><br>


Assignment II

作業：利用sklearn進行手寫辨識<br>
環境：Python<br>
套件：sklearn, matplotlib, scipy, numpy<br>


此次作業之database都可以在sklearn中找到，因此可以直接使用datasets.load_digits()將資料抓出來。<br>
利用以下程式碼進行訓練<br>
images_and_labels = list(zip(digits.images, digits.target))<br>
for index, (image, label) in enumerate(images_and_labels[:4]):<br>
    plt.subplot(2, 4, index + 1)<br>
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')<br>
    plt.title('Training: %i' % label)<br>

訓練時，會一併儲存每一張圖片的數字是甚麼，方便讓電腦學習後面的數據，實際數字存在digits.target變數中<br><br>

用reshape將影像打平成64x1的矩陣。<br>
然後用classifier = svm.SVC(gamma=0.001)來產生一個SVC分類器。<br>
將一半的資料送入分類器訓練classifier.fit。<br>
其中SVC(gamma=0.001)是在設定$$\gamma$$ 這個值要大於零。<br>
利用後半部份的資料來測試訓練完成之SVC分類機predict(data[n_samples / 2:])並將預測結果存入predicted。<br>
原本的正確數字存在expected，用來做準確度統計。<br><br>

使用sklearn的metrics.confusion_matrix)可以列出下面矩陣。<br>
![Alt text](https://i.imgur.com/r9G0MRi.jpg)<br>
此矩陣對角線左上方第一個數字 87，代表實際為0且預測為0的總數有87個，但誤判為4的資料個數為1個,依此類推。<br>
可以利用numpy來產生圖表觀察誤判的程度：<br>
![Alt text](https://i.imgur.com/hPxyIwR.jpg)<br>
比較明顯的例子可以看到學習過程中，實際為三的數字曾誤判為5.7.8，這個數據也反映在矩陣上。<br><br>

報表：<br>
![Alt text](https://i.imgur.com/Khvmydm.jpg)<br>
報表代表著實際為手寫數字的總數。例如實際為0的數字共有88個，依此類推。<br>

訓練後，我們可以將影像再丟進程式，測試學習結果：<br>
![Alt text](https://i.imgur.com/tnvukpW.jpg)<br>
上列為訓練的數字影像，下列為訓練完的測試數字影像及結果。<br><br>

問題：<br>
此次作業，因為手寫辨識的發展已經很成熟，所以有很多資源可以參考，寫起來和理解起來也比較容易。<br>
唯一遇到的問題是一開始不知道sklrean需要用到scipy的套件，所以程式一直error，載入scipy後就沒什麼大問題了。

