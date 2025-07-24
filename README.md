# bank-churn-prediction  
銀行客戶流失預測專案  
📊 **Bank Customer Churn Prediction**

預測顧客是否即將流失，協助企業提前介入留客，掌握商業生命週期價值。  
本專案以 Logistic Regression 與 Random Forest 進行監督式學習，並透過資料視覺化進行分析，導出適合的建模架構與推薦的商業策略。

---

## 📁 專案結構

bank-churn-prediction/
├── data/ # 原始資料與處理後資料
├── images/ # 圖表與模型輸出圖
├── notebook/ # Jupyter Notebook 主程式
├── README.md # 專案說明文件

---

## 📌 專案背景

金融機構在提升業績的同時，透過精準建模找出流失目標，用於提升顧客服務與客戶關係管理（CRM）場景，例如：

- 客戶關懷
- 產品推薦
- 精準行銷策略

---

## 🧠 使用技術

- 程式語言：Python  
- 分析工具：Pandas, NumPy, Matplotlib, Seaborn  
- 機器學習：Scikit-learn（Logistic Regression, Random Forest）  
- 評估指標：混淆矩陣 / Precision / Recall / F1-score  
- 資料視覺化：Heatmap、Bar Chart  

---

## 🔁 專案流程

### 📓 專案主程式碼  
主程式碼位於 [`notebook/bank_churn_prediction.ipynb`](notebook/bank_churn_prediction.ipynb)，以 Jupyter Notebook 撰寫，涵蓋資料載入、前處理、模型訓練、模型評估與視覺化等完整流程，並以 Markdown 說明每個步驟的邏輯與分析重點，便於閱讀與學習。

### 1. 資料預處理階段  
- 標籤編碼處理：Label Encoding  
- 欄位篩選、特徵數值化  

### 2. 模型建立訓練  
- Logistic Regression  
- Random Forest  

### 3. 預測與評估  
- 混淆矩陣圖 (Confusion Matrix Heatmap)  
- 特徵重要性圖 (Bar Chart)  

### 4. 模型準確性與建議策略洞察💡

---

## 📈 成效亮點

---

## 🔍 結果洞察與商業應用策略

### 📌 模型分析洞察：
- **準確率對比：** Random Forest 表現優於 Logistic Regression，能更精準掌握流失客戶特徵。
- **特徵影響力：** 客戶的「信用評分（Credit Score）」與「帳戶活躍狀態（Is Active Member）」為最重要的流失指標。
- **模型優化潛力：** 雖然模型準確率達標，但在召回率與 F1-score 上仍有優化空間，未來可嘗試 XGBoost 或調參以提升表現。

### 💼 商業應用建議：
- **高風險客戶提前預警：** 對預測結果為流失風險高者，提前以簡訊、專人聯繫等方式進行關懷行動。
- **建立個人化推薦機制：** 利用關鍵特徵如「產品持有數」、「是否為活躍用戶」等，提供定制化產品或優惠。
- **強化客戶參與度：** 對於活躍度低者推出專屬活動、獎勵制度，提高黏著度與續留率。

📣 **策略價值**：透過此預測模型，銀行可節省大幅的行銷成本，並將資源聚焦於高風險群體，有效提升整體留存率與客戶終身價值（CLV）。


### 🔍 模型比較圖：
![Model Comparison](images/model_comparison.png)

### 📊 Logistic Regression 混淆矩陣：
![Logistic Confusion Matrix](images/confusion_logistic.png)

### 🌲 Random Forest 混淆矩陣：
![RF Confusion Matrix](images/confusion_rf.png)

### 🎯 特徵重要性分析（以 Logistic 為例）：
![Feature Importance](images/feature_importance_logistic.png)
