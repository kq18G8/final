import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlock(pos.x+3, pos.y, pos.z, block.STONE.id)
mc.setBlock(pos.x+4, pos.y, pos.z, block.STONE.id)
mc.setBlock(pos.x+5, pos.y, pos.z, block.STONE.id)
mc.setBlock(pos.x+6, pos.y, pos.z, block.STONE.id)
mc.setBlock(pos.x+7, pos.y, pos.z, block.STONE.id)
mc.setBlock(pos.x+8, pos.y, pos.z, block.STONE.id)
mc.setBlock(pos.x+9, pos.y, pos.z, block.STONE.id)
mc.setBlock(pos.x+10, pos.y, pos.z, block.STONE.id)
mc.setBlock(pos.x+11, pos.y, pos.z, block.STONE.id)
mc.setBlock(pos.x+12, pos.y, pos.z, block.STONE.id)

