# docker
Lesson practical for containers


1. Create `Dockerfile` with the following contents in this directory:

```
FROM ubuntu:16.04

RUN apt-get update -qqq
RUN whoami

ENTRYPOINT ["/bin/echo", "hi,", "world"]
```

`FROM` tells us where to start, `RUN` give specific instructions to build the environment, and `ENTRYPOINT` dictates what happens when the computer turns on.

2. Build the container by running the following in terminal:

```
docker build -t mydockerimagename .
```

`docker` is the command, `build` is the instruction, `-t` says that you want to name your container and `mydockerimagename` is the name, and `.` is the directory to look for finding the Dockerfile (the current directory)

3. Run the container by running the following in terminal:

```
docker run -ti mydockerimagename
```

`run` is now the instruction, `-ti` tells it to be interactive and dump outputs to our terminal, and again you provided the image name.

4. Update the dockerfile to be a suitable environment for your previous p-hacking homework. This includes:
  - installing `python`
  - installing `numpy`, `pandas`, and maybe other libraries
  - adding your script (Docker has `ADD` and `COPY` functions to explore)
  - either add your data as above, or get a local copy and prepare to "mount" it, googleable with "Docker mounting volumes"
  
5. Build and run your docker container again

6. Make sure your script prints output to terminal.

