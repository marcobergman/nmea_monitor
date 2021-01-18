# nmea_monitor
Simple python tool that takes nmea sentences from standard input and lists them with their age.

Example usage:

```
pi@openplotter:~ $ nc localhost 10110|python monitor_nmea.py
```

Example output:

```
!AIVDM,1,1,,A,100001001WP>>efN8BCi60p00000,0*4b (0.1s)
$GPRMC,004309,A,5236.3680,N,00300.5212,E,6.0,260.0,190121,,,A,C*11 (0.1s)
$GPGLL,5236.3680,N,00300.5212,E,004309,A,C*43 (0.0s)
$IIMWV,000,R,06,N,A*0b (0.0s)
$IIVHW,260,T,260,M,06,N,06,K*55 (0.0s)
$IIVWR,0.00,R,6.00,N,3.09,M,11.11,K*75 (9.1s) ***** STALE *****
```
