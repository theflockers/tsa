# Tomcat Sample Application Container

## Introduction

This repo contains the deliverables for the Tomcat Application Server Assignment.

## Running

Assuming that all toolset is already available, the following steps are required to build/run the container:

```
git clone https://github.com/theflockers/tsa.git
```

Change to `tsa` and `./run.sh` to build/run it.

```
$ cd tsa/
tsa $ ./run.sh
```

If your user has no writeable access to the docker socket (defaults to  `unix:///var/run/docker.sock`) you need `sudo`

```
tsa $ sudo ./run
```
