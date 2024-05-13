using Dojo.Starknet;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Numerics;
using UnityEngine;
using Utils;
using static JSInteropManager;

public class WalletConnect : MonoBehaviour
{
    public static string playerAddress;

    private IEnumerator ConnectWalletAsync(Action connectWalletFunction, bool argent)
    {
        // Call the JavaScript method to connect the wallet
        connectWalletFunction();

        // Wait for the connection to be established
        yield return new WaitUntil(() => JSInteropManager.IsConnected());

        playerAddress = JSInteropManager.GetAccount();
        PlayerPrefs.SetString("playerAddress", playerAddress);
        Debug.Log("Connected to wallet: " + playerAddress);
        DojoEntitiesStorage.currentAccount = new Account(null, null, new FieldElement(playerAddress));
        DojoContractCommunication.selectedWalletType = DojoContractCommunication.WalletType.ARGENT_X;
    }

    public void OnButtonConnectWalletArgentX()
    {
        StartCoroutine(ConnectWalletAsync(JSInteropManager.ConnectWalletArgentX, true));
    }

    public void OnButtonConnectWalletBraavos()
    {
        StartCoroutine(ConnectWalletAsync(JSInteropManager.ConnectWalletBraavos, false));
    }

    // Start is called before the first frame update
    void Start()
    {
        bool available = JSInteropManager.IsWalletAvailable();
        if (!available)
        {
            JSInteropManager.AskToInstallWallet();
        }
    }

    public struct TestStruct{
        public DojoContractCommunication.EndpointDojoCallStruct endpointData;
        public FieldElement addressContract;
        public BigInteger amount;
    }

    public async void Transfer()
    {
        var arr = new string[3] { "0x00d8f5468626409c9af775c7994f4b4d1e7f17edbecd82ad548d3632b8773538", "10000000000", "0" };

        //list of objects
        var listsOfActions = new List<object>();

        var newStruct = new TestStruct
        {
            addressContract = new FieldElement("0x04718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d"),
            amount = 10000000000,
            endpointData = new DojoContractCommunication.EndpointDojoCallStruct
            {
                addressOfSystem = "0x04718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d",
                functionName = "transfer"
            }
        };

        listsOfActions.Add(newStruct);
        listsOfActions.Add(newStruct);
        listsOfActions.Add(newStruct);
        listsOfActions.Add(newStruct);

        //DojoContractCommunication.selectedWalletType = DojoContractCommunication.WalletType.BRAAVOS;

        var transaction = await DojoContractCommunication.InvokeContract(listsOfActions, objectName: gameObject.name, functionName: "Callback", account: DojoEntitiesStorage.currentAccount);
    }

    public void Callback(string result)
    {
        Debug.Log("Callback: " + result);
    }
}
