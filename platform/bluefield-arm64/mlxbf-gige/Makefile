.ONESHELL:
SHELL = /bin/bash
.SHELLFLAGS += -ex

MAIN_TARGET = mlxbf-gige.ko
MLXBF_GIGE_SRC_RPM = mlxbf-gige-1.1-0.gfae9bf0.src.rpm
MODULE_DIR := $(shell pwd)/mlxbf-gige-$(MLXBF_GIGE_DRIVER_VERSION)

$(addprefix $(DEST)/, $(MAIN_TARGET)): $(DEST)/% :
	rm -rf ./mlxbf-gige-$(MLXBF_GIGE_DRIVER_VERSION)
	wget -O $(MLXBF_GIGE_SRC_RPM) "https://linux.mellanox.com/public/repo/bluefield/3.7.0/extras/SRPMS/$(MLXBF_GIGE_SRC_RPM)"
	rpm2cpio $(MLXBF_GIGE_SRC_RPM) | cpio -idmv

	# Patch
	tar xzf mlxbf-gige-1.1.tar.gz
	pushd ./mlxbf-gige-$(MLXBF_GIGE_DRIVER_VERSION)

	# Build the package
	make -C /lib/modules/$(KVERSION)/build M=$(MODULE_DIR)
	popd

	mv ./mlxbf-gige-$(MLXBF_GIGE_DRIVER_VERSION)/$* $(DEST)/
