FROM alpine:latest
ADD ./script.sh /home
ADD ./dracula.txt /home
RUN apk update && apk add bash
RUN apk add coreutils
CMD ["echo", "Ready."]
CMD ["tail -f /dev/null"]

