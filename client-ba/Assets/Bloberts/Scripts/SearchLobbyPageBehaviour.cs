using Dojo.Starknet;
using System.Collections.Generic;
using UnityEngine;

public class SearchLobbyPageBehaviour : Menu
{
    [SerializeField] private GameObject _invitationToLobbyPrefab;
    [SerializeField] private Transform _invitationToLobbyParent;

    [SerializeField] private MenuManager _menuManager;
    [SerializeField] private Menu _lobbyMenu;

    private void Start()
    {
        UiReferencesStatic.searchLobbyPageBehaviour = this;
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Y))
        {
            _menuManager.OpenMenu(_lobbyMenu);
        }

        if (DojoEntitiesStorage.challengeResponse != null )
        {
            _menuManager.OpenMenu(_lobbyMenu);
        }
    }

    private void OnEnable()
    {
        RefreshInvitations();
    }

    public void RefreshInvitations()
    {
        Debug.Log("refreshing invitations");

        //kill all the children
        foreach (Transform child in _invitationToLobbyParent)
        {
            Destroy(child.gameObject);
        }

        foreach (var invite in DojoEntitiesStorage.userReceivedChallengeInvites)
        {
            if (invite.dojoOpen == false)
            {
                continue;
            }
            var invitationObject = Instantiate(_invitationToLobbyPrefab);
            invitationObject.transform.localScale = Vector3.one;
            
            invitationObject.transform.SetParent(_invitationToLobbyParent);

            invitationObject.GetComponent<InvitationToLobby>().Initialize(invite.dojoChallengeId, invite.dojoSender ,invite.dojoBlobertId , this);
        }
    }

    public async void SayNoToInvite(FieldElement challengeID)
    {
        var endpoint = new DojoContractCommunication.EndpointDojoCallStruct
        {
            addressOfSystem = DojoEntitiesStorage.worldManagerData.challengeblobertContractAddress,
            functionName = ChallengeActionsContract.FunctionNames.RejectInvite.EnumToString(),
        };

        var dataStruct = new ChallengeActionsContract.RejectInviteStruct
        {
            endpointData = endpoint,
            challengeId = challengeID,
        };

        var calls = new List<object>();
        calls.Add(dataStruct);

        var transaction = await DojoContractCommunication.InvokeContract(calls, gameObject.name, "OnChainTransactionCallbackFunctionSN", account: DojoEntitiesStorage.currentAccount);
    }

    public async void SayYesToInvite(FieldElement challengeID)
    {
        var endpoint = new DojoContractCommunication.EndpointDojoCallStruct
        {
            addressOfSystem = DojoEntitiesStorage.worldManagerData.challengeblobertContractAddress,
            functionName = ChallengeActionsContract.FunctionNames.RespondInvite.EnumToString(),
        };

        var dataStruct = new ChallengeActionsContract.RespondInviteStruct
        {
            endpointData = endpoint,
            challengeId = challengeID,
            blobertId = DojoEntitiesStorage.userChoosenBlobert.dojoId,
        };

        DojoEntitiesStorage.selectedChallengeID = challengeID;

        var calls = new List<object>();
        calls.Add(dataStruct);

        var transaction = await DojoContractCommunication.InvokeContract(calls, gameObject.name, "OnChainTransactionCallbackFunctionSY", account: DojoEntitiesStorage.currentAccount);
    }
}
