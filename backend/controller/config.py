# Config 정보
import enum

CONFIG = {
    'REDIS-IP': '210.114.89.152',
    'REDIS_PORT': '15900',
    # 'R-CHANNEL': 'orderChannel',    # Receiving Channel
    # 'S-CHANNEL': 'resChannel',      # Sending Channel
    'GANACHE': 'http://localhost:7545', # Ganache URL, 실제 적용 시에 적절한 값으로 바뀌어야 함.
    'RPC-URL': 'http://210.114.89.52:8545', # RPC URL, 실제 적용 시에 적절한 값으로 바뀌어야 함.
    # 'ADAM': '0xb3b4ef17ba517e75b79169354fd9dfff51b9d592'
    'SYSTEM_EOA': '0xdd13ef496458b1fd6b68410FD4939Fc63B039051',
    'JOHN_EOA': '0xb209cE7eDd8E14898226ff1c697ed82D03ECB702',
    'BOB_EOA': '0x6ADCe01a571d9440f867f8896D96651CAd80F5AB',
    'DEVICE_EOA': '0x2cc7759e911cE401621f41bB7555Fb58BFB241D1',
    'SYSTEM_DAPP': '0xE847cD46C55b8050b64d5a8031d692333DFCd190',
    'JOHN_DAPP': '0xB6527ACf88f03fdb384675afDDCE1295f01A2867',
    'BOB_DAPP': '0xa592c07c24779CcD497E5cbd2B3DdC192C3113e18',
    'DEVICE_DAPP': '0x9F47DEB785FF34c9b06C97644D004B84026e6572',
    'OWNER_TICKET_DAPP': '0x737C3350D90eFF38F71FFff08A5A42A112122F6e'
}

CMD = {
    'GET_BALANCE': 'getBalance', # query balance
    'CALL_FUNCTION': 'callFunction', # DApp의 메서드를 호출
    'CALL_TX': 'callTx',            # Call Tx of DApp
    'CREATE_ACCOUNT': 'createAccount', # 계정을 생성
    'DEPLOY_DAPP': 'deployDApp',     # DApp을 Deployment
    'GET_BLOCK': 'getBlock',     # Block에 대한 정보를 보여줌.
    'GET_TX': 'getTx',           # TX에 대한 정보를 보여줌.
    'FILL_ETH': 'fillEth',       # ether를 채우는 명령
    'PING': 'ping'               # ping method
}


class ResCode(enum.Enum):
    OK = 200
    SERVER_FAIL = 500
    TIME_OUT = 501
    BLOCKCHAIN_ERR = 502


class NetType(enum.Enum):
    GANACHE = 1
    GETH = 2


class Mode(enum.Enum):
    PRODUCT = 1
    DEV = 2


# Error code
ERR_SERVER_FAIL = 500
