# Twitter Injury Report Detection

This directory contains the twitter bot project submitted to *Unicode Research*,
an online teaching and research organization which provides classes and competitions
for students to engage in.

The goal of this project is to create a computer program that can classify injury
reports from twitter data in Baseball. The best model found during the 8-week course
and competition was a pre-trained RoBERTa Neural Network. The long-term goal of this
project is to collect all injury data possible for sports players so that a
more direct analysis of the impact of injuries can be completed.

Among all applicants, this project won 1st place for its direct impact/inspiration
on industry and soundness of research.

<center>

|  Model  |  Data Type  |  Sensitivity  | Specificity |  Precision  |  Accuracy  |  F1 Score  |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| kNN | TF-IDF | 0.9753 | 0.7833 | 0.9781 | 0.9577 | 0.9767 |
| Bernoulli NB | Boolean | 0.9893 | 0.6837 | 0.9566 | 0.9514 | 0.9727 |
| Multinomial NB | Count | **0.9913** | 0.6086 | 0.9383 | 0.9367 | 0.9641 |
| Random Forest | TF-IDF | 0.9792 | 0.8519 | 0.9855 | 0.9679 | 0.9824 |
| Random Forest | Boolean | 0.983 | 0.6201 | 0.9463 | 0.9365 | 0.9643 |
| SVM | TF-IDF | 0.9792 | 0.8519 | 0.9855 | 0.9679 | 0.9824 |
| LSTM | GloVe | 0.9748| 0.9651 | 0.9927 | 0.9731 | 0.9837 |
| GRU | GloVe | 0.9634 | 0.9502 | 0.9901 | 0.9613 | 0.9766 |
| XLNet | Pretrained | 0.9815 | 0.908 | 0.9789 | 0.9678 | 0.9802 |
| RoBERTa | Pretrained | **0.985** | 0.8242 | 0.9679 | 0.9598 | 0.9764 |
| DistilBERT | Pretrained | 0.9803 | 0.9231 | 0.9829 | 0.9699 | 0.9816 |
| XLM-RoBERTa | Pretrained | 0.9553 | 0.8544 | 0.9698 | 0.9382 | 0.9625 |

Table data on Sensitivity, Specificity etc. differs from the in-presentation table
due to different formulas being applied.

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
