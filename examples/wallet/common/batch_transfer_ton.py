from tonutils.client import ToncenterV3Client
from tonutils.wallet import WalletV4R2
from tonutils.wallet.messages import TransferMessage

# Set to True for test network, False for main network
IS_TESTNET = True

# Mnemonic phrase
MNEMONIC = "word1 word2 word3 ..."


async def main() -> None:
    client = ToncenterV3Client(is_testnet=IS_TESTNET, rps=1, max_retries=1)
    wallet, public_key, private_key, mnemonic = WalletV4R2.from_mnemonic(client, MNEMONIC)

    tx_hash = await wallet.batch_transfer_messages(
        messages=[
            TransferMessage(
                destination="UQ...",
                amount=0.01,
                body="Hello from tonutils!",
            ),
            TransferMessage(
                destination="UQ...",
                amount=0.01,
                body="Hello from tonutils!",
            ),
            TransferMessage(
                destination="UQ...",
                amount=0.01,
                body="Hello from tonutils!",
            ),
            TransferMessage(
                destination="UQ...",
                amount=0.01,
                body="Hello from tonutils!",
            ),
        ]
    )

    print("Successfully transferred!")
    print(f"Transaction hash: {tx_hash}")


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
