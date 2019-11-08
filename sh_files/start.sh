#!/bin/bash
cd /root/project/v2et
service nginx start && gunicorn --bind unix:/tmp/v2et.cn.socket v2et.wsgi:application
