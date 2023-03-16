# http-workshop
## Intro/abstract

My NDC 2023 workshop https://ndcoslo.com/agenda/part-12-artisanal-http-or-http-by-hand-0jfs/0xeiawe0qsu

> In this workshop, we will dig into HTTP 1.1 - the Hypertext Transfer Protocol - from the ground up. We will iterate on the problem of communication between computers, 
> starting by typing text in a terminal on one computer and sending it over TCP/IP to another computer. We will gradually build on this, and before you know it, we are 
> talking to HTTP-savvy programs like browsers. Along the way, we’ll introduce tools such as netcat, curl, jq, wireshark, nginx and k6. Our goal is that you should 
> understand the capabilities of HTTP better, be able to design solutions that use the capabilities of HTTP to its potential - and have new tools and tricks you can use 
> when troubleshooting. The format will be highly interactive, so bring a laptop with a Linux terminal of some sort (For example WSL2 with Ubuntu on Windows, a Mac or a 
> real Linux box). If you would like to do the workshop in a pair, bring a friend - or let us know and we can hook you up with someone. For those that prefer to work 
> alone, it is perfectly fine to talk to your own browser on your own laptop, too.

## Running the workshop/tools
There are a varieties of tools we can use for this workshop, some tools will be considers "must-haves", some are fun to try and optional.
They can be run either in GitHub codespace, as dev containers locally on your laptop or by installing the tools on your linux machine, if you have a Mac it might work, on Windows the only reasonable option is to use WSL2 or a devcontainer. All these options will be decsribed in detail.

Wireshark can also be fun to install to monitor traffic, but it is not required.

1. ⛈️ Cloud-based: Setup on codespace (Easy/cloudbased)
This is the simplest way, everything runs in the browser, but it requires a GitHub Teams account or similar that
have codespaces available.
See documentation [here](setup_descriptions/setup_codespace.md)

2. 🐋 Devcontainer on local machine: This works on Mac/Linux/Windows. It does require docker and VS Code to be installed, but installs all the tools required automatically once that is setup. Docker Desktop should be possible to run as a personal user under the education and open-source clause, as this is an open-source project for education https://www.docker.com/pricing/. 
See documentation [here](setup_descriptions/setup_devcontainer.md)

3. 🪟 Windows: Setup on WSL2
On Windows, running Linux is easy to do using WSL2.
See documentation [here](setup_descriptions/setup_wsl.md)

4. 🍎/🐧:Mac or Linux: Local setup
This requires a mac or linux installation, as these tools really does not work properly on Windows.
Descriptions are for Ubuntu, so you might have to figure out how to do it on your distro...
See documentation [here](setup_descriptions/setup_linuxmac.md)


# Assignments
The order is the intended workshop order, but feel free to skip to whatever you find most interesting. 
I use some emojies to indicate if things can be skipped or not.
- 🧱 is considered a foundation of sort, and should not be skipped. These will be tutorial-ish.
- 💡 These are good to get better insights, likely include some more thinking/playing around on your own. Can be skipped.
- 🎓 For extra points and deep-dive, feel free to skip, likely includes more work and things to figure out on your own.

- [Part 1 TCP/IP Basics](assignments/part_1_tcpip/tcp.md)
- [Part 2 HTTP Basics](assignments/part_2_being_a_server/http_server_basics.md)
- [Part 3 Responses](assignments/part_3_being_a_client/http_basics.md)
- [Part 4 Browsers](assignments/part_4_browsers/html.md)
- [Part 5 Proxies](assignments/part_5_proxies/proxies.md)
- [Part 6 Hypermedia](assignments/part_6_hypermedia/hypermedia.md)


# Background material

A lot of the examples are shown in videos on Twitter and summarized in my https://blog.bjartnes.dev/posts/http-love, and more will come there two. I might find other formats, YouTube etc, to distribute the videos to make it easy to link it to specific assignments/explanations.

How I set up my terminal in WSL2 https://blog.bjartnes.dev/posts/how-i-set-up-powershell-to-look-good/
(I will likely do the same blogpost for Ubuntu, to show how to make it look good in Windows.)
