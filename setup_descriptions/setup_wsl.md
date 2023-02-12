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
