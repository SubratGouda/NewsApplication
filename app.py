from flask import Flask,render_template
from newsapi import NewsApiClient
 


app = Flask(__name__)

@app.route('/')
def home():
    # endter client id and api_key for authorization

    newsapi = NewsApiClient(api_key = "86aa2dd2c24145ed9ed67ae5e5cb0a48")

    #for top headlines of news, we will code
    top_headlines = newsapi.get_top_headlines(sources = 'bbc-news')

    #source is meant by, where the news comes into your app by api
    all_article = newsapi.get_everything(sources = 'bbc-news')
    # fetch all the articles of the top headline news
    t_artilces = top_headlines['articles']
    a_artilces = all_article['articles']

    # make a list of contents to store the calues on that list
    news = []
    desc = []
    img = []
    p_date = []
    url = []

    # fetch all the contents of articles by using for loop
    for i in range(len(t_artilces)):
        main_article = t_artilces[i]

        # Atlast append all the contents in to each of list
        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])

        # make a zip for find the contents directly and shortly
        

    # make a list of contents to store the calues on that list
    news_all = []
    desc_all = []
    img_all = []
    p_date_all = []
    url_all = []

    # fetch all the contents of articles by using for loop
    for i in range(len(a_artilces)):
        main_article = a_artilces[i]

        # Atlast append all the contents in to each of list
        news_all.append(main_article['title'])
        desc_all.append(main_article['description'])
        img_all.append(main_article['urlToImage'])
        p_date_all.append(main_article['publishedAt'])
        url_all.append(main_article['url'])

        # make a zip for find the contents directly and shortly
        contents  = zip(news,desc,img,p_date,url)
        all  = zip(news_all,desc_all,img_all,p_date_all,url_all)
   

    # pass it in render file    
    return render_template("home.html", contents = contents, all = all)


if __name__ == '__main__':
    app.run(debug=True)