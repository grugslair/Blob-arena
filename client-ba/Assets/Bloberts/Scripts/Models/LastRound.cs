using Dojo;
using Dojo.Starknet;
using Dojo.Torii;

public class LastRound : ModelInstance
{
    #region GeneratedRegion 

    [ModelField("combat_id")]
    public FieldElement dojoCombatId;
    


    [ModelField("health_a")]
    public byte dojoHealthA;
    


    [ModelField("health_b")]
    public byte dojoHealthB;
    


    [ModelField("move_a")]
    public BlobertUtils.Move dojoMoveA;
    


    [ModelField("move_b")]
    public BlobertUtils.Move dojoMoveB;
    


    [ModelField("damage_a")]
    public byte dojoDamageA;
    


    [ModelField("damage_b")]
    public byte dojoDamageB;
    

    #endregion 

    private void Start()
    {
        if (DojoEntitiesStorage.currentCombatId.Hex() == this.dojoCombatId.Hex())
        {
            DojoEntitiesStorage.lastRoundCurrentGame = this;
        }
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);

        if (this == DojoEntitiesStorage.lastRoundCurrentGame)
        {
            UiReferencesStatic.battlePageBehaviour.UpdateLastRound(this);
        }
    }
}
