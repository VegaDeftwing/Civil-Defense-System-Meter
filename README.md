# Civil Defense System Meter
Display CPU and RAM usage on a modded CD Radiation Meter

be sure to open the port of the arduino using

~~~
stty -F /dev/ttyUSB0 cs8 9600 ignbrk -brkint -icrnl -imaxbel -opost -onlcr -isig -icanon -iexten -echo -echoe -echok -echoctl -echoke noflsh -ixon -crtscts
~~~

in your startup file of choice (works well in i3 .conf file)
