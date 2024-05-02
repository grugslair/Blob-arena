using Dojo;
using Dojo.Starknet;
using Dojo.Torii;

public class LastRound : ModelInstance
{
    [ModelField("combat_id")]
    public FieldElement combatId;

    [ModelField("health_a")]
    public byte healthA;
    [ModelField("health_b")]
    public byte healthB;

    [ModelField("move_a")]
    public BlobertUtils.Move moveA;
    [ModelField("move_b")]
    public BlobertUtils.Move moveB;

    [ModelField("damage_a")]
    public byte damageA;
    [ModelField("damage_b")]
    public byte damageB;

    private void Start()
    {
        if (DojoEntitiesStorage.currentCombatId.Hex() == this.combatId.Hex())
        {
            DojoEntitiesStorage.lastRoundCurrentGame = this;
        }
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);

        if (this == DojoEntitiesStorage.lastRoundCurrentGame)
        {
            UiReferencesStatic.battlePageBehaviour.UpdateFrontEndData();
        }
    }
}
