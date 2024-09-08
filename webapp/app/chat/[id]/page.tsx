"use client"
import {
    SignProtocolClient,
    SpMode,
    EvmChains,
    OffChainSignType,
} from "@ethsign/sp-sdk";
import { useParams } from "next/navigation";
import { useEffect, useState } from "react";
import { privateKeyToAccount } from "viem/accounts";

const ChatHistory = () => {

    const cidParam = useParams()?.id
    const baseURL = "https://scan.sign.global/attestation/"
    const [verifiedAttestationId, setVerifiedAttestationId] = useState("")

    const attestChat = async (cid: string) => {
        const client = new SignProtocolClient(SpMode.OffChain, {
            signType: OffChainSignType.EvmEip712,
            account: privateKeyToAccount(`0x${process.env.NEXT_PUBLIC_PRIVATE_KEY!}`), // Optional
        });

        // Create schema
        const schemaInfo = await client.createSchema({
            name: "xxx",
            data: [{ name: "cid", type: "string" }],
        });

        // Create attestation
        const attestationInfo = await client.createAttestation({
            schemaId: schemaInfo.schemaId,
            data: { cid: cid },
            indexingValue: "xxx",
        });

        // Revoke attestation
        const revokeAttestationRes = await client.revokeAttestation(attestationInfo.attestationId, {
            reason: "verify_cid",
        });
        setVerifiedAttestationId(revokeAttestationRes.attestationId)
    }

    useEffect(() => {
        if (cidParam) {
            attestChat(cidParam as string)
        }
    }, [cidParam])

    return (
        <div className="bg-white h-screen mt-10 py-6 sm:py-8 lg:py-12">
            <div className="mx-auto max-w-screen-2xl px-4 md:px-8">
                <div className="flex flex-col items-center justify-between gap-4 rounded-lg bg-gray-100 p-4 sm:flex-row md:p-8">
                    <div>
                        <h2 className="text-xl font-bold text-indigo-500 md:text-2xl">Your Attestation is done.</h2>
                        <p className="text-gray-600">Do you want to check ?</p>
                    </div>

                    <a href={`${baseURL}${verifiedAttestationId}`} className="inline-block rounded-lg bg-indigo-500 px-8 py-3 text-center text-sm font-semibold text-white outline-none ring-indigo-300 transition duration-100 hover:bg-indigo-600 focus-visible:ring active:bg-indigo-700 md:text-base">See Live</a>
                </div>
            </div>
        </div>
    )
}

export default ChatHistory