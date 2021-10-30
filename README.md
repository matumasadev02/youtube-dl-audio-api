# youtube-dl-audio-api
 
This is an api that uses youtube-dl to return the audio url of the video.
 
## DEMO

![](./demo.gif)  
test server:  
https://youtube-dl-audio-api.herokuapp.com/
## Requirement

* python3
* youtube-dl
* flask
* gunicorn (on heroku only)

## Usage
 
### Install
```bash
pip3 install youtube_dl flask gunicorn
```
```bash
git clone https://github.com/matumasadev02/youtube-dl-audio-api.git
cd youtube-dl-audio-api
python3 app.py
```
or Deploy to Heroku
 
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Redirect to audio url:  
```127.0.0.1:5000/?url=[url]```  
### Return json:  
```127.0.0.1:5000/get?url=[url]```  
return:
```
{
url: "https://www.example.com/hogehoge.m4a"
}
```
## Author
 
This program was made by matumasadev02.
 
* website: https://www.dev02.net/
* E-mail: matumasadev02@gmail.com
 
## License
youtube-dl-audio-api is released into the public domain.