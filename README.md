# 如何接入焦耳区块链，并部署节点
## step-1
请准备一台Linux Ubuntu 14.04（或者更高）的服务器，并且下载焦耳客户端
下载地址 http://static-mars.gouchacha.com/downloads/joulecoind

## step-2
下载完成后，cd 到 joulecoind 二进制文件所在目录，并且启动运行 ./joulecoind 
这时会抛出一个警告，提示我们设置RPC账号和密码。
只需要 
```angular2html
vi ~/.joulecoin/joulecoin.conf
```

输入 
```
rpcuser=rpc_user
rpcpassword=rpc_passwd 
```
然后再将RPC账号密码更新到config.py的配置文件中。
(安全起见请设置强密码，这里只是实例)
然后重新启动客户端至daemon, 命令为：
```angular2html
./joulecond -daemon
```
## step-3
OK, 焦耳区块链全节点已经部署完毕！只需要等待区块同步完成即可
这时你还可以用命令行体验一下，看看目前当前算力和同步区块数
```angular2html
./joulecoind getmininginfo
```
最后，在Python2.7的环境下面，安装必须的包
```angular2html
pip install -r requirements.txt
```
启动Flask HTTP服务，默认是8000端口
```angular2html
python server.py
```

# 特别说明（必读）
## 基本架构
在开始之前，本文有必要简述一下本API的架构。

JouleNode[RPC] --> FlaskServer[HTTP]
本API包含两个部分，一部分是焦耳区块链节点，它开放的是RPC端口调用，为了大家使用方便（主要是跨语言支持），我们在RPC上面封装了一个简单
Flask HTTP接口，考虑到充值提现场景较为低频，大部分场景下面应该不会遇到太大的效率问题，如果有大家可以自己来进行扩展，提高并发性
##安全警示
本API仅限服务器内网使用，不可以直接在服务中对外开放，否则可能导致积分被盗，请使用时务必保证是内网调用，并定制自己的SECRET_KEY


# 接口实例
## 基本说明
所有接口返回状态中，status=0 表示接口返回成功， status=-1 表示返回错误
## 1. 获取当前挖矿信息
### URL
http://localhost:8000/get_mining_info?verify_key=QhDv4SAM2JEDvDd8
###Response
{
  "mininginfo": {
    "blocks": 415944, 
    "currentblocksize": 0, 
    "currentblocktx": 0, 
    "difficulty": 0.80661440, 
    "errors": "", 
    "generate": false, 
    "genproclimit": -1, 
    "hashespersec": 0, 
    "networkhashps": 122391174, 
    "pooledtx": 0, 
    "testnet": false
  }, 
  "status": 0
}

## 2. 获取当前节点各个账户的余额
###URL
http://localhost:8000/list_accounts?verify_key=QhDv4SAM2JEDvDd8
###Response
{
  "accounts": {
    "": -666.0041, 
    "blank": 0.0, 
    "blank2": 0.0, 
    "main": 1440.0001
  }, 
  "status": 0
}

## 3. 获取某个地址下面收到的总积分值
###URL
http://localhost:8000/get_received_by_address?verify_key=QhDv4SAM2JEDvDd8&address=JLSj8mDh1EvTwNuDqvmKJXoB62oWgXpXJy###Response
###Response
{
  "receivedbyaddress": 1440458.00010000, 
  "status": 0
}

## 4. 获取当前节点的总余额
### URL
http://localhost:8000/get_info?verify_key=QhDv4SAM2JEDvDd8
### Response
{
  "info": {
    "balance": 771151.996, 
    "blocks": 415964, 
    "difficulty": 0.8066144
  }, 
  "status": 0
}


## 5. 获取当前区块链最新区块的信息
###URL
http://localhost:8000/get_best_block?verify_key=QhDv4SAM2JEDvDd8
###Response
{
  "best_block_info": {
    "bits": "1d013d5f", 
    "confirmations": 1, 
    "difficulty": 0.80661440, 
    "hash": "00000000474bbd77b182a489990d480c831357574359aa1015901542774a179f", 
    "height": 415966, 
    "merkleroot": "a712ac32ba3b53a6cb5ed7830b8ee2d45338e1e77fd6228dca12d7c1eda03996", 
    "nonce": 50114, 
    "previousblockhash": "00000001098705cd16138570dbbe8aeeb9bf5312a02d3bd91d023fb18a65b39a", 
    "size": 189, 
    "time": 1533710643, 
    "tx": [
      "a712ac32ba3b53a6cb5ed7830b8ee2d45338e1e77fd6228dca12d7c1eda03996"
    ], 
    "version": 2
  }, 
  "status": 0
}


##6. 往某个地址转账一定金额
传参：address(地址)，amount(金额)
###URL
http://localhost:8000/send_to_address?verify_key=QhDv4SAM2JEDvDd8&address=JLSj8mDh1EvTwNuDqvmKJXoB62oWgXpXJy&amount=1.0
###Response
{
  "status": 0, 
  "tx_id": "df2347a3a9da97976473523e3f01b5037269b4c304584d238d77d046777a528c"
}


##7. 获取某条交易的详细信息
传参：tx_id（交易ID）
注意返回值里面的confirmations参数代表了区块链的确认次数，一般默认是6次确认正式到账，但是方便起见，2次一般也可以认为到账了
###URL
http://localhost:8000/get_transaction?verify_key=QhDv4SAM2JEDvDd8&tx_id=df2347a3a9da97976473523e3f01b5037269b4c304584d238d77d046777a528c
###Response
{
  "status": 0, 
  "tx_info": {
    "amount": 0E-8, 
    "blockhash": "00000000ce84e867a0dcf9b110c2dd91ea076121b6d895dd7879de0928cbe81c", 
    "blockindex": 1, 
    "blocktime": 1533712204, 
    "confirmations": 5, 
    "details": [
      {
        "account": "", 
        "address": "JLSj8mDh1EvTwNuDqvmKJXoB62oWgXpXJy", 
        "amount": -1.00000000, 
        "category": "send", 
        "fee": 0E-8
      }, 
      {
        "account": "main", 
        "address": "JLSj8mDh1EvTwNuDqvmKJXoB62oWgXpXJy", 
        "amount": 1.00000000, 
        "category": "receive"
      }
    ], 
    "fee": 0E-8, 
    "normtxid": "42e19747956d277ea68a41cc7fb9461eaf035da61c04bcc5c8e3afefd970ed05", 
    "time": 1533712194, 
    "timereceived": 1533712194, 
    "txid": "df2347a3a9da97976473523e3f01b5037269b4c304584d238d77d046777a528c"
  }
}


##8. 创建一个新的账户
传参：account_name（要创建的账户名）
###URL
http://localhost:8000/create_new_account?verify_key=QhDv4SAM2JEDvDd8&account_name=blank3
###Response
{
  "account": "blank3", 
  "address": "JWx6usPriDwtxXE7Vv1LATV1ZteQpm5Xmv", 
  "status": 0
}


##9. 获取某个账户下面所有的地址
传参：account_name（要查询的账户名）
###URL
http://localhost:8000/get_addresses_by_account?verify_key=QhDv4SAM2JEDvDd8&account_name=blank3
###Response
{
  "address": [
    "JaejYzRNcJWZNJYpbbNQm4jz7j8mLeMmFZ", 
    "Jefv9rdrq2SuerP48bY9rLBC7CbSAeBwFnF"
  ], 
  "status": 0
}

##10. 获取某个账户新生成的一个地址
传参：account_name（要查询的账户名）
###URL
http://localhost:8000/get_new_address?verify_key=QhDv4SAM2JEDvDd8&account_name=blank3
###Response
{
  "new_address": "JKDNyVAxCKPVYbfDvRZiapGBgdrcVjUEbE", 
  "status": 0
}
