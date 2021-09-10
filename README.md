# Twitter Injury Report Detection

This directory contains the twitter bot project submitted to *Unicode Research*,
an online teaching and research organization which provides classes and competitions
for students to engage in.

The goal of this project is to use a model that can classify injury
reports in Baseball from Twitter data. The best model found during the 8-week course
and competition was the pre-trained RoBERTa Neural Network. The long-term goal of this
project is to collect injury data possible for all sports players, classify the type of injury and create a website where this data can be displayed.

Among all applicants, this project won 1st place.

<center>

|  Model  |  Data Type / Epochs  |  Sensitivity  | Specificity |  Precision  |  F1 Score  |  Accuracy  |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| kNN | Boolean | 0.2734 | **0.9965** | 0.9182 | 0.4214 | 0.9058 |
| kNN | TF-IDF | 0.1957 | 0.9942 | 0.8294 | 0.3167 | 0.8941 |
| Bernoulli NB | Boolean | 0.8614 | 0.9486 | 0.7061 | 0.776 | 0.9377 |
| Multinomial NB | Count | 0.8614 | 0.9342 | 0.6525 | 0.7425 | 0.9251 |
| Logistic Regression | TF-IDF | 0.9373 | 0.9787 | 0.8629 | 0.8986 | 0.9735 |
| Random Forest | Boolean | 0.7631 | 0.9719 | 0.7959 | 0.7792 | 0.9458 |
| Random Forest | TF-IDF | 0.8502 | 0.9522 | 0.7184 | 0.7787 | 0.9394 |
| SVM | TF-IDF | 0.8661 | 0.9909 | 0.9315 | 0.8976 | 0.9752 |
| LSTM | 10 | 0.9353 | 0.985 | 0.9541 | 0.9466 | 0.9726 |
| GRU | 10 | 0.9226 | 0.9864 | 0.9577 | 0.9398 | 0.9705 |
| RoBERTa | 5 | 0.9478 | 0.9887 | **0.9664** | 0.957 | 0.9782 |
| XLM-RoBERTa | 5 | 0.9648 | 0.9855 | 0.9568 | 0.9608 | **0.9803** |
| XLNet | 5 | **0.9691** | 0.9841 | 0.953 | **0.9609** | **0.9803** |
| DistilBERT | 5 | 0.8706 | 0.9812 | 0.9393 | 0.9036 | 0.9536 |
| DistilBERT FT | 5 | 0.8861 | 0.9789 | 0.9333 | 0.9091 | 0.9557 |

</center>

The score most valued for our use case was the sensitivity, so we label the best
"classical" machine learning model and best neural net model with bold text. All 
classical models were trained on the full dataset (15,000 datapoints) using 
stratified sampling, while all Neural Networks were completed on a curated sample 
of the dataset (7,000 datapoints) to deal with class imbalance issues.

**Final Presentation on Google Slides:**

https://docs.google.com/presentation/d/14rEB-cdVIzm6ITT4htV-2WRAQc1vFt29-4AF6MiwzWw/edit?usp=sharing

**Final Presentation Video:**

https://www.youtube.com/watch?v=Ff__8mj2oAI&t=5740s&ab_channel=SwapneelMehta

**Unicode Research:**

https://djunicode.in/

*This Folder represents the most up-to-date version of the project. For seeing
the project as it looked a week after the Final Presentation, please see the
Sports Injury Classification Repository.*
