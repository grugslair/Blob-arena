using Dojo;
using Dojo.Starknet;
using Dojo.Torii;
using System;

public class TwoHashes : ModelInstance
{
    [ModelField("id")]
    public FieldElement roundId;

    [ModelField("a")]
    public FieldElement b;
    [ModelField("b")]
    public FieldElement a;

    private void Start()
    {
        if (DojoEntitiesStatic.currentRoundId != null)
        {
            if (DojoEntitiesStatic.currentRoundId.Hex() == roundId.Hex())
            {
                DojoEntitiesStatic.twoHashesCurrentGame = this;
            }
        }
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);
    }
}
