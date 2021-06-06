# Amgi
A handy python script that helps automating the normally tedious process of creating cards for Anki.

## Introduction
[Anki](https://apps.ankiweb.net/) is an indispensable tool for everyone learning a foreign language. If you somehow stumbled upon this small app I suppose you already know what it is. If by chance not I highly encourage to check it out. It is of tremendous use even beyond the study of languages. The creation of personalized flash cards for Anki can be incredible time consuming though. Even to create one signle card for a word that you looked up at some online dictionary with all the information that a single entry has to offer can take minutes, which multiplicates onto hours if you try to add a bunch of them together. 

There are incredible ressources for other languages like Japanese to help with the creation of Anki flash cards, but unfortunately I haven't found a good one for Korean yet. So I just thought I might as well create one myself!

### The Basic Korean Dictionary
As someone who is currently learning Korean I have been on the look for a good online dictionary for quite some time now. Luckily I found one in the [Basic Korean Dictionary](https://krdict.korean.go.kr/eng/mainAction?nation=eng) of the National Institute of the Korean Language. But even better than just the dictionary itself are the premade vocabulary list which are grouped by topic and ranked in order of their level of difficulty, ranging from beginner to advanced. While starting out to learn a new languge I consider the most important part the acquisition of a solid base vocabulary. These [lists](https://krdict.korean.go.kr/eng/dicSearchDetail/searchDetailActCategory?nation=eng&nationCode=6&searchFlag=N&sort=W&currentPage=1&ParaWordNo=&syllablePosition=&actCategoryList=&all_gubun=ALL&gubun=W&gubun=P&gubun=E&all_wordNativeCode=ALL&wordNativeCode=1&wordNativeCode=2&wordNativeCode=3&wordNativeCode=0&all_sp_code=ALL&sp_code=1&sp_code=2&sp_code=3&sp_code=4&sp_code=5&sp_code=6&sp_code=7&sp_code=8&sp_code=9&sp_code=10&sp_code=11&sp_code=12&sp_code=13&sp_code=14&sp_code=27&all_imcnt=ALL&imcnt=1&imcnt=2&imcnt=3&imcnt=0&all_multimedia=ALL&multimedia=P&multimedia=I&multimedia=V&multimedia=A&multimedia=S&multimedia=N&searchSyllableStart=&searchSyllableEnd=&searchOp=AND&searchTarget=word&searchOrglanguage=all&wordCondition=wordAll&query=&myViewWord=25039) may be the best way to build this foundation as fast as possible if you are a new Korean learner.

## Prerequisites
In order to download and create lists you have at first create an account at the [website](https://krdict.korean.go.kr/login/login) of the National Institute of the Korean Language. It's in Korean, but it's not too hard if you just use a common tool like [Google Translate](https://translate.google.de/) or [Papago](https://papago.naver.com/?sk=ko&tk=en).

In addition you should have Python (I used 3.9 but it should work up with older ones as well) as well as [Genanki](https://github.com/kerrickstaley/genanki).

## Usage
When downloading a list of words that you want to create some flash cards for choose XML as file type. 
