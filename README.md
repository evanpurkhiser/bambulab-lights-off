Turns off the Bambu Lab printers lights when they are idle.

```
docker run \
  -e PRINTER_IP=192.168.1.xxx \
  -e PRINTER_SERIAL=your-serial-here \
  -e PRINTER_ACCESS_CODE=access-code \
  evanpurkhiser/bambulab-lights-off
```
