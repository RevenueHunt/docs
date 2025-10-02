#!/bin/bash

# https://gist.github.com/nepsilon/45fae11f8d173e3370c3
ssh-add -K ~/.ssh/id_ed25519

# Copy all files to the revenuehunt.com server in a single connection
scp llms.txt shopify.txt shopify-legacy.txt woocommerce.txt root@143.198.165.23:/var/www/html/