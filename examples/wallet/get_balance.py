from tonutils.client import ToncenterV3Client
from tonutils.utils import to_nano
from tonutils.wallet import (
    WalletV3R1,
    # Uncomment the following lines to use different wallet versions:
    # WalletV3R2,
    # WalletV4R1,
    # WalletV4R2,
    # WalletV5R1,
    # HighloadWalletV2,
    # HighloadWalletV3,
)

# Set to True for test network, False for main network
IS_TESTNET = True

# Mnemonic phrase
MNEMONIC = "word1 word2 word3 ..."


async def main() -> None:
    client = ToncenterV3Client(is_testnet=IS_TESTNET, rps=1, max_retries=1)
    wallet, public_key, private_key, mnemonic = WalletV3R1.from_mnemonic(client, MNEMONIC)

    # Uncomment and use the following lines to create different wallet versions from mnemonic:
    # wallet, public_key, private_key, mnemonic = WalletV3R2.from_mnemonic(client, MNEMONIC)
    # wallet, public_key, private_key, mnemonic = WalletV4R1.from_mnemonic(client, MNEMONIC)
    # wallet, public_key, private_key, mnemonic = WalletV4R2.from_mnemonic(client, MNEMONIC)
    # wallet, public_key, private_key, mnemonic = WalletV5R1.from_mnemonic(client, MNEMONIC)
    # wallet, public_key, private_key, mnemonic = HighloadWalletV2.from_mnemonic(client, MNEMONIC)
    # wallet, public_key, private_key, mnemonic = HighloadWalletV3.from_mnemonic(client, MNEMONIC)

    balance = await wallet.balance()

    print(f"Wallet balance (nano): {to_nano(balance)}")
    print(f"Wallet balance (TON): {balance}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
