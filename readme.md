### [Silicon Valley Job Title Generator](https://t.me/svjtgbot)

It's a telegram bot serving as a PoC :)  

Served on AWS Lambda, uses Python 3.7.


Based on this [tutorial](https://hackernoon.com/serverless-telegram-bot-on-aws-lambda-851204d4236c).


### How to deploy:

Well, uh, I don't really know. I'm not that experienced with the serverless framework, so you'll have to figure it out mostly by yourself.


First of all, export some variables, cuz they're useful.  
(hint: I like to keep them in `.env` file and load them up automatically with `autoenv`).

```
export AWS_ACCESS_KEY_ID=<AWS IAM USER KEY ID>
export AWS_SECRET_ACCESS_KEY=<AWS IAM USER ACCESS KEY>
export TOKEN=<TELEGRAM BOT TOKEN FROM BOTFATHER>
```


Then just

```
serverless deploy
```

I think?


This should zip your code, push it to S3 and do all the mumbo jumbo for lambda to work correctly, like setting up API Gateway and CloudWatch and stuff. I don't even know.


But that's not all! You'll have to hook your API Gateway endpoint URL to telegram API so they can redirect all messages to that endpoint.  

Fortunately, that's simple, here, take a look at this example (I'm using `httpie`, you could do that too, or fiddle around with `curl`, I don't mind).

```
http https://api.telegram.org/bot${TOKEN}/setWebhook url=<YOUR API GATEWAY URL>
```


Then hit your telegram bot on PM and see if it works! :)
