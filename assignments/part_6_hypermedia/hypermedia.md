## Part 6 - Maybe some Azure stuff and other REAL life stuff...
Why not try to run this in a virtual machine behind a public IP?

### 6.1 🎓 PKCE to Azure B2C by hand
This is a useful exercise to understand how to work with real, distributed hypermedia applications by hand... Parts of the conversation here is going to be way to complex to do without a browser, there will be too much code and demand and other tricks. Still - the input and the output of the entire conversation can be done by hand, and this was a truly eye-opening experience for me to go through. So, while a bit tedious, it is really worth it to tie all pieces together. We start a browser with a redirect link where we listen to the redirect using netcat.
https://blog.bjartnes.dev/posts/auth-flow-pkce/