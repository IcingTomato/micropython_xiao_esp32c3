Compile MicroPython for Seeed XIAO-ESP32C3
=======================

## Getting the Repositories

```shell
git clone --recursive https://github.com/espressif/esp-idf.git

cd esp-idf; git checkout release/v4.4; git submodule init; git submodule update --init --recursive;

./install.sh

cd ..

git clone --recurse-submodules https://github.com/IcingTomato/micropython_xiao_esp32c3.git
```

##  Building the Firmware

```shell
cd micropython_xiao_esp32c3/mpy-cross

make

cd ../ports/esp32

export ESPPORT=/dev/ttyACM0 (or /dev/ttycu.SLAB_USBtoUART macOS or COMxx on MinGW)

export IDF_PATH=/path/to/esp-idf

. $IDF_PATH/export.sh

make clean

make submodules

make BOARD=XIAOESP32_C3

python esptool.py -p /dev/ttyACM0 -b 460800 --before default_reset --after hard_reset --chip esp32c3 --no-stub write_flash --flash_mode dio --flash_size detect --flash_freq 80m 0x0 build-XIAOESP32_C3/bootloader/bootloader.bin 0x8000 build-XIAOESP32_C3/partition_table/partition-table.bin 0x10000 build-XIAOESP32_C3/micropython.bin
```
