from pypresence import Presence
import time

client_id = "610284471765303306"
RPC = Presence(client_id)
RPC.connect()
RPC.update(state="https://discord.boats", details="Website", large_image="boats")
while True:
    time.sleep(15)
