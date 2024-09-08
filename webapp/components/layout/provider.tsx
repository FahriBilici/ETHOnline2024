"use client"
import { config } from "./wagmi";
import { MetaMaskUIProvider } from "@metamask/sdk-react-ui";
import { WagmiProvider } from 'wagmi';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { HTMLProps } from "react";
import Navbar from "./navbar";
import Footer from "./footer";


export const viewport = {
  width: 'device-width',
  initialScale: 1,
  maximumScale: 1,
  userScalable: 1,
}

const queryClient = new QueryClient()

function Container({ children }: Readonly<HTMLProps<HTMLDivElement>>) {
  return (
    <div lang="en">
      <MetaMaskUIProvider
        sdkOptions={{
          dappMetadata: {
            name: "ChatUI",
          },
          infuraAPIKey: process.env.NEXT_PUBLIC_INFURA_API_KEY,
        }}
      >
        <WagmiProvider config={config}>
          <QueryClientProvider client={queryClient}>
            <Navbar/>

            {children}
            <Footer/>
          </QueryClientProvider>
        </WagmiProvider>
      </MetaMaskUIProvider>
    </div>
  );
}

export default Container;