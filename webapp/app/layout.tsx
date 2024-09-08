import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Container from "@/components/layout/provider";
import { Toaster } from "@/components/toaster/sonner";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Chat UI",
  description: "Web3 Plugin to Chat GPT",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Container>
          {children}
          <Toaster />
        </Container>
      </body>

    </html>
  );
}
