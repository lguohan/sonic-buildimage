include $(PLATFORM_PATH)/bfscripts.mk
include $(PLATFORM_PATH)/tmfifo.mk
include $(PLATFORM_PATH)/mlxbf-gige.mk
include $(PLATFORM_PATH)/gpio-mlxbf2.mk
include $(PLATFORM_PATH)/one-image.mk

SONIC_ALL += $(SONIC_ONE_IMAGE) \
             $(DOCKER_FPM)

# Inject mlnx sai into syncd
$(SYNCD)_DEPENDS += $(MLNX_SAI)
$(SYNCD)_UNINSTALLS += $(MLNX_SAI)

ifeq ($(ENABLE_SYNCD_RPC),y)
$(SYNCD)_DEPENDS += $(LIBSAITHRIFT_DEV)
endif

# Runtime dependency on mlnx sai is set only for syncd
$(SYNCD)_RDEPENDS += $(MLNX_SAI)
