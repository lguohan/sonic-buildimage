# Mellanox SAI

MFT = mft-4.8.0-26.amd64.deb
$(MFT)_SRC_PATH = $(PLATFORM_PATH)/mft
$(MFT)_DEPENDS += $(LINUX_HEADERS) $(LINUX_HEADERS_COMMON)
SONIC_MAKE_DEBS += $(MFT)

KERNEL_MFT = kernel-mft-dkms_4.8.0-$(KVERSION)_all.deb
$(eval $(call add_derived_package,$(MFT),$(KERNEL_MFT)))
