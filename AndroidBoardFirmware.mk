LOCAL_PATH := $(call my-dir)

$(foreach file,$(wildcard $(LOCAL_PATH)/images/*), $(eval $(call add-radio-file,images/$(notdir $(file)))))
