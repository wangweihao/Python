/*
 * =====================================================================================
 *
 *       Filename:  3.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  2015年04月23日 20时41分46秒
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

int main(int argc, char *argv[])
{
	FILE *fp = fopen("a.txt", "r");
    char buffer[4096];
    fgets(buffer, sizeof(buffer), fp);
    fprintf(fp, "%s", buffer);

	return EXIT_SUCCESS;
}


