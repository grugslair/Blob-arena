using Dojo;
using Dojo.Starknet;
using Dojo.Torii;
using UnityEngine;

public class ChallengeResponse : ModelInstance
{
    [ModelField("challenge_id")]
    public FieldElement challengeId;
    [ModelField("blobert_id")]
    public FieldElement blobertId;
    [ModelField("open")]
    public bool open;
    [ModelField("combat_id")]
    public FieldElement combatId;


    private bool _previousOpen = true;
    // Start is called before the first frame update
    void Start()
    {
        if (DojoEntitiesStorage.selectedChallengeID != null)
        {
            if (challengeId.Hex() == DojoEntitiesStorage.selectedChallengeID.Hex() && open)
            {
                DojoEntitiesStorage.challengeResponse = this;
            }
        }
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);

        if (open != _previousOpen)
        {
            _previousOpen = open;

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
