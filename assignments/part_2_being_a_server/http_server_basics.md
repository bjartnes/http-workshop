
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
Another little trick is to set the terminal prompt to server on one terminal and client on the other, too try to separate them. I like to keep clients on the left and the server on the right as well. Just type ```PS1="Server >"``` and ```PS1="Client >"``` in
the terminal. 

```
curl http://localhost:8080/foo 
```

You should see something like 

<sub>HTTP Request</sub>
```
GET /foobar HTTP/1.1
Host: localhost:10000
User-Agent: curl/7.81.0
Accept: */*
```

Type the following HTTP Response in the window where you are running nc to answer the client. 

<sub>HTTP Response</sub>
```
HTTP/1.1 200 OK
Content-Type: text/plain

HEI!!!
```

The extra line, a double newline with no space in between, signifies the end of the HTTP headers and the beginning of the content. The [HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers) are in the format of headername:headervalue, and the content is
whatever we say in the Content-Type header.

The client claims to accept anything ```(*/*)``` so we give it ```text/plain```.
To end the message, for now we have to hang up the TCP connection. Use <kbd>Ctrl</kbd> + <kbd>D</kbd> to send EOF (end-of-file).  If you did not use ```-q 0``` the more brutal <kbd>Ctrl</kbd>+<kbd>C</kbd> will kill the process and terminate the TCP/IP connection.
📝 THe correct way to signifiy the end of the message to the client is to provide the length of the content you are sending in the HTTP header as ```Content-Length```. We will come back to that, but this is quicker than counting characters and it works in many cases so we will use this
from time to time.

It will look something like this
![Image that explains where to type what](https://user-images.githubusercontent.com/88324093/226139174-37b35ae3-12bc-4a33-9e2d-c0eda8404d3e.png)

## 🧱 Part 2.2 A modern JSON API

If we want to not only accept plain text, but something slightly (only slightly) more structured, we can ask for JSON. Instead of asking for ```*/*``` we can send a header to ask for JSON, using ```-H 'Accept: application/json``` to the curl command (```-H``` sends a header and its value).

To parse the response as json, we can pipe the result into jq. Start the server again by listening to port 8080 as in the previous exercise and ask for json and pipe the result to jq.
```
curl http://localhost:8080/foo -H 'Accept: application/json' | jq
```

The result should look something like:

<sub>HTTP Request</sub>
```
GET /foo HTTP/1.1
Host: localhost:10000
User-Agent: curl/7.81.0
Accept: application/json
```

An answer like
<sub>HTTP Response </sub>
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
If you are working locally on your own machine from the terminal


Answer something along the lines ofg
```
HTTP/1.1 200 OK
Content-Type: text/plain

Hello
```

## 🧱 Part 2.4 Posting data
To post data you can use curl and send a file. We should tell the server what the content we are sending is. 

```
curl -X POST -H "Content-Type: application/json" -d @example.json http://localhost:10000/foobar
```
 
You can answer anything that is valid HTTP, but the following should be sufficient. We don't have to send any content back.
```
HTTP/1.1 201 CREATED 
```

Notice how the sending and recieving the JSON file is not very different from anything else we have been doing. 

## 🧱 Part 2.5 Talking to python 

Start netcat on some port, for example
```
nc -l localhost 6666 -q 0
```

Start python with ```python3```.
Load the requests library and do a HTTP request to the port where you listen with netcat.
```
import requests
import requests
response = requests.get("http://localhost:6666/fooobar")
```
...and answer with some reply and hang up using <kbd>CTRL</kbd>+<kbd>D</kbd>.

Then print the response object from Python
```
response.status_code
response.text
```

![Python example](https://user-images.githubusercontent.com/88324093/226142823-81a81d89-ec9e-47aa-8799-38d5e5c4abef.png)