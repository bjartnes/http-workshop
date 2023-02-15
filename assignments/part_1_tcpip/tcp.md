## Part 1 - TCP/IP the foundation
We need to have a basic understanding of the layer underneath us - TCP/IP. TCP/IP is hard to build, but can be simple to use, so it is a great foundation to stand on.
It also provides some motivation for a protocol and understanding of the basic tools.

HTTP 1.1 builds on TCP/IP, so a little bit of what it provides is useful to understand.

IP provides sending packages - but they can get lost, arrive out of order etc.
TCP provides flow control, ordering, retrying etc to give the (illusion) of a stable, bi-directional communication channel.

![TCPStack](tcp.drawio.png)

Ports do not exist on the IP level, a port is an adress of sorts on the TCP layer. A TCP connection consists of two socket pairs. For example, (41.199.222.3:80, 177.41.72.6:3022). 
We typically do not see the clients port (an ephermal port, only used for the duration of the connection), but the adress we connect to is typically a well known port such as 80 or 443. 

We do not need a lot of detail on this, but it is useful to understand which abstraction layer the different concepts belong too.

### 1.1 🧱 - Basic chatting with netcat over TCP/IP
This is a must-do. Let's just talk locally over TCP/IP using netcat.
To listen on a port
```
nc -l localhost 8080
```

To connect to that port (the ephermal port is picked for us automatically)
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