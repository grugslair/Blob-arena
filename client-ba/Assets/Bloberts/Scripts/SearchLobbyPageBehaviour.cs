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

    private void OnEnable()
    {
        RefreshInvitations();
    }

    public void RefreshInvitations()
    {
        //kill all the children
        foreach (Transform child in _invitationToLobbyParent)
        {
            Destroy(child.gameObject);
        }

        foreach (var invite in DojoEntitiesStorage.userReceivedChallengeInvites)
        {
            var invitationObject = Instantiate(_invitationToLobbyPrefab);
            invitationObject.transform.SetParent(_invitationToLobbyParent);

            invitationObject.GetComponent<InvitationToLobby>().Initialize(invite.challengeId, invite.sender ,invite.blobertId , this);
        }
    }

    public void SayNoToInvite(FieldElement challengeID)
    {
        Debug.Log("called the say no to inv function");

        var endpoint = new EndpointDojoCallStruct
        {
            account = DojoEntitiesStorage.currentAccount,
            addressOfSystem = DojoEntitiesStorage.worldManagerData.challengeblobertContractAddress,
            functionName = ChallengeContract.FunctionNames.CloseResponse.EnumToString(),
        };

        var dataStruct = new ChallengeContract.RejectInviteStruct
        {
            challengeId = challengeID,
        };

        var transaction = ChallengeContract.RejectInvite(dataStruct, endpoint);
    }

    public void SayYesToInvite(FieldElement challengeID)
    {
        Debug.Log("called the say yes to inv function");

        var endpoint = new EndpointDojoCallStruct
        {
            account = DojoEntitiesStorage.currentAccount,
            addressOfSystem = DojoEntitiesStorage.worldManagerData.challengeblobertContractAddress,
            functionName = ChallengeContract.FunctionNames.RespondInvite.EnumToString(),
        };

        var dataStruct = new ChallengeContract.RespondInviteStruct
        {
            challengeId = challengeID,
            blobertId = DojoEntitiesStorage.userChoosenBlobert.dojoBlobertId,
        };

        DojoEntitiesStorage.selectedChallengeID = challengeID;

        var transaction = ChallengeContract.RespondInvite(dataStruct, endpoint);
    }

}
