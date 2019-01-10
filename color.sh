#!/bin/bash

for f in ./cropped/*.jpg; do th colorize.lua $f ./outputs/$f; done

