freeze("$(BOARD_DIR)", "_boot.py", opt=3)
freeze("$(MPY_DIR)/drivers/dht", "dht.py")
freeze("$(MPY_DIR)/drivers/onewire")
include("$(MPY_DIR)/extmod/webrepl/manifest.py")
include("$(MPY_DIR)/drivers/neopixel/manifest.py")
