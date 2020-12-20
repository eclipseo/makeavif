#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install -y libaom-dev golang gcc-8 g++-8
pushd
cd /tmp
rm -rf /tmp/cavif
go get github.com/Kagami/go-avif

git clone --recurse-submodules --recursive https://github.com/link-u/cavif.git

cd cavif
mkdir build && cd build
CXX=g++-8 CC=gcc-8 cmake ..
make -j4 cavif
make install
rm -rf /tmp/cavif
popd
