# __0x13-firewall__

## __0-block_all_incoming_traffic_but__

Contains commands to install and configure ufw to only allow incoming traffic on:

- `22` (SSH)
- `443` (HTTPS SSL)
- `80` (HTTP)

## __100-port_forwarding__

ufw configuration file (`/etc/ufw/before.rules`) to redirect all incoming traffic on port `8080` to port `80`.
