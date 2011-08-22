#!/bin/sh

rm -rf _site
jekyll src _site
rsync -avp _site/ storage:/c/Web/blog
