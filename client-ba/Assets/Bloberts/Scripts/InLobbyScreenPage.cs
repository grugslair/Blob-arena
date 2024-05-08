using DojoContractCommunication;
using System.Collections;
using System.Net;
using TMPro;
using UnityEngine;

public class InLobbyScreenPage : Menu
{
    [SerializeField] private GameObject _adminButtons;  
    [SerializeField] private GameObject _guestButtons;

    [SerializeField] private BlobertCardData _leftBlobertCardData;   //self
    [SerializeField] private TMP_Text _leftOwnerText;   
    [SerializeField] private TMP_Text _leftBlobIdText;

    [SerializeField] private BlobertCardData _rightBlobertCardData;   // enemy
    [SerializeField] private TMP_Text _rightOwnerText;
    [SerializeField] private TMP_Text _rightBlobIdText;

    [SerializeField] private MenuManager _menuManager;

    [SerializeField] private Menu _battlePage;
    [SerializeField] private Menu _searchLobbyPage;
    [SerializeField] private Menu _createLobbyPage;

    private void Start()
    {
        UiReferencesStatic.lobbyBehavior = this;
    }

    private void OnEnable()
    {
        if (DojoEntitiesStorage.challengeInvite == null)
        {
            DojoEntitiesStorage.challengeInvite = DojoEntitiesStorage.challengeInvitesDict[DojoEntitiesStorage.challengeResponse.challengeId.Hex()];
        }

        if (DojoEntitiesStorage.challengeInvite.sender.Hex() == DojoEntitiesStorage.currentAccount.Address.Hex())
        {
            _adminButtons.SetActive(true);
            _guestButtons.SetActive(false);

            _leftBlobertCardData.SetBlobertData(DojoEntitiesStorage.challengeInvite.blobertId);
            _leftBlobIdText.text = $"ID: {BlobertUtils.HexToBigInt(DojoEntitiesStorage.challengeInvite.blobertId.Hex())}";
            _leftOwnerText.text = $"{DojoEntitiesStorage.currentAccount.Address.Hex().Substring(0,8)}";

            _rightBlobertCardData.SetBlobertData(DojoEntitiesStorage.challengeResponse.blobertId);
            _rightBlobIdText.text = $"ID: {BlobertUtils.HexToBigInt(DojoEntitiesStorage.challengeResponse.blobertId.Hex())}";
            _rightOwnerText.text = $"{DojoEntitiesStorage.challengeInvite.receiver.Hex().Substring(0, 8)}";
        }
        else
        {
            _adminButtons.SetActive(false);
            _guestButtons.SetActive(true);

            _leftBlobertCardData.SetBlobertData(DojoEntitiesStorage.challengeResponse.blobertId);
            _leftBlobIdText.text = $"ID: {BlobertUtils.HexToBigInt(DojoEntitiesStorage.challengeResponse.blobertId.Hex())}";
            _leftOwnerText.text = $"{DojoEntitiesStorage.currentAccount.Address.Hex().Substring(0, 8)}";

            _rightBlobertCardData.SetBlobertData(DojoEntitiesStorage.challengeInvite.blobertId);
            _rightBlobIdText.text = $"ID: {BlobertUtils.HexToBigInt(DojoEntitiesStorage.challengeInvite.blobertId.Hex())}";
            _rightOwnerText.text = $"{DojoEntitiesStorage.challengeInvite.sender.Hex().Substring(0, 8)}";
        }
    }

 
    public void CurrentLobbyStateCheck()
    {
        if (DojoEntitiesStorage.challengeInvite != null)
        {
            if (DojoEntitiesStorage.challengeResponse.open == false)
            {
                if (DojoEntitiesStorage.challengeInvite.sender.Hex() == DojoEntitiesStorage.currentAccount.Address.Hex())
                {
                    _menuManager.OpenMenu(_createLobbyPage);
                    DojoEntitiesStorage.challengeResponse = null;
                }
                else
                {
                    _menuManager.OpenMenu(_searchLobbyPage);
                    DojoEntitiesStorage.selectedChallengeID = null;
                    DojoEntitiesStorage.challengeResponse = null;
                    DojoEntitiesStorage.challengeInvite = null;
                }
            }
        }
    }

    public void StartGame()
    {
        var endpoint = new EndpointDojoCallStruct
        {
            account = DojoEntitiesStorage.currentAccount,
            addressOfSystem = DojoEntitiesStorage.worldManagerData.challengeblobertContractAddress,
            functionName = ChallengeActionsContract.FunctionNames.AcceptResponse.EnumToString(),
        };

        var dataStruct = new ChallengeActionsContract.AcceptResponseStruct
        {
            challengeId = DojoEntitiesStorage.challengeInvite.challengeId,
        };

        var transaction = ChallengeActionsContract.AcceptResponseCall(dataStruct, endpoint);
    }

    public void AdminLeaveLobby()
    {
        var endpoint = new EndpointDojoCallStruct
        {
            account = DojoEntitiesStorage.currentAccount,
            addressOfSystem = DojoEntitiesStorage.worldManagerData.challengeblobertContractAddress,
            functionName = ChallengeActionsContract.FunctionNames.RejectResponse.EnumToString(),
        };

        var dataStruct = new ChallengeActionsContract.RejectResponseStruct
        {
            challengeId = DojoEntitiesStorage.challengeInvite.challengeId,
        };

        var transaction = ChallengeActionsContract.RejectResponseCall(dataStruct, endpoint);
    }

    public void UserCloseLobby()
    {
        var endpoint = new EndpointDojoCallStruct
        {
            account = DojoEntitiesStorage.currentAccount,
            addressOfSystem = DojoEntitiesStorage.worldManagerData.challengeblobertContractAddress,
            functionName = ChallengeActionsContract.FunctionNames.RescindResponse.EnumToString(),
        };

        var dataStruct = new ChallengeActionsContract.RescindResponseStruct
        {
            challengeId = DojoEntitiesStorage.challengeInvite.challengeId,
        };

        var transaction = ChallengeActionsContract.RescindResponseCall(dataStruct, endpoint);
    }

    private void Update()
    {
        if (DojoEntitiesStorage.knockoutCurrentGame != null)
        {
            StartCoroutine(DelayedExecution());
        }
    }

    private IEnumerator DelayedExecution()
    {
        yield return new WaitForSeconds(1);

        DojoEntitiesStorage.healthsCurrentGame = DojoEntitiesStorage.healthsDict[DojoEntitiesStorage.knockoutCurrentGame.combatId.Hex()];
        DojoEntitiesStorage.currentCombatId = DojoEntitiesStorage.knockoutCurrentGame.combatId;

        _menuManager.OpenMenu(_battlePage);
    }
}
