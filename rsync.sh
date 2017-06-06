#!/bin/sh

rsync -auvz --exclude=.git --exclude=*.deb --exclude=migrations . /export/crawlspace/eab
