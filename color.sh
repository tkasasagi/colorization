#!/bin/bash

for f in *.jpg; do th colorize.lua $f ./outputs/$f; done

