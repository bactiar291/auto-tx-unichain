from web3 import Web3
import time

# Koneksi ke node Ethereum melalui HTTP provider (misalnya Infura atau QuikNode)
web3 = Web3(Web3.HTTPProvider('https://autumn-cosmological-scion.unichain-sepolia.quiknode.pro/c568806873f2a9edb9fcdea8aef0569ff729eb25'))

# Verifikasi koneksi
if web3.is_connected():
    print("Terkoneksi dengan jaringan Ethereum")
else:
    raise Exception("Gagal terhubung ke jaringan Ethereum")

# Informasi akun pengirim (wallet utama)
sender_address = 'YOUR_SENDER_ADDRESS_HERE'  # Masukkan alamat pengirim
private_key = 'YOUR_PRIVATE_KEY_HERE'  # Masukkan kunci privat

# Daftar penerima
receivers = [
    '0xb6D8c5f48B5B2467dfd8046C712A591EBCA1Cbdc',
    '0x83eECe161a79b2c158318D4Ec162502A922adC85',
    '0x32EFA31Ebca25F5156DBcDAf7DE1985feB64927D',
    '0xCa7EE5ccf848504e716059a243422eAeB799F074',
    # Tambahkan lebih banyak address jika diperlukan
]

# Jumlah Ether yang dikirim per transaksi (dalam wei)
amount = web3.to_wei(0.000000012, 'ether')  # Contoh: 0.000000012 ETH

# Estimasi gas fee
gas_price = web3.eth.gas_price

# Fungsi untuk mengirim transaksi
def send_transaction(receiver_address, amount, gas_price):
    # Ambil nonce
    nonce = web3.eth.get_transaction_count(sender_address)

    # Buat transaksi
    tx = {
        'nonce': nonce,
        'to': receiver_address,
        'value': amount,
        'gas': 21000,  # Gas limit untuk transaksi biasa
        'gasPrice': gas_price,
        'chainId': 1301  # Sepolia Testnet, ganti ke Mainnet jika diperlukan
    }

    # Tanda tangani transaksi dengan kunci privat
    signed_tx = web3.eth.account.sign_transaction(tx, private_key)

    # Kirim transaksi
    tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

    # Cetak hash transaksi
    print(f"Transaksi berhasil dikirim ke {receiver_address}. Tx Hash: {web3.to_hex(tx_hash)}")

# Kirim transaksi ke setiap wallet
for receiver in receivers:
    send_transaction(receiver, amount, gas_price)
    time.sleep(5)  # Penundaan 5 detik di antara transaksi untuk menghindari nonce error
