# Part 5 - Talking through proxies
This is where we introduce HTTP proxies, such as nginx. 

![Proxy](proxy.drawio.png)

![Nginx](nginx_setup.drawio.png)


## 💡5.1  talking thorugh nginx
![image](https://user-images.githubusercontent.com/88324093/220855629-50b7663c-1309-41c7-8ce8-296d19915dc6.png)

![image](https://user-images.githubusercontent.com/88324093/220857750-bf03fa6b-b16d-48b6-919b-f9ec772a48fc.png)

![image](https://user-images.githubusercontent.com/88324093/220858616-848cec75-4391-4f69-b03d-f7a157bdbb1f.png)

## 💡5.2  talking thorugh nginx with cache on
https://www.nginx.com/blog/nginx-caching-guide

Create a directory to store cache files in and make nginx's www-data user own it.
```
mkdir /var/cache/nginx
chown www-data  /var/cache/nginx
```

In the  ```etc/nginx/sites-enabled/default``` add the following line in the beginning of the file.
```
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m max_size=10g inactive=60m use_temp_path=off;
```
and 
```
proxy_cache my_cache; 
```
before the proxy pass line, to tell nginx to use the cache.

Now, if you in the response add a HTTP header for cache and to 
```
HTTP/1.1 200 OK
Content-Type: text/plain
Cache-Control: public, max-age=604800
```


## 🎓 5.3 Load testing
Let's see what the cache can do for us.
