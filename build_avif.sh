#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install -y cmake nasm cargo ninja-build python3-pip
python -m pip install --upgrade pip
python -m pip install setuptools
python -m pip install meson

cd /tmp
rm -rf /tmp/libavif

git clone https://github.com/AOMediaCodec/libavif.git
cd libavif/ext
#export MAKEFLAGS=-j$(nproc)
MAKEFLAGS=-j4
bash aom.cmd
bash libjpeg.cmd
bash libyuv.cmd

cd ..
mkdir build
cd build

cmake -G Ninja -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF -DAVIF_CODEC_AOM=ON -DAVIF_LOCAL_AOM=ON -DAVIF_CODEC_DAV1D=OFF -DAVIF_LOCAL_DAV1D=OFF -DAVIF_CODEC_RAV1E=OFF -DAVIF_LOCAL_RAV1E=OFF -DAVIF_CODEC_LIBGAV1=OFF -DAVIF_LOCAL_LIBGAV1=OFF -DAVIF_CODEC_SVT=OFF -DAVIF_LOCAL_SVT=OFF -DAVIF_LOCAL_LIBYUV=ON -DAVIF_BUILD_EXAMPLES=OFF -DAVIF_BUILD_APPS=ON -DAVIF_BUILD_TESTS=OFF ..
ninja

cp /tmp/libavif/build/avifenc /usr/bin/
rm -rf /tmp/cavif

