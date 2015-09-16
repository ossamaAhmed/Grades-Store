#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char input[256];
char *token;
char *tok;
char buffer[256];


char* getPW(char *username)
{
	char *membercheck=(char *)malloc(256);
	char *tu=(char *)malloc(256);
	char *tp=(char *)malloc(256);
	char *tpp=(char *)malloc(256);
	FILE *members = fopen("./members.csv","rt");
	while(!feof(members))
	{
		fgets(membercheck,255,members);
		if(!feof(members))
		{
			tu = strtok(membercheck, ",");
			tu = strtok(NULL, ",");
			//printf("<p>the username is: %s </p>", tu);
			if (strcmp(username,tu)==0)
			{
				//tp = strtok(NULL, ",");
				tp = strtok(NULL, "\n");
				//printf("<p>the password is: %s",tp);
				//return strtok(NULL, "\n");
				return tp;
				//break;
			}
		}
	}
	fclose(members);
	return NULL;
}

int check(char *username, char *password)
{
	FILE *members= fopen("./members.csv", "rt");
	char *temp = (char *)malloc(256);
	temp=getPW(username);
	if(temp==NULL)
	{
		return 1;
	}
	else
	{
		return strcmp(temp,password);
	}
}

void success(char *username)
{
	char *tp=(char *)malloc(256);
	int flag=1;
	tp = strcpy(tp,username);
	tp = strcat(tp, "\n");
	char *read=(char *)malloc(256);
	FILE *loggedin=fopen("./loggedin.csv","a+rt");
	while(!feof(loggedin))
	{
		fgets(read,255,loggedin);
		if(strcmp(tp,read)==0)
		{
			flag=0;
		}
	}
	if(flag)
	{
		fprintf(loggedin,"%s\n",username);
	}
	fclose(loggedin);
	char *line=(char *)malloc(2048);
	FILE *catalogue=fopen("./catalogue.html","r+wt");
	while(!feof(catalogue))
	{
		fgets(line,2047,catalogue);
		if(strcmp(line,"<html>\n")==0)
		{
			printf("%s<head><title>Welcome %s</title></head>",line,username);
		}

		else if(strcmp(line,"<input type=\"hidden\" name=\"username\" value=\"default\">\n")==0)
		{
			printf("<input type=\"hidden\" name=\"username\" value=\"%s\">\n", username);
		}
		else
		{
			printf("%s",line);
		}
	}
	fclose(catalogue);
}

void failure()
{
	printf("<meta http-equiv=\"refresh\" content=\"0; url=./error.html\"/>");
}

int main(void)
{
	char* username;
	char* password;
	username=(char *)malloc(256);
	password=(char *)malloc(256);
	//FILE *f= fopen("./login.html", "rt");
	//int ch;
    	printf("Content-Type: text/html\n\n");
	printf("<html>");
    	//if(f==NULL)
	//{
 	//   printf("<head><title>ERROR</title></head>");
       	//   printf("<body><p>Unable to open file!</p></body>");	
	//}
	//else
    	//{
	//	while ((ch=fgetc(f))!=EOF)
	//    {
	//    	putchar(ch);
	//    }
	fgets(input,255,stdin);
	strncpy(buffer,input,255);
	username=strtok(buffer,"=");
	username=strtok(NULL,"&");
	password=strtok(NULL, "=");
	password=strtok(NULL, "\n");
	getPW(username);
	//printf("%s\n",password);
	//printf("%s\n", username);
	int loggedin=check(username,password);
	//printf("%d\n",loggedin);
	//printf("<p>getPW: %s</p>", getPW);
	if(loggedin==0)
	{
		success(username);
	}
	else
	{
		failure();
	}
	//}
	//fclose(f);
}
