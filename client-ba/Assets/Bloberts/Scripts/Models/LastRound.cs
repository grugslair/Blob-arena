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
    public BlobertUitls.Move moveA;
    [ModelField("move_b")]
    public BlobertUitls.Move moveB;

    [ModelField("damage_a")]
    public byte damageA;
    [ModelField("damage_b")]
    public byte damageB;

    private void Start()
    {
        if (DojoEntitiesStatic.currentRoundId != null)
        {
            if (combatId.Hex() == DojoEntitiesStatic.currentRoundId.Hex())
            {
                DojoEntitiesStatic.lastRoundCurrentGame = this;
            }
        }
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);

        if (DojoEntitiesStatic.currentRoundId != null)
        {
            if (combatId.Hex() == DojoEntitiesStatic.currentRoundId.Hex())
            {
                UiReferencesStatic.battlePageBehaviour.UpdateData();
            }
        }
    }
}
