from com.learn.blockChainDemo.sourceBlock import create_genesis_block, next_block

#首先生成一个起源块
blockChain=[create_genesis_block()]
previous_block=blockChain[0]

print(previous_block)

#添加到区块中的块数目
num_of_block=20

#把块加入到区块链中去
for i in range(0,num_of_block):
    block_to_add=next_block(previous_block)
    blockChain.append(block_to_add)
    previous_block=block_to_add

    #告诉区块上的所有节点，新加入的区块信息
    print("宝哥通知：第 {} 个区块已经被加入到区块链中了!".format(block_to_add.index))
    print("相应的Hash值是: {}\n".format(block_to_add.hash))


