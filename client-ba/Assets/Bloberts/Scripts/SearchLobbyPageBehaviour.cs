using Dojo.Starknet;
using DojoContractCommunication;
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
            if (invite.open == false)
            {
                continue;
            }
            var invitationObject = Instantiate(_invitationToLobbyPrefab);
            invitationObject.transform.localScale = Vector3.one;
            
            invitationObject.transform.SetParent(_invitationToLobbyParent);

            invitationObject.GetComponent<InvitationToLobby>().Initialize(invite.challengeId, invite.sender ,invite.blobertId , this);
        }
    }

    public async void SayNoToInvite(FieldElement challengeID)
    {
        var endpoint = new EndpointDojoCallStruct
        {
            account = DojoEntitiesStorage.currentAccount,
            addressOfSystem = DojoEntitiesStorage.worldManagerData.challengeblobertContractAddress,
            functionName = ChallengeActionsContract.FunctionNames.RejectInvite.EnumToString(),
        };

        var dataStruct = new ChallengeActionsContract.RejectInviteStruct
        {
            challengeId = challengeID,
        };

        var transaction = await ChallengeActionsContract.RejectInviteCall(dataStruct, endpoint);
    }

    public async void SayYesToInvite(FieldElement challengeID)
    {
        var endpoint = new EndpointDojoCallStruct
        {
            account = DojoEntitiesStorage.currentAccount,
            addressOfSystem = DojoEntitiesStorage.worldManagerData.challengeblobertContractAddress,
            functionName = ChallengeActionsContract.FunctionNames.RespondInvite.EnumToString(),
        };

        var dataStruct = new ChallengeActionsContract.RespondInviteStruct
        {
            challengeId = challengeID,
            blobertId = DojoEntitiesStorage.userChoosenBlobert.dojoBlobertId,
        };

        DojoEntitiesStorage.selectedChallengeID = challengeID;

        var transaction = await ChallengeActionsContract.RespondInviteCall(dataStruct, endpoint);

        if (transaction != null)
        {
            Debug.Log("not null and should be opening lobby");
            DojoEntitiesStorage.challengeInvite = DojoEntitiesStorage.challengeInvitesDict[challengeID.Hex()];
        }
    }
}
