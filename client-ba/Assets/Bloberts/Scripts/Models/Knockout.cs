using Dojo;
using Dojo.Starknet;
using Dojo.Torii;

public class Knockout : ModelInstance
{
    #region GeneratedRegion 

    [ModelField("combat_id")]
    public FieldElement dojoCombatId;
    


    [ModelField("player_a")]
    public FieldElement dojoPlayerA;
    


    [ModelField("player_b")]
    public FieldElement dojoPlayerB;
    


    [ModelField("blobert_a")]
    public FieldElement dojoBlobertA;
    


    [ModelField("blobert_b")]
    public FieldElement dojoBlobertB;
    

    #endregion  

    private void Start()
    {
        DojoEntitiesStorage.knockoutDict.Add(dojoCombatId.Hex(), this);

        if (DojoEntitiesStorage.challengeInvite != null)
        {
            var invStruct = DojoEntitiesStorage.challengeInvite;

            if (dojoPlayerA.Hex() == invStruct.dojoSender.Hex()  ||   dojoPlayerA.Hex() == invStruct.dojoReceiver.Hex())
            {
                
            }
            else
            {
                return;
            }

            if (dojoPlayerB.Hex() == invStruct.dojoSender.Hex() || dojoPlayerB.Hex() == invStruct.dojoReceiver.Hex())
            {
                DojoEntitiesStorage.knockoutCurrentGame = this;
            }
            else
            {
                return;
            }
        }
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);
    }
}
