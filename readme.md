### [Silicon Valley Job Title Generator](https://t.me/svjtgbot)

It's a telegram bot serving as a PoC :)
Served on AWS Lambda, uses Python 3.7.

Based on this [tutorial](https://hackernoon.com/serverless-telegram-bot-on-aws-lambda-851204d4236c).


### How to deploy:

Well, uhh, I don't really know. I'm not experienced with the serverless framework, so you'll have to figure it out by yourself.

The only hint I can give you is to download the deps locally with this command:
```
python3 -m pip install -r requirements.txt -t deps
```
They are ignored in git repo, but are needed for lambda to handle HTTP requests.


Other than that you should also export some variables :)
```
export AWS_ACCESS_KEY_ID=<AWS IAM USER KEY ID>
export AWS_SECRET_ACCESS_KEY=<AWS IAM USER ACCESS KEY>
export TOKEN=<TELEGRAM BOT TOKEN FROM BOTFATHER>
```


Then just
```
serverless deploy
```
i think?
