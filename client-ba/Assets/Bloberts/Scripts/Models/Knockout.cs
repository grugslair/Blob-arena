using Dojo;
using Dojo.Starknet;
using Dojo.Torii;

public class Knockout : ModelInstance
{
    [ModelField("combat_id")]
    public FieldElement combatId;

    [ModelField("player_a")]
    public FieldElement playerA;
    [ModelField("player_b")]
    public FieldElement playerB;

    [ModelField("blobert_a")]
    public FieldElement blobertA;
    [ModelField("blobert_b")]
    public FieldElement blobertB;

    private void Start()
    {
        DojoEntitiesStorage.knockoutDict.Add(combatId.Hex(), this);

        if (DojoEntitiesStorage.challengeInvite != null)
        {
            var invStruct = DojoEntitiesStorage.challengeInvite;

            if (playerA.Hex() == invStruct.sender.Hex()  ||   playerA.Hex() == invStruct.receiver.Hex())
            {
                
            }
            else
            {
                return;
            }

            if (playerB.Hex() == invStruct.sender.Hex() || playerB.Hex() == invStruct.receiver.Hex())
            {
                DojoEntitiesStorage.knockoutCurrentGame = this;
            }
            else
            {
                return;
            }
        }


        //if (DojoEntitiesStorage.currentCombatId != null)
        //{
        //    if (DojoEntitiesStorage.currentCombatId.Hex() == this.combatId.Hex())
        //    {
        //        DojoEntitiesStorage.knockoutCurrentGame = this;
        //    }
        //}
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);
    }
}
