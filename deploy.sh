#!/bin/bash

# https://gist.github.com/nepsilon/45fae11f8d173e3370c3
ssh-add -K ~/.ssh/id_ed25519

# Copy files to the revenuehunt.com server
scp llms.txt root@143.198.165.23:/var/www/html/llms.txt
scp shopify.txt root@143.198.165.23:/var/www/html/shopify.txt
scp shopify-legacy.txt root@143.198.165.23:/var/www/html/shopify-legacy.txt
scp woocommerce.txt root@143.198.165.23:/var/www/html/woocommerce.txt