#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

blob_fixups: blob_fixups_user_type = {
    'vendor/lib/hw/camera.sdm660.so': blob_fixup()
        .binary_regex_replace(b'\xc1\x68\xd0\xe9\x0d\x20\xcd\xe9\x03\x20', b'\xc1\x68\xd0\xe9\x12\x20\xcd\xe9\x03\x20')
        .binary_regex_replace(b'\xdb\xf8\x00\x10\x08\x9a\x49\x6b\xc6\xe9\x04\x21', b'\xdb\xf8\x00\x10\x08\x9a\x89\x6c\xc6\xe9\x04\x21'),
    'vendor/lib/lib_lowlight.so': blob_fixup()
        .replace_needed('libstdc++.so', 'libstdc++_vendor.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'lavender',
    'xiaomi',
    blob_fixups=blob_fixups,
    check_elf=False,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(module, 'sdm660-common', module.vendor)
    utils.run()
