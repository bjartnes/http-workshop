# Part 2 - Server basics
HTTP is built for client-server architectures and thus consists of two parts - the client and the server. Let's start with being a server, and use cURL as a client.

## 🧱 Part 2.1 Talking to cURL

<details>
    <summary> Extra material for the curious </summary>

A server will listen to connections on the server's IP adress and a designated port.
(In these exercises, we will only be able to answer one connection at a time, but in practice the server will hand off over connections so it can continue listen for new requests. Each connection is identified by its socket pair, that is the client's IP and port and the server's IP and port.)

</details>

## A simple response

As a server, start listening!
```
nc -l localhost 8080 -q 0
```
(You do not HAVE to use ```-q 0```, but it makes it more elegant to hang-up when done. This allows us to hang up by sending EOF, end-of-file, instead of killing the process. This is explained later)

Open a new terminal (try splitting the terminal, as explained earlier) and use cURL to send a HTTP request
```
curl http://localhost:8080/foo 
```

You should see something like 
```
GET /foobar HTTP/1.1
Host: localhost:10000
User-Agent: curl/7.81.0
Accept: */*
```

Answer 
```
HTTP/1.1 200 OK
Content-Type: text/plain

HEI!!!
```

The extra line, a double newline with no space in between, signifies the end of the HTTP headers and the beginning of the content. The [HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) are in the format of headername:headervalue, and the content is
whatever we say in the Content-Type header.

The client claims to accept anything (*/*) so we give it text/plain.
To end the message, for now we have to hang up the TCP connection. Use <kbd>CTRL</kdb>+<kbd>D</kdb> to send EOF (end-of-file), or if you did not use ```-q 0``` the more brutal <kbd>CTRL</kdb>+<kbd>C</kdb> will kill the process and terminate the TCP/IP connection. 

## 🧱 Part 2.2 A modern JSON API

If we want to not only accept plain text, but something slightly (only slightly) more structured, we can ask for JSON. Instead of asking for ```*/*``` we can send a header to ask for JSON, using ```-H 'Accept: application/json``` to the curl command (```-H``` sends a header and its value).

To parse the response as json, we can pipe the result into jq. Start the server again by listening to port 8080 as in the previous exercise and ask for json and pipe the result to jq.
```
curl http://localhost:8080/foo -H 'Accept: application/json' | jq
```

The result should look something like:
```
GET /foo HTTP/1.1
Host: localhost:10000
User-Agent: curl/7.81.0
Accept: application/json
```

An answer like
```
HTTP/1.1 200 OK
Content-Type: application/json

{ "fooooobar": 17 }
```

should work, as should any other valid json response. 

🗒️: As we are on both sides here, it works just as fine without the accept header and the content-type header (Try it!), but to respect the protocol we have to remember to be specific about what we ask for and we can return - we shouldn't have to guess. 

## 🧱 Part 2.3 Talking to a browser

We will expand more on browsers later, because browsers are very fun, but for the completeness of the examples here we will try to do a simple server that return text to a browser.
Listen to a port, for example 10000, by ```nc -l localhost 10000 -q 0``` and then point
a browser to http://localhost:10000

If you are working inside a GitHub Codespace, the simplest thing is to use a terminal browser. Carbonyl is already installed, and can load a we
```
carbonyl http://localhost:10000 --no-sandbox
```


Answer something along the lines ofg
```
HTTP/1.1 200 OK
Content-Type: text/plain

Hello
```
