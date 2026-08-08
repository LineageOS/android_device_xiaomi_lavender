#!/bin/bash
#
# Copyright (C) 2016 The CyanogenMod Project
# Copyright (C) 2017-2020 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

function blob_fixup() {
    case "${1}" in
        vendor/lib/hw/camera.sdm660.so)
            perl -pi -e 's/\xc1\x68\xd0\xe9\x0d\x20\xcd\xe9\x03\x20/\xc1\x68\xd0\xe9\x12\x20\xcd\xe9\x03\x20/g' "${2}"
            perl -pi -e 's/\xdb\xf8\x00\x10\x08\x9a\x49\x6b\xc6\xe9\x04\x21/\xdb\xf8\x00\x10\x08\x9a\x89\x6c\xc6\xe9\x04\x21/g' "${2}"
            ;;
    esac
}

# If we're being sourced by the common script that we called,
# stop right here. No need to go down the rabbit hole.
if [ "${BASH_SOURCE[0]}" != "${0}" ]; then
    return
fi

set -e

export DEVICE=lavender
export DEVICE_COMMON=sdm660-common
export VENDOR=xiaomi

"./../../${VENDOR}/${DEVICE_COMMON}/extract-files.sh" "$@"
