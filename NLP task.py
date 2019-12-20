import pandas as pd
import numpy as np
import jieba
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

#读入训练集
def read_data(file1, file2, file3):
    news = pd.read_csv(file1, sep=',', encoding='utf-8').astype(str)
    lable = pd.read_csv(file2, sep=',', encoding='utf-8').astype(str)
    test = pd.read_csv(file3, sep=',',encoding='utf-8').astype(str)
    return news, lable, test

#将两个列表合并在一起
def merge_list(news, lable, test):
    data = news.merge(lable, on='id')
    #将标题和内容合并成X
    data['X'] = data['title'] + data['content']
    test['X'] = test['title'] + test['content']
    return data, test

#利用jieba切割
def cut_content(x):
    return ' '.join(jieba.cut(x))


#停用词
def stop_words(file_stop):
    stopwords = pd.read_csv(file_stop, index_col=False, sep='\t', quoting=3, names=["stopword"], encoding="utf-8")
    stop_word = []
    for stopword in stopwords['stopword']:
        stop_word.append(stopword)
    return stop_word

#tf-idf处理训练集和测试集
def tf_idf_method(data, test, stop_word):
    vectorizer = CountVectorizer(max_df=0.8, min_df=3, token_pattern=u'(?u)\\b[^\\d\\W]\\w+\\b',
                                 stop_words=frozenset(stop_word))
    transformer = TfidfTransformer()
    xTrain_tfidf = transformer.fit_transform(vectorizer.fit_transform(data['X_split']))
    xTest_tfidf = transformer.transform(vectorizer.transform(test['X_split']))
    yTrain = data['label']
    return xTrain_tfidf, xTest_tfidf, yTrain

#预测测试集
def predict(logistic, xTest_tfidf, test):
    preds = logistic.predict_proba(xTest_tfidf)
    preds = np.argmax(preds, axis=1)
    test_preds = pd.DataFrame(preds)
    test_preds.columns = ['label']
    test_id = test['id'].tolist()
    test_preds['id'] = test_id
    return test_preds

file1 = 'F:\Train\Train_DataSet.csv'
file2 = 'F:\Train\Train_DataSet_Label.csv'
file3 = 'F:\Test\Test_DataSet.csv'
file_stop = 'F:\stop_words_zh.txt'
news, table, test = read_data(file1, file2, file3)
data, test = merge_list(news, table, test)
stop_word = stop_words(file_stop)

data['X_split'] = data['X'].apply(cut_content)
test['X_split'] = test['X'].apply(cut_content)

xTrain_tfidf, xTest_tfidf, yTrain = tf_idf_method(data, test, stop_word)

logistic = LogisticRegression(C=4, dual=True)
logistic.fit(xTrain_tfidf, yTrain)

test_preds = predict(logistic,xTest_tfidf,test)
test_preds[["id", "label"]].to_csv('E:\sub_lr_baseline.csv', index=None)
