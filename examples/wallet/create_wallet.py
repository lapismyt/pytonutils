from tonutils.client import ToncenterV3Client
from tonutils.wallet import (
    # Uncomment the following lines to use different wallet versions:
    # WalletV2R1,
    # WalletV2R2,
    # WalletV3R1,
    # WalletV3R2,
    # WalletV4R1,
    WalletV4R2,
    # WalletV5R1,
    # HighloadWalletV2,
    # HighloadWalletV3,
    # PreprocessedWalletV2,
    # PreprocessedWalletV2R1,
)

# Set to True for test network, False for main network
IS_TESTNET = True


def main() -> None:
    client = ToncenterV3Client(is_testnet=IS_TESTNET, rps=1, max_retries=1)
    wallet, public_key, private_key, mnemonic = WalletV4R2.create(client)

    # Uncomment and use the following lines to create different wallet versions:
    # wallet, public_key, private_key, mnemonic = WalletV3R2.create(client)
    # wallet, public_key, private_key, mnemonic = WalletV4R1.create(client)
    # wallet, public_key, private_key, mnemonic = WalletV4R2.create(client)
    # wallet, public_key, private_key, mnemonic = WalletV5R1.create(client)
    # wallet, public_key, private_key, mnemonic = HighloadWalletV2.create(client)
    # wallet, public_key, private_key, mnemonic = HighloadWalletV3.create(client)
    # wallet, public_key, private_key, mnemonic = PreprocessedWalletV2.create(client)
    # wallet, public_key, private_key, mnemonic = PreprocessedWalletV2R1.create(client)

    print("Wallet has been successfully created!")
    print(f"Address: {wallet.address.to_str()}")
    print(f"Mnemonic: {mnemonic}")


if __name__ == "__main__":
    main()
