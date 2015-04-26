/*
 * =====================================================================================
 *
 *       Filename:  4.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2015年04月23日 21时20分43秒
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:   (wangweihao), 578867817@qq.com
 *        Company:  xiyoulinuxgroup
 *
 * =====================================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

void func(char **p)
{
    *p = (char*)malloc(sizeof(char));
}

int main(int argc, char *argv[])
{
	char *s = NULL;
    func(&s);
    strcpy(s, "i love xiyou_linux");
    puts(s);

	return EXIT_SUCCESS;
}


