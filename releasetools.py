#
# Copyright (C) 2019 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

import common

def FullOTA_InstallEnd(info):
  OTA_InstallEnd(info)

def IncrementalOTA_InstallEnd(info):
  OTA_InstallEnd(info)

def AddImage(info, basename, dest):
  path = "IMAGES/" + basename
  if path not in info.input_zip.namelist():
    return

  data = info.input_zip.read(path)
  common.ZipWriteStr(info.output_zip, basename, data)
  info.script.AppendExtra('package_extract_file("%s", "%s");' % (basename, dest))

def OTA_InstallEnd(info):
  info.script.Print("Patching device-tree and verity images...")
  AddImage(info, "vbmeta.img", "/dev/block/bootdevice/by-name/vbmeta")
