import datetime as date
from com.learn.blockChainDemo.blockDefine import Block
'''定义一个起源块'''
def create_genesis_block():
    return Block(0,date.datetime.now(),'This is a start block',"0")

'''生成后续的区块：基于已有的区块通过Hash计算生成新的值'''
def next_block(last_block):
    this_index=last_block.index+1
    this_timestamp=date.datetime.now()
    this_data="Hey!I am block!"+str(this_index)
    this_hash=last_block.hash
    return Block(this_index,this_timestamp,this_data,this_hash)



