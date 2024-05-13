using Dojo.Starknet;
using System;
using System.Collections.Generic;
using TMPro;
using UnityEngine;

public class CreateLobbyBehavior : Menu
{
    public MenuManager menuManager;
    public Menu _lobbyPhase;
    //se the data for the blobert and have an input field take waya the button

    public BlobertCardData blobertCardData;
    public TMP_InputField inputFieldOtherPlayer;

    public TMP_Text idText;
    public TMP_Text addressText;

    [SerializeField] private GameObject _sendRequestGameobject;

    [SerializeField] private GameObject _cancelRequestGameobject;
    [SerializeField] private TMP_Text _cancelRequestText;

    private void Start()
    {
        UiReferencesStatic.createLobbyBehavior = this;
    }

    private void OnEnable()
    {
        UiReferencesStatic.createLobbyBehavior = this;

        var blobert = DojoEntitiesStorage.userChoosenBlobert;

        addressText.text = DojoEntitiesStorage.currentAccount.Address.Hex();

        blobertCardData.SetBlobertData(blobert.dojoId);

        CheckForActiveRequest();
    }

    private DateTime lastInteractionWithContract = DateTime.MinValue;

    /*
    public async void CreateLobby()
    {
        double secondsSinceLastCommit = (DateTime.Now - lastInteractionWithContract).TotalSeconds;

        if (secondsSinceLastCommit < 2)
        {
            Debug.Log("You are creating a lobby too fast");
            return;
        }
        else
        {
            lastInteractionWithContract = DateTime.Now;
        }

        // if input field is empty return
        if (string.IsNullOrEmpty(inputFieldOtherPlayer.text))
        {
            return;
        }

        var endpoint = new EndpointDojoCallStruct
        {
             
            addressOfSystem = DojoEntitiesStorage.worldManagerData.knockoutContractAddress,
            functionName = ,
        };

        Debug.Log("Creating new game");
        Debug.Log("Player A: " + DojoEntitiesStorage.currentAccount.Address.Hex());
        Debug.Log("Player B: " + new FieldElement(inputFieldOtherPlayer.text).Hex());
        Debug.Log("Blobert A: " + DojoEntitiesStorage.userBlobertData.blobertId.Hex());

        //for loop to check all the blobs and if the other player has the blobert

        var blobertFound = false;
        var blobertId = new FieldElement("0");

        foreach (var blobert in DojoEntitiesStorage.allBlobertDict)
        {
            if (blobert.Value.owner.Hex() == inputFieldOtherPlayer.text)
            {
                blobertId = blobert.Value.blobertId;
                blobertFound = true;
            }
        }

        if (!blobertFound)
        {
            Debug.Log("Blobert not found");
            return;
        }


        var dataStruct = new DojoContractCaller.CreateNewGameStruct
        {
            player_a = DojoEntitiesStorage.currentAccount.Address,
            player_b = new FieldElement(inputFieldOtherPlayer.text),
            blobert_aID = DojoEntitiesStorage.userBlobertData.blobertId,
            blobert_bID = blobertId,
        };

        var transaction = await DojoContractCaller.CreateNewGame(dataStruct, endpoint);
    }
    */

    public async void SendChallenge()
    {
        Debug.Log("called the send challenge function");

        var endpoint = new DojoContractCommunication.EndpointDojoCallStruct
        {
            addressOfSystem = DojoEntitiesStorage.worldManagerData.challengeblobertContractAddress,
            functionName = ChallengeActionsContract.FunctionNames.SendInvite.EnumToString(),
        };

        var structData = new ChallengeActionsContract.SendInviteStruct
        {
            endpointData = endpoint,
            receiver = new FieldElement(inputFieldOtherPlayer.text),
            blobertId = DojoEntitiesStorage.userChoosenBlobert.dojoId,
        };

        var calls = new List<object>();
        calls.Add(structData);

        var transaction = await DojoContractCommunication.InvokeContract(calls, objectName: gameObject.name, functionName: "OnChainTransactionCallbackFunctionSC", account: DojoEntitiesStorage.currentAccount);

        CheckForActiveRequest();
    }

    public void OnChainTransactionCallbackFunctionSC(string transactionHash)
    {
        Debug.Log("Transaction hash callback: " + transactionHash);
    }

    public async void CancelSentInvite()
    {
        var endpoint = new DojoContractCommunication.EndpointDojoCallStruct
        {
            addressOfSystem = DojoEntitiesStorage.worldManagerData.challengeblobertContractAddress,
            functionName = ChallengeActionsContract.FunctionNames.RescindInvite.EnumToString(),
        };

        var dataStruct = new ChallengeActionsContract.RescindInviteStruct
        {
            endpointData = endpoint,
            challengeId = DojoEntitiesStorage.selectedChallengeID,
        };

        var calls = new List<object>();
        calls.Add(dataStruct);

        //var transaction = await ChallengeActionsContract.RescindInviteCall(dataStruct, endpoint);
        var transaction = await DojoContractCommunication.InvokeContract(calls, objectName: gameObject.name, functionName: "OnChainTransactionCallbackFunctionCSI", account: DojoEntitiesStorage.currentAccount);

        CheckForActiveRequest();
    }

    public void OnChainTransactionCallbackFunctionCSI(string transactionHash)
    {
        Debug.Log("Transaction hash callback: " + transactionHash);
        //if (transactionHash == "User abort" || transactionHash == "Execute failed")
        //{
        //    UiEntitiesReferenceManager.notificationManager.CreateNotification("Selling Outpost was aborted", null, 5f);
        //    return;
        //}
    }

    public async void StartGame()
    {
        var endpoint = new DojoContractCommunication.EndpointDojoCallStruct
        {
             
            addressOfSystem = DojoEntitiesStorage.worldManagerData.challengeblobertContractAddress,
            functionName = ChallengeActionsContract.FunctionNames.AcceptResponse.EnumToString()
        };

        var dataStruct = new ChallengeActionsContract.AcceptResponseStruct
        {
            endpointData = endpoint,
            challengeId = new FieldElement(inputFieldOtherPlayer.text),
        };

        var calls = new List<object>();
        calls.Add(dataStruct);

        var transaction = await DojoContractCommunication.InvokeContract(calls, objectName: gameObject.name, functionName: "OnChainTransactionCallbackFunctionSG", account: DojoEntitiesStorage.currentAccount);

        //var transaction = ChallengeActionsContract.AcceptResponseCall(dataStruct, endpoint);
    }

    public void OnChainTransactionCallbackFunctionSG(string transactionHash)
    {
        Debug.Log("Transaction hash callback: " + transactionHash);
        //if (transactionHash == "User abort" || transactionHash == "Execute failed")
        //{
        //    UiEntitiesReferenceManager.notificationManager.CreateNotification("Selling Outpost was aborted", null, 5f);
        //    return;
        //}
    }

    void Update()
    {
        //if (DojoEntitiesStorage.healthsCurrentGame != null && DojoEntitiesStorage.knockoutCurrentGame != null)
        //{
        //    Debug.Log("we move to the next phase");
        //    menuManager.OpenMenu(battlePhase);
        //}

        //for (int i = DojoEntitiesStorage.knockoutsList.Count - 1; i >= 0; i--)
        //{
        //    var currentKnockout = DojoEntitiesStorage.knockoutsList[i];

        //    if (DojoEntitiesStorage.knockoutCurrentGame != null && DojoEntitiesStorage.healthsCurrentGame != null)
        //    {
        //        break;
        //    }

        //    if (BlobertUtils.Address0sFix(currentKnockout.playerA.Hex()) == DojoEntitiesStorage.currentAccount.Address.Hex() || BlobertUtils.Address0sFix(currentKnockout.playerB.Hex()) == DojoEntitiesStorage.currentAccount.Address.Hex())
        //    {
        //        // the knowouct round made contains the player
        //        // find the healths round by doing another loop ffs

        //        for (int x = 0; x < DojoEntitiesStorage.healthsList.Count; x++)
        //        {
        //            //sanity check

        //            var health = DojoEntitiesStorage.healthsList[x];
        //            if (currentKnockout.combatId.Hex() == health.combatId.Hex())
        //            {
        //                // this is the same hex as the knowcout

        //                if (health.a > 0 && health.b > 0)
        //                {
        //                    DojoEntitiesStorage.knockoutCurrentGame = currentKnockout;
        //                    DojoEntitiesStorage.healthsCurrentGame = health;
        //                    DojoEntitiesStorage.currentRoundId = currentKnockout.combatId;

        //                    break;
        //                }
        //                else
        //                {
        //                    continue;
        //                }
        //            }
        //        }

        //    }
        //    else
        //    {
        //        //delete from the list
        //        DojoEntitiesStorage.knockoutsList.RemoveAt(i);
        //        continue;
        //    }

        //}

        // i need to check if there is a request going right now 


        if (DojoEntitiesStorage.challengeInvite != null && DojoEntitiesStorage.challengeResponse != null)
        {
           Debug.Log("we move to the next phase");
            menuManager.OpenMenu(_lobbyPhase);
        }


        if (Input.GetKeyDown(KeyCode.H))
        {
            if (DojoEntitiesStorage.challengeInvite != null)
            {
                Debug.Log("challenge invite is not null");
            }
            else
            {
                Debug.Log("challenge invite is null");
            }

            if (DojoEntitiesStorage.challengeResponse != null)
            {
                Debug.Log("challenge response is not null");
            }
            else
            {
                Debug.Log("challenge response is null");
            }
        }
    }

    public void CheckForActiveRequest()
    {
        if (DojoEntitiesStorage.challengeInvite != null)
        {
            _sendRequestGameobject.SetActive(false);
            _cancelRequestGameobject.SetActive(true);
            _cancelRequestText.text = $"Cancel Request to {DojoEntitiesStorage.challengeInvite.dojoReceiver.Hex().Substring(0,6)}";
        }
        else
        {
            _sendRequestGameobject.SetActive(true);
            _cancelRequestGameobject.SetActive(false);
        }
    }
}
