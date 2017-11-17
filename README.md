# IP Converter

1) Script will use a formula to create an ip address into an integer.
2) Why create a single integer? 
> Maybe a line of code is more optimized as an integer that has no special characters _(i.e. ",", ".")_.
3) Given the following line of code:

``` bash
#!/bin/sh
ipaddress = 192.168.0.1
ping -c 1 192.168.0.1
```

Using the IP Converter we can convert the 'ipaddress' to 3232236033.

``` bash
#!/bin/sh
ipaddress = 3232236033
ping -c 1 192.168.0.1
```

