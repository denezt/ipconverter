#!/usr/bin/env python3
# PURPOSE:
# 	Simple Script to convert
# 	IP Address to Integer.
# FORMULA:
# 	(first octet * 16777216) + (second octet * 65536)
#	+ (third octet * 256) + (fourth octet)

first_octet=1
second_octet=22
third_octet=74
fourth_octet=216

def iterateIP():
    for i in range(1, 100):
        # ip_as_int = (first_octet * 16777216) + (second_octet * 65536) + (third_octet * 256) + (fourth_octet)
        print("%i.%i.%i.%i" % (i, second_octet, third_octet, fourth_octet))
        ip_as_int = (i * 16777216) + (second_octet * 65536) + (third_octet * 256) + (fourth_octet)
        print("IP As Integer: " + str(ip_as_int))

if __name__ == '__main__':
    iterateIP()
