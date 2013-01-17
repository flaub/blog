#!/bin/sh

rm -rf _site
jekyll src _site
#rsync -avp _site/ ec2:/var/www
boto-rsync --endpoint s3-us-west-2.amazonaws.com _site/ s3://www.anomali.es
