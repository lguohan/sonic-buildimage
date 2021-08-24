.ONESHELL:
SHELL = /bin/bash
.SHELLFLAGS += -ex

MAIN_TARGET = gpio-mlxbf2.ko
MLXBF2_GPIO_SRC_RPM = gpio-mlxbf2-1.0-0.g24d2a4a.src.rpm
MODULE_DIR := $(shell pwd)/gpio-mlxbf2-$(MLXBF2_GPIO_DRIVER_VERSION)

$(addprefix $(DEST)/, $(MAIN_TARGET)): $(DEST)/% :
	rm -rf ./gpio-mlxbf2-$(MLXBF2_GPIO_DRIVER_VERSION)
	wget -O $(MLXBF2_GPIO_SRC_RPM) "https://linux.mellanox.com/public/repo/bluefield/3.7.0/extras/SRPMS/$(MLXBF2_GPIO_SRC_RPM)"
	rpm2cpio $(MLXBF2_GPIO_SRC_RPM) | cpio -idmv

	# Patch
	tar xzf gpio-mlxbf2-$(MLXBF2_GPIO_DRIVER_VERSION).tar.gz
	pushd ./gpio-mlxbf2-$(MLXBF2_GPIO_DRIVER_VERSION)

	# Build the package
	make -C /lib/modules/$(KVERSION)/build M=$(MODULE_DIR)
	popd

	mv ./gpio-mlxbf2-$(MLXBF2_GPIO_DRIVER_VERSION)/$* $(DEST)/
