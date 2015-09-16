login.cgi:login.c
	gcc -o login.cgi login.c
clean:
	rm -f login.cgi loggedin.csv
