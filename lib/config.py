import sys
import os

BLOCKCHAIN_SERVICE_NAME = 'insight'
BLOCKCHAIN_SERVICE_CONNECT = 'http://127.0.0.1:3000'

BACKEND_RPC_USER = 'pepeuser'
BACKEND_RPC_PASSWORD = 'peperpcpass'
RPC_USER = 'pepeuser'
RPC_PASSWORD = 'peperpcpass'

"""Variables prefixed with `DEFAULT` should be able to be overridden by
configuration file and command‐line arguments."""

UNIT = 100000000        # The same across assets.


# Versions
VERSION_MAJOR = 9
VERSION_MINOR = 39
VERSION_REVISION = 0
VERSION_STRING = str(VERSION_MAJOR) + '.' + str(VERSION_MINOR) + '.' + str(VERSION_REVISION)


# Counterparty protocol
TXTYPE_FORMAT = '>I'

TWO_WEEKS = 2 * 7 * 24 * 3600
MAX_EXPIRATION = 4 * 2016   # Two months

MEMPOOL_BLOCK_HASH = 'mempool'
MEMPOOL_BLOCK_INDEX = 9999999


# SQLite3
MAX_INT = 2**63 - 1


# Bitcoin Core
OP_RETURN_MAX_SIZE = 160 # bytes


# Currency agnosticism
BTC = 'PEPE'
XCP = 'KDAQ'

BTC_NAME = 'Pepecoin'
BTC_CLIENT = 'pepecoind'
XCP_NAME = 'Kekdaq'
XCP_CLIENT = 'kekdaqd'

DEFAULT_RPC_PORT_TESTNET = 19377
DEFAULT_RPC_PORT = 9377

DEFAULT_BACKEND_RPC_PORT_TESTNET = 39376
DEFAULT_BACKEND_RPC_PORT = 29376

UNSPENDABLE_TESTNET = 'mvKekDaqXXXXXXXXXXXXXXXXXXXXaupTK1'
UNSPENDABLE_MAINNET = 'PKekDaqXXXXXXXXXXXXXXXXXXXXXWH8yfH'

ADDRESSVERSION_TESTNET = b'\x6f'
# PRIVATEKEY_VERSION_TESTNET =
ADDRESSVERSION_MAINNET = b'\x37'
# PRIVATEKEY_VERSION_MAINNET =
MAGIC_BYTES_TESTNET = b'\x3a\xc4\x2c\x2f'   # For bip-0010
MAGIC_BYTES_MAINNET = b'\x3a\xc4\x2c\x2f'   # For bip-0010

WIF_PREFIX_TESTNET = b'\xf1'
WIF_PREFIX_MAINNET = b'\x99'

BLOCK_FIRST_TESTNET_TESTCOIN = 0
BURN_START_TESTNET_TESTCOIN = BLOCK_FIRST_TESTNET_TESTCOIN
BURN_END_TESTNET_TESTCOIN = 4017708    # Fifty years, at 1 minute per block.

BLOCK_FIRST_TESTNET = BLOCK_FIRST_TESTNET_TESTCOIN
BURN_START_TESTNET =  BURN_START_TESTNET_TESTCOIN
BURN_END_TESTNET = 4017708             # Fifty years, at 1 minute per block.

BLOCK_FIRST_MAINNET_TESTCOIN = 668000
BURN_START_MAINNET_TESTCOIN = BLOCK_FIRST_MAINNET_TESTCOIN
BURN_END_MAINNET_TESTCOIN = 1186400    # Fifty years, at 1 minute per block.

BLOCK_FIRST_MAINNET = BLOCK_FIRST_MAINNET_TESTCOIN
BURN_START_MAINNET = BURN_START_MAINNET_TESTCOIN
BURN_END_MAINNET = BURN_START_MAINNET + 6*30*24*60    # 6 months (6*30=180) days burn period with 1 min target time per block.

BURN_SECOND_START = 1489487
BURN_SECOND_END = 3000000

MAX_BURN_BY_ADDRESS = 1000000 * UNIT 	# 5M PEPE.
BURN_MULTIPLIER = 50 				        # from 55 to 50 KDAQ per 1 PEPE.
BURN_SECOND_MULTIPLIER = 10

# Protocol defaults
# NOTE: If the DUST_SIZE constants are changed, they MUST also be changed in kekdaqd/lib/config.py as well
DEFAULT_REGULAR_DUST_SIZE = 0.0001 * UNIT 		  
DEFAULT_MULTISIG_DUST_SIZE = 0.0001 * UNIT * 2 
DEFAULT_OP_RETURN_VALUE = 0 			    # 0 PEPE.
DEFAULT_FEE_PER_KB = 0.01 * UNIT             # 0.01 PEPE.


# UI defaults
DEFAULT_FEE_FRACTION_REQUIRED = .009   # 0.90%
DEFAULT_FEE_FRACTION_PROVIDED = .01    # 1.00%

