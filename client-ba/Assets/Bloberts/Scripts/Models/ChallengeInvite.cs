using Dojo;
using Dojo.Starknet;
using Dojo.Torii;

public class ChallengeInvite : ModelInstance
{
    #region GeneratedRegion 

    [ModelField("challenge_id")]
    public FieldElement dojoChallengeId;
    


    [ModelField("sender")]
    public FieldElement dojoSender;
    


    [ModelField("receiver")]
    public FieldElement dojoReceiver;
    


    [ModelField("blobert_id")]
    public FieldElement dojoBlobertId;
    


    [ModelField("open")]
    public bool dojoOpen;
    

    #endregion 

    // Start is called before the first frame update
    void Start()
    {
        DojoEntitiesStorage.challengeInvitesDict.Add(dojoChallengeId.Hex(), this);

        if (dojoSender.Hex() == DojoEntitiesStorage.currentAccount.Address.Hex() && dojoOpen)
        {
            DojoEntitiesStorage.challengeInvite = this;
            DojoEntitiesStorage.selectedChallengeID = dojoChallengeId;

            if (UiReferencesStatic.createLobbyBehavior != null)
            {
                UiReferencesStatic.createLobbyBehavior.CheckForActiveRequest();
            }
        }
        else if (dojoReceiver.Hex() == DojoEntitiesStorage.currentAccount.Address.Hex() && dojoOpen)
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

        if (!dojoOpen && DojoEntitiesStorage.userReceivedChallengeInvites.Contains(this))
        {
            DojoEntitiesStorage.userReceivedChallengeInvites.Remove(this);

            if (UiReferencesStatic.searchLobbyPageBehaviour != null)
            {
                UiReferencesStatic.searchLobbyPageBehaviour.RefreshInvitations();
            }
        }
        if (!dojoOpen && DojoEntitiesStorage.selectedChallengeID != null)
        {
            if (dojoChallengeId.Hex() == DojoEntitiesStorage.selectedChallengeID.Hex())
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
