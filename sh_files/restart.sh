#!/bin/bash
cd /root/project/v2et
ps -ef | grep gunicorn | grep -v grep | cut -c 9-15 |xargs kill -s 9
service nginx restart && gunicorn --certfile=/etc/nginx/cert/v2et.cn.pem --keyfile=/etc/nginx/cert/v2et.cn.key  --bind unix:/tmp/v2et.cn.stocket v2et.wsgi:application
