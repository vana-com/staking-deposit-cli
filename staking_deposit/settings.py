from typing import Dict, NamedTuple
from eth_utils import decode_hex

DEPOSIT_CLI_VERSION = '2.7.0'


class BaseChainSetting(NamedTuple):
    NETWORK_NAME: str
    GENESIS_FORK_VERSION: bytes
    GENESIS_VALIDATORS_ROOT: bytes


MAINNET = 'mainnet'
GOERLI = 'goerli'
PRATER = 'prater'
SEPOLIA = 'sepolia'
ZHEJIANG = 'zhejiang'
HOLESKY = 'holesky'

VANA_MAINNET = 'vana_mainnet'
VANA_MOKSHA = 'vana_moksha'
VANA_MAYA = 'vana_maya'

# Mainnet setting
MainnetSetting = BaseChainSetting(
    NETWORK_NAME=MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('00000000'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('4b363db94e286120d76eb905340fdd4e54bfe9f06bf33ff6cf5ad27f511bfe95'))
# Goerli setting
GoerliSetting = BaseChainSetting(
    NETWORK_NAME=GOERLI, GENESIS_FORK_VERSION=bytes.fromhex('00001020'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('043db0d9a83813551ee2f33450d23797757d430911a9320530ad8a0eabc43efb'))
# Sepolia setting
SepoliaSetting = BaseChainSetting(
    NETWORK_NAME=SEPOLIA, GENESIS_FORK_VERSION=bytes.fromhex('90000069'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('d8ea171f3c94aea21ebc42a1ed61052acf3f9209c00e4efbaaddac09ed9b8078'))
# Zhejiang setting
ZhejiangSetting = BaseChainSetting(
    NETWORK_NAME=ZHEJIANG, GENESIS_FORK_VERSION=bytes.fromhex('00000069'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('53a92d8f2bb1d85f62d16a156e6ebcd1bcaba652d0900b2c2f387826f3481f6f'))
# Holesky setting
HoleskySetting = BaseChainSetting(
    NETWORK_NAME=HOLESKY, GENESIS_FORK_VERSION=bytes.fromhex('01017000'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('9143aa7c615a7f7115e2b6aac319c03529df8242ae705fba9df39b79c59fa8b1'))

# Vana Mainnet setting
VanaSetting = BaseChainSetting(
    NETWORK_NAME=VANA_MAINNET, GENESIS_FORK_VERSION=bytes.fromhex('20000089'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('7a2ee1f3a4332b8a3229efd4cba0903049bc8b1e7cd1fe46052e320cf3f6d184'))
# Vana Moksha setting
VanaMokshaSetting = BaseChainSetting(
    NETWORK_NAME=VANA_MOKSHA, GENESIS_FORK_VERSION=bytes.fromhex('20000089'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('256a8b1abd2d74a87eac1b1d1c16d1e56341951dc7b81b235c2b8bdb03470eef'))
# Vana Maya setting
VanaMayaSetting = BaseChainSetting(
    NETWORK_NAME=VANA_MAYA, GENESIS_FORK_VERSION=bytes.fromhex('20000089'),
    GENESIS_VALIDATORS_ROOT=bytes.fromhex('60bf4eb36d0b502dd08035c113c1d793a3f2a7c9ab1e4eb4f6de12ab1854422b'))

ALL_CHAINS: Dict[str, BaseChainSetting] = {
    MAINNET: MainnetSetting,
    GOERLI: GoerliSetting,
    PRATER: GoerliSetting,  # Prater is the old name of the Prater/Goerli testnet
    SEPOLIA: SepoliaSetting,
    ZHEJIANG: ZhejiangSetting,
    HOLESKY: HoleskySetting,
    VANA_MAINNET: VanaSetting,
    VANA_MOKSHA: VanaMokshaSetting,
    VANA_MAYA: VanaMayaSetting,
}


def get_chain_setting(chain_name: str = MAINNET) -> BaseChainSetting:
    return ALL_CHAINS[chain_name]


def get_devnet_chain_setting(network_name: str,
                             genesis_fork_version: str,
                             genesis_validator_root: str) -> BaseChainSetting:
    return BaseChainSetting(
        NETWORK_NAME=network_name,
        GENESIS_FORK_VERSION=decode_hex(genesis_fork_version),
        GENESIS_VALIDATORS_ROOT=decode_hex(genesis_validator_root),
    )
