/*
 * =====================================================================================
 *
 *       Filename:  1.c
 *
 *    Description:  a
 *
 *        Version:  1.0
 *        Created:  2015年04月23日 20时17分28秒
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

void fun(void)
{
    unsigned int a = 6;
    int b = -20;
    printf("%u\n", a+b);
    (a+b > 6) ? puts(">6"):puts("<6");
}



int main(int argc, char *argv[])
{
	fun();

	return EXIT_SUCCESS;
}


