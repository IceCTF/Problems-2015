#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netdb.h>
#define MAXLINE 4096

int my_connect(char *server, unsigned int port, int *sockfd);
int my_send(int sockfd, char *out, int debug);
int my_read(int sockfd, char *recvline, int debug);

int main(int argc, char **argv) {
    int sockfd, n, debug;
    char recvline[MAXLINE+1], out[MAXLINE+1];
    char *cmd, *pos;
    char server[] = "176.31.102.84";
    debug = 1;

    if (!my_connect(server, 6667, &sockfd)) {
        printf("Failed to connect to %s.\n", server);
        exit(1);
    }

    while(1) {
        recvline[0] = 0;
        n = my_read(sockfd, recvline, debug);

        if (n > 0) {
            recvline[n] = 0;

            // Parse username and message
            if(strstr(recvline, "PRIVMSG MrRobot :start") != NULL)
            {
                my_send(sockfd, "NICK MrRobot\r\n", debug);
                my_send(sockfd, "USER MrRobot 8 * : Christian Slater\r\n", debug);
                my_send(sockfd, "JOIN #ctf\r\n", debug);

                my_send(sockfd, "PRIVMSG #ctf :Fuck her right in the pussy\r\n", debug);
            }

            if (strstr(recvline, "PING") != NULL) {
                out[0] = 0;
                pos = strstr(recvline, " ")+1;
                sprintf(out, "PONG %s\r\n", pos);
                my_send(sockfd, out, debug);
            }
        }
    }
    exit(0);
}

int my_connect(char *server, unsigned int port, int *sockfd) {
    struct sockaddr_in servaddr;
    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(port);

    if ( (*sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        return 0;
    }

    if (inet_pton(AF_INET, server, &servaddr.sin_addr) <= 0) {
        return 0;
    }
    if (connect(*sockfd, (struct sockaddr*)&servaddr, sizeof(servaddr)) < 0 ) {
        return 0;
    }

    return 1;
}

int my_send(int sockfd, char *out, int debug) {
    if (debug) {
        printf("OUT: %s", out);
    }
    return send(sockfd, out, strlen(out), 0);
}

int my_read(int sockfd, char *recvline, int debug) {
    int n;
    n = read(sockfd, recvline, MAXLINE);
    if (n > 0 && debug) {
        printf("IN: %s", recvline);
    }
    return n;
}
