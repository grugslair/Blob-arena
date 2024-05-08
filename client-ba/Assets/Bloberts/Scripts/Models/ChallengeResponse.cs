using Dojo;
using Dojo.Starknet;
using Dojo.Torii;
using UnityEngine;

public class ChallengeResponse : ModelInstance
{
    #region GeneratedRegion 

    [ModelField("challenge_id")]
    public FieldElement dojoChallengeId;
    


    [ModelField("blobert_id")]
    public FieldElement dojoBlobertId;
    


    [ModelField("open")]
    public bool dojoOpen;
    


    [ModelField("combat_id")]
    public FieldElement dojoCombatId;
    

    #endregion  

    private bool _previousOpen = true;
    // Start is called before the first frame update
    void Start()
    {
        if (DojoEntitiesStorage.selectedChallengeID != null)
        {
            if (dojoChallengeId.Hex() == DojoEntitiesStorage.selectedChallengeID.Hex() && dojoOpen)
            {
                DojoEntitiesStorage.challengeResponse = this;
            }
        }
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);

        if (dojoOpen != _previousOpen)
        {
            _previousOpen = dojoOpen;

            if (DojoEntitiesStorage.challengeResponse == null) 
            {
                DojoEntitiesStorage.challengeResponse = this;
            }
        }


        if (DojoEntitiesStorage.challengeResponse == this)
        {
            UiReferencesStatic.lobbyBehavior.CurrentLobbyStateCheck();
        }
    }
}
