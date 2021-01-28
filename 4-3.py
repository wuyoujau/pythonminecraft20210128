from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from random import randrange

for i in range(10):
    x,y,z = mc.player.getTilePos()
    z = z+i
    for j in range(10):
        color = randrange(0,16)
        x = x+1
        mc.setBlock(x,y,z,35,color)
        
        
ans = randrange(0,16)
while True:
    hits = mc.events.pollBlockHits()
    if len(hits)>0:
        h = hits[0]
        block = mc.getBlockWithData(h.pos)
        data = block.data
        
        if data == ans:
            mc.postToChat("恭喜你找到了")
            mc.setBlock(h.pos,57)
            break
        
        elif data < ans:
            mc.postToChat("找錯了 找大一點的吧")
        elif data > ans:
            mc.postToChat("找錯了 找小一點的吧")
        
        
        
        
        
            
        
