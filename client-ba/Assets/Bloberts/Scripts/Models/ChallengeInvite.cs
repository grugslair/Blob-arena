using Dojo;
using Dojo.Starknet;
using Dojo.Torii;

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
        DojoEntitiesStorage.challengeInvitesDict.Add(challengeId.Hex(), this);

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

            if (UiReferencesStatic.searchLobbyPageBehaviour != null)
            {
                UiReferencesStatic.searchLobbyPageBehaviour.RefreshInvitations();
            }
        }
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);

        if (!open && DojoEntitiesStorage.userReceivedChallengeInvites.Contains(this))
        {
            DojoEntitiesStorage.userReceivedChallengeInvites.Remove(this);

            if (UiReferencesStatic.searchLobbyPageBehaviour != null)
            {
                UiReferencesStatic.searchLobbyPageBehaviour.RefreshInvitations();
            }
        }
        if (!open && DojoEntitiesStorage.selectedChallengeID != null)
        {
            if (challengeId.Hex() == DojoEntitiesStorage.selectedChallengeID.Hex())
            {
                DojoEntitiesStorage.challengeInvite = null;
                DojoEntitiesStorage.selectedChallengeID = null;

                if (UiReferencesStatic.createLobbyBehavior != null)
                {
                    UiReferencesStatic.createLobbyBehavior.CheckForActiveRequest();
                }
            }
        }
    }
}
