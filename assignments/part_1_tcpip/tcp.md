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

Let that run, and open another terminal to connect to that port (the ephermal port is picked for us automatically):

```
nc localhost 8080 
```

With TCP/IP we get a nice way of sending data back and forth - but there is not structure to what we send. This is what we will explore when we dig into HTTP.

Type things, netcat sends line by line as you hit <kbd>ENTER</kbd>.
<details>
    <summary>Video explanation</summary>
  
https://user-images.githubusercontent.com/88324093/218261638-92c15a84-5366-4ed8-be71-0806ec0892f3.mp4

</details>

### 1.2 💡Hanging up properly, closing sockets
This is nice, useful to understand how HTTP sockets work and scale and get re-used etc, but not required for the workshop.
By starting netcat with the ```-q 0``` it will respect hanging up (sending EOF). We send EOF using <kbd>CTRL</kbd>+<kbd>D</kbd>.

This is also shown in the video in 1.1.

### 1.3 💡Finding the IP adress of domains using nslookup
DNS can help us find the IP adresses based on a domain name. We can use the tool ```nslookup blog.bjartnes.dev``` for example.
Try looking up the ip of
- bjartnes.dev
- blog.bjartnes.dev
- cats.bjartnes.dev
- dogs.bjartnes.dev

<details>
    <summary>Solution</summary>
<img width="421" alt="image" src="https://user-images.githubusercontent.com/1174441/219027126-8764de59-ab18-4c29-b941-1b66ff559313.png">

</details>

### 1.4 🎓 Inspecting traffic with tcpdump and/or wireshark.
Wireshark is a graphical UI which is a little easier to use, but tcpdump works on all these machines and from the terminal.
To use it, open a third terminal.

On localhost, it is easiest to use ```-i lo``` to listen to the loopback interface, when talking to other machines we can find the interface using ```ifconfig```
```
sudo tcpdump -i lo port 8080 -v
```
The codespace is running as root for simplicity (or lazyness on my part), so just skip sudo there.
```
tcpdump -i lo port 8080 -v
```
You can observe the packages, the three way handshake etc. We will come back to using it later as we talk HTTP.

