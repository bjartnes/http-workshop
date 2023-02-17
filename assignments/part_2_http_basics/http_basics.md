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

### something something boring about line endings too
OMG
```
echo -ne 'GET / HTTP/1.1\r\nHost: info.cern.ch\r\n\r\n' | nc info.cern.ch 80
nc info.cern.ch 80 -C
````
### 2.2 🎓 Chatting over TLS 
Try talking to bjartnes.dev and request the frontpage by sending the 
```
GET / HTTP/1.1
Host: bjartnes.dev 
```
Try to follow (as in, by hand, a new request) the link...

Now, try to connect to vg the same way, but his time using 
```ncat --ssl bjartnes.dev 443```
and send the same request.
We are not going to use TLS so much in this workshop, but it is important to know about as it is used everywhere and sneaks in over TCP to make the connections secure.


## 2.3 🧱 Server
Let's be a server and talk to curl or postman or something.

## 2.4 🧱 Host headers
Let's connect with curl to the same IP with different hostnames.

## 2.5 🎓 TCP Dump

Using tcpdump to monitor what was going on in the previous challenges. (Or Wireshark, if you have it) 
```
sudo tcpdump -i lo port 8080 -v
```
or 
```
tcpdump -i lo port 8080 -v
```

<details>
    <summary>An example</summary>

https://user-images.githubusercontent.com/1174441/219039131-e325d2b2-d3c2-47c3-bffe-f1d2d468b181.mp4
</details>

