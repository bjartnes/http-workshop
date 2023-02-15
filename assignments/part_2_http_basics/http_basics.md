# Part 2 - HTTP basics
## 2.1 🧱 Client  - talking to some internetservices
Let's call some web services on the internet and talk to them.
From part 1 we learned some useful tricks to talk HTTPS using ncat.
```ncat --ssl HOSTNAME PORT```

HTTP messages in all its simplicity
```
VERB PATH VERSION
Host: HOSTNAME
```
As for example 
```
GET / HTTP/1.1
Host: bjartnes.dev
```


## 2.2 🧱 Server
Let's be a server and talk to curl or postman or something.

## 2.3 🧱 Host headers
Let's connect with curl to the same IP with different hostnames.
