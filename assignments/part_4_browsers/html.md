## Part 4 - Talking to browsers/HTML/code-on-demand
Might be some server-sent events etc in here too...
###  4.1 🧱 Rendering HTML to a browser

### 4.2 💡 Redirecting with javascript
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

### 4.3 💡 Server-sent events
Pushing cats and dogs as images over SSE.

### 4.4 🎓 CORS
How CORS work - by hand.


### 4.5 🎓 401 and 403s
Maybe do some hand-rolled security