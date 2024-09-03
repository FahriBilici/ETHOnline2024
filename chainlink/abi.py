AggregatorV3Interface = '[{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],' \
                        '"stateMutability":"view","type":"function"},{"inputs":[],"name":"description","outputs":[{' \
                        '"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},' \
                        '{"inputs":[{"internalType":"uint80","name":"_roundId","type":"uint80"}],"name":"getRoundData","outputs":[{' \
                        '"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer",' \
                        '"type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256",' \
                        '"name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],' \
                        '"stateMutability":"view","type":"function"},{"inputs":[],"name":"latestRoundData","outputs":[{' \
                        '"internalType":"uint80","name":"roundId","type":"uint80"},{"internalType":"int256","name":"answer",' \
                        '"type":"int256"},{"internalType":"uint256","name":"startedAt","type":"uint256"},{"internalType":"uint256",' \
                        '"name":"updatedAt","type":"uint256"},{"internalType":"uint80","name":"answeredInRound","type":"uint80"}],' \
                        '"stateMutability":"view","type":"function"},{"inputs":[],"name":"version","outputs":[{' \
                        '"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}] '

GaladrielABI = '''
[
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "runId",
				"type": "uint256"
			},
			{
				"components": [
					{
						"internalType": "string",
						"name": "id",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "content",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "functionName",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "functionArguments",
						"type": "string"
					},
					{
						"internalType": "uint64",
						"name": "created",
						"type": "uint64"
					},
					{
						"internalType": "string",
						"name": "model",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "systemFingerprint",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "object",
						"type": "string"
					},
					{
						"internalType": "uint32",
						"name": "completionTokens",
						"type": "uint32"
					},
					{
						"internalType": "uint32",
						"name": "promptTokens",
						"type": "uint32"
					},
					{
						"internalType": "uint32",
						"name": "totalTokens",
						"type": "uint32"
					}
				],
				"internalType": "struct IOracle.OpenAiResponse",
				"name": "_response",
				"type": "tuple"
			},
			{
				"internalType": "string",
				"name": "_errorMessage",
				"type": "string"
			}
		],
		"name": "onOracleOpenAiLlmResponse",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_message",
				"type": "string"
			}
		],
		"name": "sendMessage",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "initialOracleAddress",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_runId",
				"type": "uint256"
			}
		],
		"name": "getMessageHistory",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "role",
						"type": "string"
					},
					{
						"components": [
							{
								"internalType": "string",
								"name": "contentType",
								"type": "string"
							},
							{
								"internalType": "string",
								"name": "value",
								"type": "string"
							}
						],
						"internalType": "struct IOracle.Content[]",
						"name": "content",
						"type": "tuple[]"
					}
				],
				"internalType": "struct IOracle.Message[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "message",
		"outputs": [
			{
				"internalType": "string",
				"name": "role",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "response",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
'''
