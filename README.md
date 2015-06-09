# hackla-2015

server IP is 54.173.149.200

Runs on django 1.6.2 and python 3.

Install pip and run ```pip install -r requirements```

Download the following repositories

<pre>
https://github.com/ContextIO/Python-ContextIO
https://github.com/marcgibbons/django-rest-swagger
</pre>

libraries needed
<pre>
sudo apt-get install python3 python-pip
pip install django
pip install djangorestframework
pip install markdown
pip install django-filter
</pre>


## Old
site lives at ```http://hackla2015.mybluemix.net```

deply cmd ```cf push hackla2015 -m 128M -b https://github.com/ephoning/heroku-buildpack-python.git``` 
