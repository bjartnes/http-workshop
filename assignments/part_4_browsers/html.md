## Part 4 - Talking to browsers/HTML/code-on-demand
Might be some server-sent events etc in here too...
###  4.1 🧱 Rendering HTML to a browser

For example, try to start netcat, as before, and point a browser to the adress you are listening at.

<details>
    <summary>If you do not remember how...</summary>

Listen to a port, for example 10000, by ```nc -l localhost 10000 -q 0``` and then point
a browser to http://localhost:10000

If you are working inside a GitHub Codespace, the simplest thing is to use a terminal browser. Carbonyl is already installed, and can load a web browser by:
```
carbonyl http://localhost:10000 --no-sandbox
```

</details>

Answer with something like the following
```
HTTP/1.1 200 OK
Content-Type: text/html

<html>
<h1> Hello </h1>
<img src="http://placekitten.com/500/500" />
</html>
```
###  4.2 🧱 Redirecting with HTTP 
Try to talk to the browser, and then send a HTTP redirect response.
```
HTTP/1.1 302 FOUND 
Location: https://ndcoslo.com/ 
```

### 4.3 💡 Redirecting with javascript
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
    
<html> 
<body>
<script>
window.location = "https://www.vg.no";
</script>    
```
</details>

### 4.4 💡 Server-sent events
Pushing cats and dogs as images over SSE.
Server-sent events allows the server to push data to connected clients. It is a much simpler protocol than websockets, and only one-way (from the server, to the clients).

https://twitter.com/bjartnes/status/1480223053128867851
<details>
    <summary>Solution</summary>
  
```
HTTP/1.1 200 OK
Content-Type: text/html
    
<html> 
<body>
<img />
<script>
const img = document.querySelect("img");
const eventSource = new EventSource("images");
eventSource.onmessage = function(event) {
        img.src = event.data;
    }
</script>    
</html>   
```
Close the connection and listen again for the request for the eventstream
 
```
HTTP/1.1 200 OK
Content-Type: text/eventstream
    
data: http://place-puppy.com/200x200
    
data: http://place-puppy.com/202x202

data: http://place-puppy.com/202x202    
``` 
</details>  


### 4.5 🎓 CORS
How CORS work - by hand.
Open two servers, for example
```sh 
nc -l localhost 4444 -q 0
nc -l localhost 8888 -q 0
``` 

``` 
<script>
fetch('http://localhost:8888/foo').then(response => response.text()).then(data => console.log(data));
</script>
``` 
Try with and without
    
``` 
Access-Control-Allow-Origin: http://localhost:4444
``` 

### 4.6 🎓 401 and 403s
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/WWW-Authenticate#basic_authentication
    
```
HTTP/1.1 401 Unauthorized
WWW-Authenticate: Basic realm="insert realm"
```

Depending on the password being correct and if you think the user should have access (you need to base64 decode the password) you can give the user
200, 401 again or 
```
HTTP/1.1 403 Forbidden
```
