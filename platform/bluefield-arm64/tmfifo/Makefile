.ONESHELL:
SHELL = /bin/bash
.SHELLFLAGS += -ex

MAIN_TARGET = mlxbf-tmfifo.ko
TMFIFO_SRC_RPM = tmfifo-1.5-0.g04d20d3.src.rpm
MODULE_DIR := $(shell pwd)/tmfifo-$(TMFIFO_DRIVER_VERSION)

$(addprefix $(DEST)/, $(MAIN_TARGET)): $(DEST)/% :
	rm -rf ./tmfifo-$(TMFIFO_DRIVER_VERSION)
	wget -O $(TMFIFO_SRC_RPM) "https://linux.mellanox.com/public/repo/bluefield/3.7.0/extras/SRPMS/$(TMFIFO_SRC_RPM)"
	rpm2cpio $(TMFIFO_SRC_RPM) | cpio -idmv

	# Patch
	tar xzf tmfifo-1.5.tar.gz
	pushd ./tmfifo-$(TMFIFO_DRIVER_VERSION)

	# Build the package
	make -C /lib/modules/$(KVERSION)/build M=$(MODULE_DIR)
	popd

	mv ./tmfifo-$(TMFIFO_DRIVER_VERSION)/$* $(DEST)/
