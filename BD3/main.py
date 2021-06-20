import pandas
from sklearn import feature_extraction
import numpy


def save_to_file(fileName, array):
    with open(fileName, 'w') as file:
        for item in array:
            for i in item:
                file.write(str(i) + ' ')
            file.write('\n')
        file.close()


if __name__ == '__main__':
    # Reading dataset from csv file
    data = pandas.read_csv('all-data.csv')
    max_element_count = 5000

    # Positive
    positive_news = data[(data.Sentiment == 'positive')][:max_element_count]
    count = feature_extraction.text.CountVectorizer()
    tfidf = feature_extraction.text.TfidfVectorizer()
    bag = count.fit_transform(positive_news.News_Headline)
    bag_tfidf = tfidf.fit_transform(positive_news.News_Headline)
    save_to_file("bag_potitive.txt", bag.toarray())
    save_to_file("TF_IDF_potitive.txt", bag_tfidf.toarray())

    ind = numpy.argsort(tfidf.idf_)[::-1]
    features = tfidf.get_feature_names()
    top_n = 10
    top_features = [features[i] for i in ind[:top_n]]
    print('Top {} words in positive sentiment.'.format(top_n))
    print(top_features)

    # Negative
    data_negative = data[(data.Sentiment == 'negative')][:max_element_count]
    count = feature_extraction.text.CountVectorizer()
    tfidf = feature_extraction.text.TfidfVectorizer()
    bag = count.fit_transform(data_negative.News_Headline[:1000])
    bag_tfidf = tfidf.fit_transform(data_negative.News_Headline[:1000])
    save_to_file("bag_negative.txt", bag.toarray())
    save_to_file("TF_IDF_negative.txt", bag_tfidf.toarray())

    ind = numpy.argsort(tfidf.idf_)[::-1]
    features = tfidf.get_feature_names()
    top_n = 10
    top_features = [features[i] for i in ind[:top_n]]
    print('Top {} words in negative sentiment.'.format(top_n))
    print(top_features)
