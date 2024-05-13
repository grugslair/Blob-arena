mergeInto(LibraryManager.library,
{
	IsWalletAvailable: function()
	{
		if (window.starknet)
		{
			return true;
		}
		else
		{
			return false;
		}
	},

	AskToInstallWallet: function()
	{
		window.alert("Please install Starknet Wallet");
	},

	ConnectWalletArgentX: async function()
	{
		if (window.starknet_argentX)
		{
			await window.starknet_argentX.enable();
		}
	},

	ConnectWalletBraavos: async function()
	{
		if (window.starknet_braavos)
		{
			await window.starknet_braavos.enable();
		}
	},

	IsConnected: function()
	{
		if (window.starknet && window.starknet.isConnected){
			return true;
		}
		else if (window.starknet && window.starknet_braavos){
			if (window.starknet_braavos.isConnected){
				return true;
			}
			else{
				return false;
			}
		}
		else{
			return false;
		}
	},

	GetAccount: function()
	{	
		var address = "";

		if (window.starknet.isConnected){
			address = window.starknet.account.address
		}
		else if (window.starknet_braavos.isConnected){
			address = window.starknet_braavos.account.address
		}

		var bufferSize = lengthBytesUTF8(address) + 1;
		var buffer = _malloc(bufferSize);
		stringToUTF8(address, buffer, bufferSize);
		return buffer;
	},

	//delete the ones below
	SendTransactionArgentX: async function(contractAddress, entrypoint, calldata, callbackObjectName, callbackMethodName)
	{
		const jsStringToWasm = (str) => {
			var bufferSize = lengthBytesUTF8(str) + 1;
			var buffer = _malloc(bufferSize);
			stringToUTF8(str, buffer, bufferSize);
			return buffer;
		}
		
		const calldataArray = JSON.parse(UTF8ToString(calldata))
		const contractAddressStr = UTF8ToString(contractAddress)
		const entrypointStr = UTF8ToString(entrypoint)
		const callbackObjectStr = UTF8ToString(callbackObjectName)
		const callbackMethodStr = UTF8ToString(callbackMethodName)

		await window.starknet_argentX.enable();
		if (window.starknet_argentX.selectedAddress)
		{
			window.starknet_argentX.account.execute([{
				contractAddress: contractAddressStr,
				entrypoint: entrypointStr,
				calldata: calldataArray.array
			}]).then((response) => {
				const transactionHash = response.transaction_hash;
				gameInstance.SendMessage(callbackObjectStr, callbackMethodStr, transactionHash);
			}).catch((error) => {
				const errorMessage = error.message;
				gameInstance.SendMessage(callbackObjectStr, callbackMethodStr, errorMessage);
			})	
		}
	},

	SendTransactionBraavos: async function(contractAddress, entrypoint, calldata, callbackObjectName, callbackMethodName)
	{
		const jsStringToWasm = (str) => {
			var bufferSize = lengthBytesUTF8(str) + 1;
			var buffer = _malloc(bufferSize);
			stringToUTF8(str, buffer, bufferSize);
			return buffer;
		}
		
		const calldataArray = JSON.parse(UTF8ToString(calldata))
		const contractAddressStr = UTF8ToString(contractAddress)
		const entrypointStr = UTF8ToString(entrypoint)
		const callbackObjectStr = UTF8ToString(callbackObjectName)
		const callbackMethodStr = UTF8ToString(callbackMethodName)

		await window.starknet_braavos.enable();
		if (window.starknet_braavos.selectedAddress)
		{
			window.starknet_braavos.account.execute([{
				contractAddress: contractAddressStr,
				entrypoint: entrypointStr,
				calldata: calldataArray.array
			}]).then((response) => {
				const transactionHash = response.transaction_hash;
				gameInstance.SendMessage(callbackObjectStr, callbackMethodStr, transactionHash);
			}).catch((error) => {
				const errorMessage = error.message;
				gameInstance.SendMessage(callbackObjectStr, callbackMethodStr, errorMessage);
			})	
		}
	},

	SendTransaction: async function(contractAddress, entrypoint, calldata, callbackObjectName, callbackMethodName)
	{
		const jsStringToWasm = (str) => {
			var bufferSize = lengthBytesUTF8(str) + 1;
			var buffer = _malloc(bufferSize);
			stringToUTF8(str, buffer, bufferSize);
			return buffer;
		}
		
		const calldataArray = JSON.parse(UTF8ToString(calldata))
		const contractAddressStr = UTF8ToString(contractAddress)
		const entrypointStr = UTF8ToString(entrypoint)
		const callbackObjectStr = UTF8ToString(callbackObjectName)
		const callbackMethodStr = UTF8ToString(callbackMethodName)

		if (window.starknet.isConnected){
			await window.starknet.enable();
			if (window.starknet.selectedAddress)
			{
				window.starknet.account.execute([{
					contractAddress: contractAddressStr,
					entrypoint: entrypointStr,
					calldata: calldataArray.array
				}]).then((response) => {
					const transactionHash = response.transaction_hash;
					console.log(transactionHash);
					gameInstance.SendMessage(callbackObjectStr, callbackMethodStr, transactionHash);
				}).catch((error) => {
					const errorMessage = error.message;
					gameInstance.SendMessage(callbackObjectStr, callbackMethodStr, errorMessage);
				})
			}
		}
		else if (window.starknet_braavos.isConnected)
		{
			await window.starknet_braavos.enable();
			if (window.starknet_braavos.selectedAddress)
			{
				window.starknet_braavos.account.execute([{
					contractAddress: contractAddressStr,
					entrypoint: entrypointStr,
					calldata: calldataArray.array
				}]).then((response) => {
					const transactionHash = response.transaction_hash;
					gameInstance.SendMessage(callbackObjectStr, callbackMethodStr, transactionHash);
				}).catch((error) => {
					const errorMessage = error.message;
					gameInstance.SendMessage(callbackObjectStr, callbackMethodStr, errorMessage);
				})	
			}
		}
	},

	SendMultiCallTransaction: async function(callsJson, callbackObjectName, callbackMethodName) {
		const jsStringToWasm = (str) => {
			var bufferSize = lengthBytesUTF8(str) + 1;
			var buffer = _malloc(bufferSize);
			stringToUTF8(str, buffer, bufferSize);
			return buffer;
		}
	
		var processedCalls = UTF8ToString(callsJson)
		const callbackObjectStr = UTF8ToString(callbackObjectName)
		const callbackMethodStr = UTF8ToString(callbackMethodName)

		const parsedObject = eval('(' + processedCalls + ')');

		if (window.starknet.isConnected){
			await window.starknet.enable();
				if (window.starknet.selectedAddress) {
				window.starknet.account.execute( parsedObject )
					.then((response) => {
						const transactionHash = response.transaction_hash;
						console.log(transactionHash);
						gameInstance.SendMessage(callbackObjectStr, callbackMethodStr, transactionHash);
					}).catch((error) => {
						const errorMessage = error.message;
						gameInstance.SendMessage(callbackObjectStr, callbackMethodStr, errorMessage);
					})
				}
			}
		else if (window.starknet_braavos.isConnected)
		{
			await window.starknet_braavos.enable();
			if (window.starknet_braavos.selectedAddress)
			{
				window.starknet_braavos.account.execute(parsedObject)
				.then((response) => {
					const transactionHash = response.transaction_hash;
					gameInstance.SendMessage(callbackObjectStr, callbackMethodStr, transactionHash);
				}).catch((error) => {
					const errorMessage = error.message;
					gameInstance.SendMessage(callbackObjectStr, callbackMethodStr, errorMessage);
				})	
			}
		}
	},

	CallContract: async function(contractAddress, entrypoint, calldata, callbackObjectName, callbackMethodName)
	{
		const jsStringToWasm = (str) => {
			var bufferSize = lengthBytesUTF8(str) + 1;
			var buffer = _malloc(bufferSize);
			stringToUTF8(str, buffer, bufferSize);
			return buffer;
		}

		const calldataArray = JSON.parse(UTF8ToString(calldata))
		const contractAddressStr = UTF8ToString(contractAddress)
		const entrypointStr = UTF8ToString(entrypoint)
		const callbackObjectStr = UTF8ToString(callbackObjectName)
		const callbackMethodStr = UTF8ToString(callbackMethodName)
		
		await window.starknet.enable();
		if (window.starknet.selectedAddress)
		{
			window.starknet.account.callContract({
				contractAddress: contractAddressStr,
				entrypoint: entrypointStr,
				calldata: calldataArray.array
			}).then((response) => {
				const responseStr = JSON.stringify(response);
				gameInstance.SendMessage(callbackObjectStr, callbackMethodStr, responseStr);
			}).catch((error) => {
				const errorMessage = error.message;
				gameInstance.SendMessage(callbackObjectStr, callbackMethodStr, errorMessage);
			})
		}
	},

	FreeWasmString: function(ptr) {
    _free(ptr);
	},

	RefreshPage: function()
	{
		window.location.reload();
	},

	GetCurrentBlockNumber: async function() {
		try {
			var provider = new window.customStark.RpcProvider({
				nodeUrl: 'https://starknet-sepolia.public.blastapi.io/rpc/v0_6',
				chainId: "0x534e5f5345504f4c4941"
			});

        	var blockNum = await provider.getBlockLatestAccepted('latest');
			console.log(blockNum);
			SendMessage('Main_Canvas', 'ReceiveBlockTimeData',  JSON.stringify(blockNum.block_number));

		} catch (error) {
			console.error("Error in GetCurrentBlockNumber:", error);
			// Handle the error or report it back to your application
		}
	},

	GetTxTransactionData: async function(TxPtr) {
		try {
			var provider = new window.customStark.RpcProvider({
				nodeUrl: 'https://starknet-sepolia.public.blastapi.io/rpc/v0_6',
				chainId: "0x534e5f5345504f4c4941"
			});

			var Tx = UTF8ToString(TxPtr); 
			
			var receipt = await provider.waitForTransaction(Tx);
			console.log("get transaction data");
			console.log(receipt);
			var eventsJson = JSON.stringify(receipt.events);
			
			if (receipt.execution_status === 'SUCCEEDED') {
				SendMessage('PlaceholderEntityManager', 'ReturnFromJsLibTxStatus', eventsJson);
			}
			else{
				SendMessage('PlaceholderEntityManager', 'BadHashCall', receipt.execution_status);
			}

		} catch (error) {
			console.error("Error in GetTxTransactionData:", error);
		}
	},

	GetTransactionReceipt: async function(TxPtr) {
		try {
			var provider = new window.customStark.RpcProvider({
				nodeUrl: 'https://starknet-sepolia.public.blastapi.io/rpc/v0_6',
				chainId: "0x534e5f5345504f4c4941"
			});

			var Tx = UTF8ToString(TxPtr); 

			var receipt = await provider.getTransactionReceipt(Tx);
			var eventsJson = JSON.stringify(receipt.events);
			console.log("get transaction receipt");
			console.log(receipt);
			SendMessage('PlaceholderEntityManager', 'ReceiveJson', eventsJson);

		} catch (error) {
			console.error("Error in GetTransactionReceipt:", error);
		}
	},

	OpenURL: function(urlPtr) {
		var url = UTF8ToString(urlPtr); 
		window.open(url, '_blank').focus();
	},

	JSBigIntToDec: function(hexPtr) {
		var hex = UTF8ToString(hexPtr); 
		const num = parseInt(hex, 16);
        const result = num / Math.pow(10, 18);
    
    	return result.toFixed(4);
	},

	StarknetNoAccountCall: async function(contractAddress, entrypoint, calldata, callbackObjectName, callbackMethodName){

		const provider = new window.customStark.RpcProvider({
			nodeUrl: 'https://starknet-sepolia.public.blastapi.io/rpc/v0_6',
			chainId: "0x534e5f5345504f4c4941"
		});

		const calldataArray = JSON.parse(UTF8ToString(calldata))
		const contractAddressStr = UTF8ToString(contractAddress)
		const entrypointStr = UTF8ToString(entrypoint)
		const callbackObjectStr = UTF8ToString(callbackObjectName)
		const callbackMethodStr = UTF8ToString(callbackMethodName)

		provider.callContract({
				contractAddress: contractAddressStr,
				entrypoint: entrypointStr,
				calldata: calldataArray.array
			}).then((response) => {
				const responseStr = JSON.stringify(response);
				console.log(responseStr);
				gameInstance.SendMessage(callbackObjectStr, callbackMethodStr, responseStr);
			}).catch((error) => {
				const errorMessage = error.message;
				gameInstance.SendMessage(callbackObjectStr, callbackMethodStr, errorMessage);
			})
	},
});