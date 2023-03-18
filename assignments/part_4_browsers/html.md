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
    
<HTML> 
<BODY>
<SCRIPT>
window.location = "https://www.vg.no";
</SCRIPT>    
```
</details>

### 4.4 💡 Server-sent events
Pushing cats and dogs as images over SSE.

### 4.5 🎓 CORS
How CORS work - by hand.


### 4.6 🎓 401 and 403s
Maybe do some hand-rolled security