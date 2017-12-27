.ONESHELL:
SHELL = /bin/bash
.SHELLFLAGS += -e

MFT_NAME = mft-4.8.0-26-x86_64-deb
MFT_TGZ = $(MFT_NAME).tgz
KERNELVER = 4.9.0-5-amd64
SRC_DEB = kernel-mft-dkms_4.8.0-26_all.deb

MAIN_TARGET = mft-4.8.0-26.amd64.deb
DERIVED_TARGETS = kernel-mft-dkms_4.8.0-4.9.0-5-amd64_all.deb

$(addprefix $(DEST)/, $(MAIN_TARGET)): $(DEST)/% :
	rm -rf $(MFT_NAME)
	wget -O $(MFT_TGZ) http://www.mellanox.com/downloads/MFT/$(MFT_TGZ)
	tar xzf $(MFT_TGZ)
	pushd $(MFT_NAME)/SDEBS

	# put a lock here because dpkg does not allow installing packages in parallel
	while true; do
	if mkdir $(DEST)/dpkg_lock &> /dev/null; then
	{ sudo dpkg -i $(SRC_DEB) && rm -d $(DEST)/dpkg_lock && break; } || { rm -d $(DEST)/dpkg_lock && exit 1 ; }
	fi
	done

	tar xvf `sudo dkms mkdriverdisk kernel-mft-dkms/4.8.0 -a all -d ubuntu -k $(KERNELVER) --media tar | grep "Disk image location" | cut -d':' -f2`
	popd

	# fix timestamp because we do not actually build tools, only kernel
	touch $(MFT_NAME)/DEBS/$*
	mv $(MFT_NAME)/SDEBS/ubuntu-drivers/4.9.0/$(DERIVED_TARGETS) $(MFT_NAME)/DEBS/$* $(DEST)

$(addprefix $(DEST)/, $(DERIVED_TARGETS)): $(DEST)/% : $(DEST)/$(MAIN_TARGET)
