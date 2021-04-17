#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc != 4) {
    	printf("what?\n");
    	
    	exit(1);
    	
    }
	printf("argc:%d\n",argc);
	printf("argv[0]:%s\n",argv[0]);
	printf("argv[1]:%s\n",argv[1]);
	printf("argv[2]:%s\n",argv[2]);
	printf("argv[3]:%s\n",argv[3]);
    unsigned int first = atoi(argv[1]);
    printf("%d",first);
    if (first != 0xcafe) {
    	printf("you are wrong, sorry.\n");
    	exit(2);
    }

    unsigned int second = atoi(argv[2]);
    if (second % 5 == 3 || second % 17 != 8) {
    	printf("ha, you won't get it!\n");
    	exit(3);
    }

    if (strcmp("h4cky0u", argv[3])) {
    	printf("so close, dude!\n");
    	exit(4);
    }

    printf("Brr wrrr grr\n");

    unsigned int hash = first * 31337 + (second % 17) * 11 + strlen(argv[3]) - 1615810207;

    printf("Get your key: ");
    printf("%x\n", hash);
    return 0;
}

