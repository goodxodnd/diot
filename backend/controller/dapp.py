# DApp Info. 2020.08.10
SystemAbi = '''
[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_did",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_addrEOA",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_addrCA",
				"type": "address"
			}
		],
		"name": "addMember",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_did",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_addrEOA",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_addrCA",
				"type": "address"
			}
		],
		"name": "checkAllAddr",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_did",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_addrCA",
				"type": "address"
			}
		],
		"name": "checkCAAddr",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_did",
				"type": "string"
			},
			{
				"internalType": "address",
				"name": "_addrEOA",
				"type": "address"
			}
		],
		"name": "checkEOAAddr",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_did",
				"type": "string"
			}
		],
		"name": "getCAAddr",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_did",
				"type": "string"
			}
		],
		"name": "hasDID",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]'''
SystemBin = "608060405234801561001057600080fd5b50336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555061109a806100606000396000f3fe608060405234801561001057600080fd5b506004361061007d5760003560e01c80639a2a780c1161005b5780639a2a780c146102c2578063a1ba69c514610393578063e554c67d14610478578063f3df39ac146105695761007d565b806328215130146100825780638b7afd871461017d5780638da5cb5b1461028e575b600080fd5b61017b6004803603606081101561009857600080fd5b81019080803590602001906401000000008111156100b557600080fd5b8201836020820111156100c757600080fd5b803590602001918460018302840111640100000000831117156100e957600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803573ffffffffffffffffffffffffffffffffffffffff16906020019092919050505061065a565b005b6102766004803603606081101561019357600080fd5b81019080803590602001906401000000008111156101b057600080fd5b8201836020820111156101c257600080fd5b803590602001918460018302840111640100000000831117156101e457600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290803573ffffffffffffffffffffffffffffffffffffffff169060200190929190803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610951565b60405180821515815260200191505060405180910390f35b610296610b73565b604051808273ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b61037b600480360360208110156102d857600080fd5b81019080803590602001906401000000008111156102f557600080fd5b82018360208201111561030757600080fd5b8035906020019184600183028401116401000000008311171561032957600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290505050610b97565b60405180821515815260200191505060405180910390f35b61044c600480360360208110156103a957600080fd5b81019080803590602001906401000000008111156103c657600080fd5b8201836020820111156103d857600080fd5b803590602001918460018302840111640100000000831117156103fa57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290505050610c2b565b604051808273ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6105516004803603604081101561048e57600080fd5b81019080803590602001906401000000008111156104ab57600080fd5b8201836020820111156104bd57600080fd5b803590602001918460018302840111640100000000831117156104df57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610d4a565b60405180821515815260200191505060405180910390f35b6106426004803603604081101561057f57600080fd5b810190808035906020019064010000000081111561059c57600080fd5b8201836020820111156105ae57600080fd5b803590602001918460018302840111640100000000831117156105d057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610ea8565b60405180821515815260200191505060405180910390f35b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161461071b576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600f8152602001807f4f776e657273686970204572726f72000000000000000000000000000000000081525060200191505060405180910390fd5b61012c835110610793576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600f8152602001807f4f776e657273686970204572726f72000000000000000000000000000000000081525060200191505060405180910390fd5b61079b61100e565b82816000019073ffffffffffffffffffffffffffffffffffffffff16908173ffffffffffffffffffffffffffffffffffffffff168152505081816020019073ffffffffffffffffffffffffffffffffffffffff16908173ffffffffffffffffffffffffffffffffffffffff1681525050428160400181815250506001816060019015159081151581525050806001856040518082805190602001908083835b6020831061085d578051825260208201915060208101905060208303925061083a565b6001836020036101000a038019825116818451168082178552505050505050905001915050908152602001604051809103902060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060208201518160010160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506040820151816002015560608201518160030160006101000a81548160ff02191690831515021790555090505050505050565b60006001846040518082805190602001908083835b602083106109895780518252602082019150602081019050602083039250610966565b6001836020036101000a038019825116818451168082178552505050505050905001915050908152602001604051809103902060030160009054906101000a900460ff1615610b67578273ffffffffffffffffffffffffffffffffffffffff166001856040518082805190602001908083835b60208310610a1f57805182526020820191506020810190506020830392506109fc565b6001836020036101000a038019825116818451168082178552505050505050905001915050908152602001604051809103902060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16148015610b5057508173ffffffffffffffffffffffffffffffffffffffff166001856040518082805190602001908083835b60208310610ae15780518252602082019150602081019050602083039250610abe565b6001836020036101000a038019825116818451168082178552505050505050905001915050908152602001604051809103902060010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16145b15610b5e5760019050610b6c565b60009050610b6c565b600090505b9392505050565b60008054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b60006001826040518082805190602001908083835b60208310610bcf5780518252602082019150602081019050602083039250610bac565b6001836020036101000a038019825116818451168082178552505050505050905001915050908152602001604051809103902060030160009054906101000a900460ff1615610c215760019050610c26565b600090505b919050565b60006001826040518082805190602001908083835b60208310610c635780518252602082019150602081019050602083039250610c40565b6001836020036101000a038019825116818451168082178552505050505050905001915050908152602001604051809103902060030160009054906101000a900460ff1615610d40576001826040518082805190602001908083835b60208310610ce25780518252602082019150602081019050602083039250610cbf565b6001836020036101000a038019825116818451168082178552505050505050905001915050908152602001604051809103902060010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050610d45565b600090505b919050565b60006001836040518082805190602001908083835b60208310610d825780518252602082019150602081019050602083039250610d5f565b6001836020036101000a038019825116818451168082178552505050505050905001915050908152602001604051809103902060030160009054906101000a900460ff1615610e9d578173ffffffffffffffffffffffffffffffffffffffff166001846040518082805190602001908083835b60208310610e185780518252602082019150602081019050602083039250610df5565b6001836020036101000a038019825116818451168082178552505050505050905001915050908152602001604051809103902060010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161415610e945760019050610ea2565b60009050610ea2565b600090505b92915050565b600060608390506001816040518082805190602001908083835b60208310610ee55780518252602082019150602081019050602083039250610ec2565b6001836020036101000a038019825116818451168082178552505050505050905001915050908152602001604051809103902060030160009054906101000a900460ff1615611002578273ffffffffffffffffffffffffffffffffffffffff166001826040518082805190602001908083835b60208310610f7b5780518252602082019150602081019050602083039250610f58565b6001836020036101000a038019825116818451168082178552505050505050905001915050908152602001604051809103902060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff161415610ff8576001915050611008565b6000915050611008565b60009150505b92915050565b6040518060800160405280600073ffffffffffffffffffffffffffffffffffffffff168152602001600073ffffffffffffffffffffffffffffffffffffffff16815260200160008152602001600015158152509056fea26469706673582212200f59b2a60f8604f6f8c477374de03ae48b1e8c2971c77176aea534ca3d95895864736f6c634300060c0033"

DeviceAbi = '''
[
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [],
		"name": "creator",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "deviceEOA",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getOwner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "ownerTicket",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_payload",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_timestamp",
				"type": "uint256"
			}
		],
		"name": "requestChangeOwner",
		"outputs": [],
		"stateMutability": "payable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_deviceEOA",
				"type": "address"
			}
		],
		"name": "setDeviceDOA",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_ticketAddr",
				"type": "address"
			}
		],
		"name": "setOwnerTicket",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]'''
DeviceBin = "608060405234801561001057600080fd5b5033600260006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555061078a806100616000396000f3fe6080604052600436106100705760003560e01c80634e4fab481161004e5780634e4fab48146101e8578063893d20e8146102395780639534f18a14610290578063baa62cf6146102e757610070565b806302d05d3f146100755780630cc19f23146100cc578063166351bc14610123575b600080fd5b34801561008157600080fd5b5061008a610338565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b3480156100d857600080fd5b506100e161035e565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6101e66004803603604081101561013957600080fd5b810190808035906020019064010000000081111561015657600080fd5b82018360208201111561016857600080fd5b8035906020019184600183028401116401000000008311171561018a57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f82011690508083019250505050505050919291929080359060200190929190505050610384565b005b3480156101f457600080fd5b506102376004803603602081101561020b57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610488565b005b34801561024557600080fd5b5061024e610572565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b34801561029c57600080fd5b506102a5610621565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b3480156102f357600080fd5b506103366004803603602081101561030a57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff169060200190929190505050610647565b005b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6000600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1690508073ffffffffffffffffffffffffffffffffffffffff1663166351bc84846040518363ffffffff1660e01b81526004018080602001838152602001828103825284818151815260200191508051906020019080838360005b8381101561041e578082015181840152602081019050610403565b50505050905090810190601f16801561044b5780820380516001836020036101000a031916815260200191505b509350505050600060405180830381600087803b15801561046b57600080fd5b505af115801561047f573d6000803e3d6000fd5b50505050505050565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff161461052e576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260238152602001806107326023913960400191505060405180910390fd5b80600360006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555050565b600080600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1690508073ffffffffffffffffffffffffffffffffffffffff1663893d20e86040518163ffffffff1660e01b815260040160206040518083038186803b1580156105e057600080fd5b505afa1580156105f4573d6000803e3d6000fd5b505050506040513d602081101561060a57600080fd5b810190808051906020019092919050505091505090565b600360009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16146106ed576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260238152602001806107326023913960400191505060405180910390fd5b80600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055505056fe5468652063726561746f72206f6e6c792063616e20646f207468697320616374696f6ea264697066735822122032c255cb22a2ffdeb979522676e68af63f6281d7f14b3fe6edc4a0a3b1079da864736f6c63430006060033"

UserAbi = '''
[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_addrSystem",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_addrTicket",
				"type": "address"
			},
			{
				"internalType": "string",
				"name": "_userDID",
				"type": "string"
			}
		],
		"name": "acceptRequest",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "addrOwner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "addrSystem",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_deviceDID",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_payload",
				"type": "string"
			}
		],
		"name": "sendRequest",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]'''
UserBin = "608060405234801561001057600080fd5b506040516109ab3803806109ab8339818101604052602081101561003357600080fd5b8101908080519060200190929190505050336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555080600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff160217905550506108d6806100d56000396000f3fe608060405234801561001057600080fd5b506004361061004c5760003560e01c80630413948514610051578063869984c8146101a35780639a8e49a4146101ed578063f3bc44f9146102c8575b600080fd5b6101a16004803603604081101561006757600080fd5b810190808035906020019064010000000081111561008457600080fd5b82018360208201111561009657600080fd5b803590602001918460018302840111640100000000831117156100b857600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f8201169050808301925050505050505091929192908035906020019064010000000081111561011b57600080fd5b82018360208201111561012d57600080fd5b8035906020019184600183028401116401000000008311171561014f57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290505050610312565b005b6101ab6105d4565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6102c66004803603604081101561020357600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291908035906020019064010000000081111561024057600080fd5b82018360208201111561025257600080fd5b8035906020019184600183028401116401000000008311171561027457600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f8201169050808301925050505050505091929192905050506105f9565b005b6102d061087a565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16146103d4576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600f8152602001807f4f776e657273686970204572726f72000000000000000000000000000000000081525060200191505060405180910390fd5b6000600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905060008173ffffffffffffffffffffffffffffffffffffffff1663a1ba69c5856040518263ffffffff1660e01b81526004018080602001828103825283818151815260200191508051906020019080838360005b8381101561046957808201518184015260208101905061044e565b50505050905090810190601f1680156104965780820380516001836020036101000a031916815260200191505b509250505060206040518083038186803b1580156104b357600080fd5b505afa1580156104c7573d6000803e3d6000fd5b505050506040513d60208110156104dd57600080fd5b8101908080519060200190929190505050905060008190508073ffffffffffffffffffffffffffffffffffffffff1663166351bc85426040518363ffffffff1660e01b81526004018080602001838152602001828103825284818151815260200191508051906020019080838360005b8381101561056857808201518184015260208101905061054d565b50505050905090810190601f1680156105955780820380516001836020036101000a031916815260200191505b509350505050600060405180830381600087803b1580156105b557600080fd5b505af11580156105c9573d6000803e3d6000fd5b505050505050505050565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff16146106bb576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600f8152602001807f4f776e657273686970204572726f72000000000000000000000000000000000081525060200191505060405180910390fd5b6000600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905060008173ffffffffffffffffffffffffffffffffffffffff1663a1ba69c5846040518263ffffffff1660e01b81526004018080602001828103825283818151815260200191508051906020019080838360005b83811015610750578082015181840152602081019050610735565b50505050905090810190601f16801561077d5780820380516001836020036101000a031916815260200191505b509250505060206040518083038186803b15801561079a57600080fd5b505afa1580156107ae573d6000803e3d6000fd5b505050506040513d60208110156107c457600080fd5b8101908080519060200190929190505050905060008490508073ffffffffffffffffffffffffffffffffffffffff1663a6f9dae1836040518263ffffffff1660e01b8152600401808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001915050600060405180830381600087803b15801561085b57600080fd5b505af115801561086f573d6000803e3d6000fd5b505050505050505050565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff168156fea26469706673582212208ca82bcc97e8137380c62013fbb33369b57c62578e2016847c7f408460dc0bdc64736f6c63430006060033"

OwnerTicketAbi = '''
[
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_userDAppAddr",
				"type": "address"
			},
			{
				"internalType": "address",
				"name": "_deviceDAppAddr",
				"type": "address"
			}
		],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "_prev",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "_new",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "_device",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "_timestamp",
				"type": "uint256"
			}
		],
		"name": "AcceptEvent",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "_from",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "_to",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "_payload",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "_timestamp",
				"type": "uint256"
			}
		],
		"name": "RejectEvent",
		"type": "event"
	},
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": false,
				"internalType": "address",
				"name": "_from",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "address",
				"name": "_to",
				"type": "address"
			},
			{
				"indexed": false,
				"internalType": "string",
				"name": "_payload",
				"type": "string"
			},
			{
				"indexed": false,
				"internalType": "uint256",
				"name": "_timestamp",
				"type": "uint256"
			}
		],
		"name": "RequestReceived",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "_userDAppAddr",
				"type": "address"
			}
		],
		"name": "changeOwner",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "deviceDAppAddr",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getLogSize",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_idx",
				"type": "uint256"
			}
		],
		"name": "getLogTime",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_idx",
				"type": "uint256"
			}
		],
		"name": "getNewOwner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getOwner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_idx",
				"type": "uint256"
			}
		],
		"name": "getPrevOwner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "invalidate",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_payload",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_timestamp",
				"type": "uint256"
			}
		],
		"name": "requestChangeOwner",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_docOid",
				"type": "string"
			}
		],
		"name": "setOid",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "userDAppAddr",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]'''
OwnerTicketBin = "608060405234801561001057600080fd5b506040516113523803806113528339818101604052604081101561003357600080fd5b8101908080519060200190929190805190602001909291905050508181336000806101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555081600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555080600260006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055505050505061122d806101256000396000f3fe608060405234801561001057600080fd5b50600436106100a95760003560e01c8063893d20e811610071578063893d20e8146102515780639fb2fff41461029b578063a6f9dae1146102a5578063b6ce1cd4146102e9578063f2d03fcf146103a4578063f388d0f214610412576100a9565b80630c73a392146100ae578063166351bc146100cc57806342e1f6f81461014f57806345f1aee6146101bd578063667b246d14610207575b600080fd5b6100b6610454565b6040518082815260200191505060405180910390f35b61014d600480360360408110156100e257600080fd5b81019080803590602001906401000000008111156100ff57600080fd5b82018360208201111561011157600080fd5b8035906020019184600183028401116401000000008311171561013357600080fd5b909192939192939080359060200190929190505050610461565b005b61017b6004803603602081101561016557600080fd5b810190808035906020019092919050505061061e565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6101c56107cc565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b61020f6107f2565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b610259610818565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b6102a3610842565b005b6102e7600480360360208110156102bb57600080fd5b81019080803573ffffffffffffffffffffffffffffffffffffffff1690602001909291905050506109a7565b005b6103a2600480360360208110156102ff57600080fd5b810190808035906020019064010000000081111561031c57600080fd5b82018360208201111561032e57600080fd5b8035906020019184600183028401116401000000008311171561035057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290505050610ce1565b005b6103d0600480360360208110156103ba57600080fd5b8101908080359060200190929190505050610da1565b604051808273ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200191505060405180910390f35b61043e6004803603602081101561042857600080fd5b8101908080359060200190929190505050610f4f565b6040518082815260200191505060405180910390f35b6000600560000154905090565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614610524576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601e8152602001807f4f6e6c79206465766963652063616e20646f207468697320616374696f6e000081525060200191505060405180910390fd5b7f32ca6a5ef1bf3c53448d9044f5f2cbabaea3713f9393039c6df12b0be7d179fd33600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16858585604051808673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001806020018381526020018281038252858582818152602001925080828437600081840152601f19601f820116905080830192505050965050505050505060405180910390a1505050565b6000813073ffffffffffffffffffffffffffffffffffffffff16630c73a3926040518163ffffffff1660e01b815260040160206040518083038186803b15801561066757600080fd5b505afa15801561067b573d6000803e3d6000fd5b505050506040513d602081101561069157600080fd5b810190808051906020019092919050505011610715576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600e8152602001807f496e646578206f766572666c6f7700000000000000000000000000000000000081525060200191505060405180910390fd5b6000821061078b576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600f8152602001807f496e64657820756e646572666c6f77000000000000000000000000000000000081525060200191505060405180910390fd5b6005600101600083815260200190815260200160002060010160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050919050565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1681565b6000600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16905090565b600260009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614610905576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252601e8152602001807f4f6e6c79206465766963652063616e20646f207468697320616374696f6e000081525060200191505060405180910390fd5b6000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff166108fc479081150290604051600060405180830381858888f1935050505015801561096c573d6000803e3d6000fd5b506000809054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16ff5b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614610a4d576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260288152602001806111d06028913960400191505060405180910390fd5b610a556110dd565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16816000019073ffffffffffffffffffffffffffffffffffffffff16908173ffffffffffffffffffffffffffffffffffffffff168152505081816020019073ffffffffffffffffffffffffffffffffffffffff16908173ffffffffffffffffffffffffffffffffffffffff1681525050428160400181815250508060056001016000600560000154815260200190815260200160002060008201518160000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555060208201518160010160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055506040820151816002015590505060056000016000815480929190600101919050555081600160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff1602179055507fde50f652553c30e2593729af0a62bda1a5fcff10a0df157ecab1c291c7ef3db381600001518260200151308460400151604051808573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020018373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200182815260200194505050505060405180910390a15050565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614610d87576040517f08c379a00000000000000000000000000000000000000000000000000000000081526004018080602001828103825260288152602001806111d06028913960400191505060405180910390fd5b8060039080519060200190610d9d92919061112a565b5050565b6000813073ffffffffffffffffffffffffffffffffffffffff16630c73a3926040518163ffffffff1660e01b815260040160206040518083038186803b158015610dea57600080fd5b505afa158015610dfe573d6000803e3d6000fd5b505050506040513d6020811015610e1457600080fd5b810190808051906020019092919050505011610e98576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600e8152602001807f496e646578206f766572666c6f7700000000000000000000000000000000000081525060200191505060405180910390fd5b60008210610f0e576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600f8152602001807f496e64657820756e646572666c6f77000000000000000000000000000000000081525060200191505060405180910390fd5b6005600101600083815260200190815260200160002060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169050919050565b6000813073ffffffffffffffffffffffffffffffffffffffff16630c73a3926040518163ffffffff1660e01b815260040160206040518083038186803b158015610f9857600080fd5b505afa158015610fac573d6000803e3d6000fd5b505050506040513d6020811015610fc257600080fd5b810190808051906020019092919050505011611046576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600e8152602001807f496e646578206f766572666c6f7700000000000000000000000000000000000081525060200191505060405180910390fd5b600082106110bc576040517f08c379a000000000000000000000000000000000000000000000000000000000815260040180806020018281038252600f8152602001807f496e64657820756e646572666c6f77000000000000000000000000000000000081525060200191505060405180910390fd5b60056001016000838152602001908152602001600020600201549050919050565b6040518060600160405280600073ffffffffffffffffffffffffffffffffffffffff168152602001600073ffffffffffffffffffffffffffffffffffffffff168152602001600081525090565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061116b57805160ff1916838001178555611199565b82800160010185558215611199579182015b8281111561119857825182559160200191906001019061117d565b5b5090506111a691906111aa565b5090565b6111cc91905b808211156111c85760008160009055506001016111b0565b5090565b9056fe4f6e6c7920746865207469636b6574206f776e65722063616e20646f207468697320616374696f6ea2646970667358221220baab657c81949a0de4df071623eb792af0327456deadafdbe2e5a51cd3fb64cc64736f6c63430006060033"