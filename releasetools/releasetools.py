import common
import re

def FullOTA_InstallEnd(info):
  OTA_InstallEnd(info)
  return

def IncrementalOTA_InstallEnd(info):
  OTA_InstallEnd(info)
  return

def AddImage(info, dir, basename, dest, printInfo=True):
  data = info.input_zip.read(dir + "/" + basename)
  common.ZipWriteStr(info.output_zip, basename, data)
  if printInfo:
    info.script.Print("Patching {} image unconditionally...".format(dest.split('/')[-1]))
  info.script.AppendExtra('package_extract_file("%s", "%s");' % (basename, dest))

def ImageExists(info, dir, basename):
  try:
    info.input_zip.getinfo(dir + "/" + basename)
    return True
  except KeyError:
    return False

def OTA_InstallEnd(info):
  AddImage(info, "RADIO", "tz.img", "/dev/block/platform/mtk-msdc.0/by-name/TEE1")
  AddImage(info, "RADIO", "tz.img", "/dev/block/platform/mtk-msdc.0/by-name/TEE2")
  AddImage(info, "RADIO", "lk.bin", "/dev/block/platform/mtk-msdc.0/by-name/UBOOT")
  AddImage(info, "BOOTABLE_IMAGES", "boot.img", "/dev/block/platform/mtk-msdc.0/by-name/recovery")

  return
