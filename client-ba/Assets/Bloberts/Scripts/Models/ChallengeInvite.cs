using Dojo;
using Dojo.Starknet;
using Dojo.Torii;
using UnityEngine;

public class ChallengeInvite : ModelInstance
{
    [ModelField("challenge_id")]
    public FieldElement challengeId;
    [ModelField("sender")]
    public FieldElement sender;
    [ModelField("receiver")]
    public FieldElement receiver;
    [ModelField("blobert_id")]
    public FieldElement blobertId;
    [ModelField("open")]
    public bool open;

    // Start is called before the first frame update
    void Start()
    {
        if (sender.Hex() == DojoEntitiesStorage.currentAccount.Address.Hex() && open)
        {
            DojoEntitiesStorage.challengeInvite = this;
            DojoEntitiesStorage.selectedChallengeID = challengeId;

            if (UiReferencesStatic.createLobbyBehavior != null)
            {
                UiReferencesStatic.createLobbyBehavior.CheckForActiveRequest();
            }
        }
        else if (receiver.Hex() == DojoEntitiesStorage.currentAccount.Address.Hex() && open)
        {
            DojoEntitiesStorage.userReceivedChallengeInvites.Add(this);
        }

        DojoEntitiesStorage.challengeInvitesDict.Add(challengeId.Hex(), this);
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);

        if (!open && DojoEntitiesStorage.userReceivedChallengeInvites.Contains(this))
        {
            if (UiReferencesStatic.searchLobbyPageBehaviour != null)
            {
                UiReferencesStatic.searchLobbyPageBehaviour.RefreshInvitations();
            }

            DojoEntitiesStorage.userReceivedChallengeInvites.Remove(this);
        }
        else if (!open && DojoEntitiesStorage.selectedChallengeID.Hex() == challengeId.Hex())
        {
            DojoEntitiesStorage.challengeInvite = null;
            DojoEntitiesStorage.selectedChallengeID = null;

            if (UiReferencesStatic.createLobbyBehavior != null)
            {
                UiReferencesStatic.createLobbyBehavior.CheckForActiveRequest();
            }
            else
            {
                Debug.Log("search lobby page is null");
            }
        }
    }
}
