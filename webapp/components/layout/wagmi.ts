import { defaultWagmiConfig } from '@web3modal/wagmi/react/config'

import { cookieStorage, createStorage } from 'wagmi'
import { mainnet, sepolia } from 'wagmi/chains'
import { createWalletClient, custom } from 'viem'
import { arbitrumSepolia, polygonMumbai } from 'viem/chains'

// Get projectId at https://cloud.walletconnect.com
export const projectId = process.env.NEXT_PUBLIC_PROJECT_ID!

const metadata = {
  name: 'ChatUI',
  description: 'ChatUI',
  url: '', // origin must match your domain & subdomain
  icons: []
}
// Create wagmiConfig
export const config = defaultWagmiConfig({
    chains: [mainnet, arbitrumSepolia], // required
    projectId, // required
    metadata, // required
    ssr: true,
    storage: createStorage({
      storage: cookieStorage
    }),
    enableWalletConnect: true, // Optional - true by default
    enableInjected: true, // Optional - true by default
    enableEIP6963: true, // Optional - true by default
    enableCoinbase: true, // Optional - true by default
  })

export const client = createWalletClient({
    chain: arbitrumSepolia,
    transport: custom(window.ethereum!)
})