# http-workshop
## Intro/abstract

My NDC 2023 workshop https://ndcoslo.com/agenda/part-12-artisanal-http-or-http-by-hand-0jfs/0xeiawe0qsu

> In this workshop, we will dig into HTTP 1.1 - the Hypertext Transfer Protocol - from the ground up. We will iterate on the problem of communication between computers, 
> starting by typing text in a terminal on one computer and sending it over TCP/IP to another computer. We will gradually build on this, and before you know it, we are 
> talking to HTTP-savvy programs like browsers. Along the way, we’ll introduce tools such as netcat, curl, jq, wireshark, nginx and k6. Our goal is that you should 
> understand the capabilities of HTTP better, be able to design solutions that use the capabilities of HTTP to its potential - and have new tools and tricks you can use 
> when troubleshooting. The format will be highly interactive, so bring a laptop with a Linux terminal of some sort (For example WSL2 with Ubuntu on Windows, a Mac or a 
> real Linux box). If you would like to do the workshop in a pair, bring a friend - or let us know and we can hook you up with someone. For those that prefer to work 
> alone, it is perfectly fine to talk to your own browser on your own laptop, too.

## Running the workshop/tools
There are a varieties of tools we can use for this workshop, some tools will be considers "must-haves", some are fun to try and optional.
They can be run either in GitHub codespace, as dev containers locally on your laptop or by installing the tools on your linux machine, if you have a Mac it might work, on Windows the only reasonable option is to use WSL2 or a devcontainer. All these options will be decsribed in detail.

### WSL2 / Linux (and likely Mac)
Install WSL2, I typically use Ubuntu from the Microsoft store https://apps.microsoft.com/store/detail/ubuntu/9PDXGNCFSCZV 
To make sure you have updated package repositories run
#### WSL notes to be added to devcontainer
apt-get update
apt-get install netcat net-tools dnsutils
```
sudo apt-get update
```
#### netcat
nc should be installed in Ubuntu, but can typically be installed as (todo: check..) netcat net-tools... or something.

#### jq
Useful for parsing JSON.
```
sudo apt-get install jq
```
#### nettools
```
sudo apt-get install net-tools
```
tcpdump....

### GitHub Codespace
Setup...

### Devcontainer locally on your machine
Setup...

# Assignments
The order is the intended workshop order, but feel free to skip to whatever you find most interesting. 
I use some emojies to indicate if things can be skipped or not.
- 🧱 is considered a foundation of sort, and should not be skipped. These will be tutorial-ish.
- 💡 These are good to get better insights, likely include some more thinking/playing around on your own. Can be skipped.
- 🎓 For extra points and deep-dive, feel free to skip, likely includes more work and things to figure out on your own.


## Part 1 - TCP/IP the foundation
We need to have a basic understanding of the layer underneath us - TCP/IP. TCP/IP is hard to build, but can be simple to use, so it is a great foundation to stand on.
It also provides some motivation for a protocol and understanding of the basic tools.

### 1.1 🧱 - Basic chatting with netcat over TCP/IP
This is a must-do. Let's just talk locally over TCP/IP using netcat.
To listen on a port
```
nc -l localhost 8080
```

To connect to that port
```
nc localhost 8080 
```

<details>
    <summary>Video explanation</summary>
  
https://user-images.githubusercontent.com/88324093/218261638-92c15a84-5366-4ed8-be71-0806ec0892f3.mp4

</details>

### 1.2 💡Hanging up properly, closing sockets
This is nice, useful to understand how HTTP sockets work and scale and get re-used etc, but not required for the workshop.

### 1.3 💡Finding the IP adress of domains using nslookup

### 1.4 🎓 Inspecting traffic with tcpdump and/or wireshark.

### 1.5 🎓 Chatting to a machine in the cloud
Setting up netcat on a publicly accessible virtual machine. Allow you to talk to multiple users.

### 1.6 🎓 Using my HTTP chatbot
Highly experimental software.... 
https://github.com/bjartwolf/http_chatbot

## Part 2 - HTTP basics
### 2.1 🧱 Client  - talking to some internetservices
Let's call some web services on the internet and talk to them.


### 2.2 🧱 Server
Let's be a server and talk to curl or postman or something.

### 2.3 🧱 Host headers
Let's connect with curl to the same IP with different hostnames.

## Part 3 - Playing with responses

### 3.1 🧱 Redirects
Might be some server-sent events etc in here too...

### 3.2 🧱 Sending json to a curl client
Let's build modern web API to send JSON to a curl client3

### 3.3 💡 Parsing JSON with jq
Sort of the same, but let's learn a little bit of jq, because this is a cute and useful tool. 


## Part 5 - Talking to browsers/HTML/code-on-demand
Might be some server-sent events etc in here too...
###  5.1 🧱 Rendering HTML to a browser

### 5.2 💡 Redirecting with javascript
Instead of redirecting with 302s like earlier, try to redirect with javascript 

<details>
    <summary>Hint</summary>
We can send HTML with a SCRIPT tag, and then use the window.location to send the browser somewhere else.
```
window.location = URL
```
</details>

<details>
    <summary>Solution</summary>
  
```
HTTP/1.1 200 OK
Content-Type: text/html
    
<HTML> 
<BODY>
<SCRIPT>
window.location = "https://www.vg.no";
</SCRIPT>    
```
</details>

### 5.3 💡 Server-sent events
Pushing cats and dogs as images over SSE.

### 5.4 🎓 CORS
How CORS work - by hand.


### 5.5 🎓 401 and 403s
Maybe do some hand-rolled security
## Part 6 - Talking through proxies
This is where we introduce HTTP proxies, such as nginx.
### 💡6.1  talking thorugh nginx


## Part 7 - Maybe some Azure stuff and other REAL life stuff...
Why not try to run this in a virtual machine behind a public IP?

### 7.1 🎓 PKCE to Azure B2C by hand
This is a useful exercise to understand how to work with real, distributed hypermedia applications by hand... We start a browser with a redirect link where we listen to the redirect using netcat.
https://blog.bjartnes.dev/posts/auth-flow-pkce/

# Background material

A lot of the examples are shown in videos on Twitter and summarized in my https://blog.bjartnes.dev/posts/http-love, and more will come there two. I might find other formats, YouTube etc, to distribute the videos to make it easy to link it to specific assignments/explanations.
