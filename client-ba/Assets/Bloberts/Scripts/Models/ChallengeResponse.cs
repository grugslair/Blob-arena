using Dojo;
using Dojo.Starknet;
using Dojo.Torii;

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


        

    }
}
