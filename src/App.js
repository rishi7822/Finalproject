// App.js
import React, { useState, useEffect } from 'react';
import { Connection, PublicKey, clusterApiUrl, Transaction, SystemProgram, sendAndConfirmTransaction } from '@solana/web3.js';

function App() {
  const [connected, setConnected] = useState(false);
  const [walletBalance, setWalletBalance] = useState(null);
  const [walletPublicKey, setWalletPublicKey] = useState(null);
  const [transactionStatus, setTransactionStatus] = useState(null);
  const [recipientAddress, setRecipientAddress] = useState('');
  const [transactionAmount, setTransactionAmount] = useState(0);

  const network = clusterApiUrl('devnet'); // Use 'mainnet-beta' for the mainnet
  const connection = new Connection(network);

  useEffect(() => {
    if (window.solana && window.solana.wallet) {
      setConnected(true);
      const publicKey = new PublicKey(window.solana.wallet.publicKey.toBase58());
      setWalletPublicKey(publicKey);

      // Fetch and display the wallet balance
      connection.getBalance(publicKey).then((balance) => {
        setWalletBalance(balance / 10 ** 9); // Convert lamports to SOL
      });
    }
  }, [connection]);

  // Function to send a custom transaction
  async function sendTransaction() {
    if (connected && walletPublicKey && recipientAddress && transactionAmount > 0) {
      try {
        const recipientPubkey = new PublicKey(recipientAddress);

        // Create a new transaction
        const transaction = new Transaction().add(
          SystemProgram.transfer({
            fromPubkey: walletPublicKey,
            toPubkey: recipientPubkey,
            lamports: transactionAmount * 10 ** 9, // Convert SOL to lamports
          })
        );

        // Sign and send the transaction
        const signature = await window.solana.wallet.signTransaction(transaction);
        const result = await sendAndConfirmTransaction(connection, transaction, [signature]);

        setTransactionStatus(`Transaction sent. Transaction ID: ${result}`);
        setRecipientAddress('');
        setTransactionAmount(0);
      } catch (error) {
        console.error('Error sending transaction:', error);
        setTransactionStatus('Transaction failed.');
      }
    }
  }

  // Function to handle recipient address input
  function handleRecipientChange(event) {
    setRecipientAddress(event.target.value.trim());
  }

  // Function to handle transaction amount input
  function handleAmountChange(event) {
    setTransactionAmount(parseFloat(event.target.value));
  }

  // Function to connect the Phantom wallet
  async function connectToPhantom() {
    if (window.solana) {
      try {
        await window.solana.connect();
        // After connecting, you can update the connected state and fetch wallet data if needed
        setConnected(true);
      } catch (error) {
        console.error('Failed to connect to Phantom:', error);
      }
    } else {
      console.error('Phantom wallet extension not found.');
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <h1>Interact with Phantom Wallet</h1>
        {connected ? (
          <>
            <p>Connected to Phantom Wallet</p>
            <p>Wallet Balance: {walletBalance} SOL</p>
            <label>
              Recipient Address:
              <input type="text" value={recipientAddress} onChange={handleRecipientChange} />
            </label>
            <label>
              Transaction Amount (SOL):
              <input type="number" value={transactionAmount} onChange={handleAmountChange} />
            </label>
            <button onClick={sendTransaction}>Send Transaction</button>
            {transactionStatus && <p>{transactionStatus}</p>}
          </>
        ) : (
          <button onClick={connectToPhantom}>Connect Wallet</button>
        )}
      </header>
    </div>
  );
}

export default App;
