# Running 

assume you have openvpn container running. Lets say the name of the open vpn container is "ovpn-container"

```
docker run -d -e key1=password_for_user1 -e key2=password_for_user2 -e key3=password_for_user3 --name asterisk --network container:ovpn-container sergem/asterisk-docker:latest /configs/launch.sh

```