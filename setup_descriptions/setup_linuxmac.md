# Linux/mac
Install WSL2, I typically use Ubuntu from the Microsoft store https://apps.microsoft.com/store/detail/ubuntu/9PDXGNCFSCZV 

## Installing tools
To install requirements, install something like this.... 
Depending on your installation, this is for Ubuntu...
Tools used are
- curl
- jq
- nginx
- k6
- netcat (nc)
- nslookup (net-tools)
- tcpdump
- ncat (optionally, for ssl) 

```
sudo apt-get update
sudo apt-get -y install netcat net-tools dnsutils nginx gnupg2 tcpdump jq ncat
```

## Installing k6 (optional)

```
gpg -k
gpg --no-default-keyring --keyring /usr/share/keyrings/k6-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D69
echo "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main" | sudo tee /etc/apt/sources.list.d/k6.list
sudo apt-get update \
    && apt-get -y install --no-install-recommends k6
```
