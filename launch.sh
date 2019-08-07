#!/bin/sh
echo "{\"apiURL\": \"http://$API_URL:$API_PORT\"}" > /usr/share/nginx/html/config.json
nginx -g 'daemon off;'