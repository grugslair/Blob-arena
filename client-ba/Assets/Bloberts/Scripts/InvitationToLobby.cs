using Dojo.Starknet;
using TMPro;
using UnityEngine;

public class InvitationToLobby : MonoBehaviour
{
    private FieldElement _challengeId;
    private SearchLobbyPageBehaviour _searchLobbyPageBehaviour;
    [SerializeField] TMP_Text _lobbyDataText;

    public void Initialize(FieldElement challengeId, FieldElement owner, FieldElement blobId, SearchLobbyPageBehaviour page)
    {
        _challengeId = challengeId;
        _searchLobbyPageBehaviour = page;
        //get the rect transfomr and set the scale to 1
        gameObject.GetComponent<RectTransform>().localScale = Vector3.one;

        _lobbyDataText.text = $"{owner.Hex().Substring(0,7)}  ID: {BlobertUtils.HexToBigInt(blobId.Hex())}";
    }

    public void Accept()
    {
        _searchLobbyPageBehaviour.SayYesToInvite(_challengeId);
    }

    public void Decline()
    {
        Debug.Log("called to decline");
        _searchLobbyPageBehaviour.SayNoToInvite(_challengeId);
    }
    
}
