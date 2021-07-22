#!/usr/bin/python3
import sys
import os
import subprocess


if __name__ == "__main__":
    # names = {}
    # for name in sys.stdin.readlines():
    #     name = name.strip()
    #     if name in names:
    #         names[name] += 1
    #     else:
    #         names[name] = 1

    # for name, count in names.items():
    #     sys.stdout.write("%d\t%s\n"%(count, name))
    # os.system("ls -l *")
    # output = os.popen('ls -l *')
    # print(output.read())
    for i in range(10):
        print(i)

        

    if len(sys.argv) > 2:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    else:
        print("this command takes two arguments and adds them\nless than two arguments given.")
        sys.exit(1)
    print("%s" % str(num1+num2))
