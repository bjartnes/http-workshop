# Part 3 - HTTP Client

## 3.1 🧱 Client  - talking to example.com
http://example.com is not using https and is quite accepting of which line-ending we send, so we will use that first to show a simple HTTP request.
```nc example.com 80```

```
GET / HTTP/1.1
Host: example.com
```

You should get a response with some HTML explaing whta example.com is for.

## 3.2 🧱 Client  - talking to example.com with only IP
The host header might seem a bit strange, we just told netcat that we wanted to talk to example.com and then the first thing we have to do is to repeat that in the HTTP respons. This makes more sense if we try to lookup the IP adress of example.com with ```nslookup example.com``` and then ```nc 93.184.216.34 80``` (or whatever IP you got back from nslookup, the IP adress can have changed since I wrote this).

Send the same HTTP request as in the previous assignment, and see that the response is the same. The reason for this is that the same IP adress could host multiple different services on HTTP. From the previous chapter, notice how cURL automatically included the host header and reflect for two seconds on the fact that netcat does not know about HTTP, wheres cURL does.

## 3.3 🧱 Some annoying tricks

### 3.3.1 🧱 TLS

Since the introduction of HTTP, we have become aware of the trouble of talking in plain text. Anyone with access to the network can see the messages we are sending, and therefore we are now using TLS to encrypt the traffic. Most servers, if you are allowed to talk on HTTP, will redirect you to a secure site. For example, try to send a HTTP GET request to http://www.vg.no. If you are lazy, you can use cURL with the verbose flag ```curl http://www.vg.no -v``` or you can send a request as in the previous step. You will see that you get a HTTP 301 Response with a location header telling you to use the secure version of the site.

If you try to use netcat to connect to the secure site (at port 443, the default port for HTTPS, ```nc www.vg.no 443```) and send HTTP traffic, you will get some error message telling you that you can not send unencrypted traffic. Instead, we can use ncat with the --ssl flag to setup a secure connection over TCP/IP and then continue as normal.

```ncat --ssl HOSTNAME PORT```

HTTP messages in all its simplicity
```
VERB PATH VERSION
Host: HOSTNAME
```
As for example, connect to bjartnes.dev at 443 and send.
```
GET / HTTP/1.1
Host: bjartnes.dev
```

### 3.3.2 🧱 Line endings
HTTP defines the headers to use CRLF (https://www.ietf.org/rfc/rfc2616.txt), that is both the \r and the \n. To make sure we send CRLF we can use the ```-C``` flag to netcat. 
For example, the classic http://info.cern.ch requires proper line endings, to try to connect and send a HTTP response with and without the -C flag. Only the -C flag should work.

Another thing to try, is to use echo to send line encodings (look up the -ne flag with ```man echo``` if you are curious.)
```
echo -ne 'GET / HTTP/1.1\r\nHost: info.cern.ch\r\n\r\n' | nc info.cern.ch 80
nc info.cern.ch 80 -C
```

### 3.3.3 🧱 Line endings and TLS
To get both line endings and TLS to work, for example to talk to https://info.cern.ch, use
```ncat --ssl info.cern.ch 443 -C```

## 3.4 Talk to website
Talk to some of your favorite websites. Try to look up their IP, connect to them and ask for their homepage.

## 3.5 🎓 TCP Dump

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