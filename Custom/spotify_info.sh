#!/usr/bin/bash
artist=$(sp metadata | grep artist | tr "|" "\n")
artist=${artist:7}
title=$(sp metadata | grep title | tr "|" "\n")
title=${title:5}
phrase="  $artist - $title  "
echo $phrase
