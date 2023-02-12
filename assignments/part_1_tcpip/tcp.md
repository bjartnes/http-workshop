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