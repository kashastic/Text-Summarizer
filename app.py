from __future__ import unicode_literals
from flask import Flask, render_template, request

from spacy_summarization import text_summarizer
import time
import spacy

nlp = spacy.load("en_core_web_sm")
app = Flask(__name__)

# Web Scraping Pkg
from bs4 import BeautifulSoup
# from urllib.request import urlopen
from urllib.request import urlopen


# Reading Time
def readingTime(mytext):
    total_words = len([token.text for token in nlp(mytext)])
    estimatedTime = total_words / 200.0
    return estimatedTime


# Fetch Text From Url
def get_text(url):
    page = urlopen(url)
    soup = BeautifulSoup(page)
    fetched_text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return fetched_text


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    start = time.time()
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        final_reading_time = readingTime(rawtext)
        final_summary = text_summarizer(rawtext)
        summary_reading_time = readingTime(final_summary)
        end = time.time()
        final_time = end - start
    return render_template('index.html', ctext=rawtext, final_summary=final_summary, final_time=final_time,
                           final_reading_time=final_reading_time, summary_reading_time=summary_reading_time)


@app.route('/analyze_url', methods=['GET', 'POST'])
def analyze_url():
    start = time.time()
    if request.method == 'POST':
        raw_url = request.form['raw_url']
        rawtext = get_text(raw_url)
        final_reading_time = readingTime(rawtext)
        final_summary = text_summarizer(rawtext)
        summary_reading_time = readingTime(final_summary)
        end = time.time()
        final_time = end - start
    return render_template('index.html', ctext=rawtext, final_summary=final_summary, final_time=final_time,
                           final_reading_time=final_reading_time, summary_reading_time=summary_reading_time)


@app.route('/compare_summary')
def compare_summary():
    return render_template('compare_summary.html')


@app.route('/about')
def about():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

#source for website links: https://blog.feedspot.com/indian_news_websites
"""stringUrl = "https://www.w3schools.com/python/ref_string_split.asp"
random = stringUrl.split('//')[1]
domainNme = random.split('/')[0]
if(domainNme.count('www')>0):
  domainNme = domainNme[4:]
domains = ['timesofindia.indiatimes.com','ndtv.com','google.com','hindustantimes.com','indiatoday.in','indianexpress.com','thehindu.com','news18.com','business-standard.com','dnaindia.com','deccanchronicle.com',
'swachhindia.ndtv.com', 'oneindia.com', 'scroll.in','financialexpress.com', 'thehindubusinessline.com', 'freepressjournal.in', 'outlookindia.com', 'thequint.com',
'telanganatoday.com', 'socialsamosa.com', 'tentaran.com', 'dkoding.in','informalnewz.com','powersportz.tv','yovizag.com','orissapost.com','dailyexcelsior.com',
'techgenyz.com', 'sinceindependence.com', 'editorji.com', 'asianage.com', 'doonhorizon.in', 'chandigarhmetro.com', 'easternherald.com','seelatest.com', 'apnlive.com'
,'abcrnews.com','starofmysore.com', 'bhaskarlive.in', 'leagueofindia.com', 'arunachaltimes.in', 'abcrnews.com', 'newstodaynet.com', 'letmethink.in', 'indianyug.com', 'headlinesoftoday.com',
'timesnowindia.com', 'thenorthlines.com', 'gudstory.com', 'quintdaily.com', 'knnindia.co.in/home', 'kashmirreader.com', 'thenewsglory.com', 'navhindtimes.in',
'newsblare.com', 'reviewminute.com', 'news4masses.com', 'teluguglobal.in', 'emitpost.com', 'ndnewsexpress.com', 'thetimesofbengal.com', 'oibnews.com',
'newsdeets.com', 'startupreporter.in', 'hellovizag.online', 'asian-times.com', 'krooknews.com', 'thenewshimachal.com', 'jknewsline.com', 'topblogmania.com',
'tricksnhub.com', 'delhincrnews.in', 'indiareal.in', 'indiaobservers.com', 'notabletoday.blogspot.com', 'goodnewwws.in']
boolean = False
if(domains.count(domainNme)):boolean =True
print(domainNme,boolean)"""