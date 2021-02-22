# productivity

This project generates a classification model that predicts how my day was based on daily survey data. The raw survey data isn't publicly accessible due to its personal nature, but there is a preprocessed (and conveniently clean) version available in the [/data](https://github.com/onederekchen/productivity/tree/main/data) folder. Note that the dataset is very small so it's likely your model will underfit even with cross-validation. If you're interested, there is also a [more detailed explanation](https://www.onederekchen.com/productivity) of my metrics and a [live dashboard](https://docs.google.com/spreadsheets/d/1ORwShJnblmd8JJNeLKK99QFEP30jLv9L1VR-meBLqrI/edit#gid=2092913362) that I use every day. 

![](https://raw.githubusercontent.com/onederekchen/productivity/main/dashboard_example.PNG)

### Requirements

- jupyterlab 2.2.8+
- matplotlib 3.3.2+
- numpy 1.19.2+
- pandas 1.1.3+
- pickleshare 0.7.5+
- scikit-learn 0.23.2+
- seaborn 0.11.0+

### Installation

To generate a model from the latest source, clone the repository and run the classifier script.
```
git clone https://github.com/onederekchen/productivity
cd productivity/model
python classify_data.py
```
