#!/bin/sh
timestamp=$(date +%Y-%m-%d_%H:%M:%S) &&
dir=$1/$timestamp  &&
mkdir -p "$dir" &&
echo "Waiting 5s for letting the drive mount" && sleep 5 &&
cp $2/* $dir -r
