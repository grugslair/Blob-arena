using Dojo;
using Dojo.Starknet;
using Dojo.Torii;
using System;
using System.Numerics;

public class Round : ModelInstance
{
    [ModelField("combat_id")]
    public FieldElement combatId;

    [ModelField("number")]
    public UInt32 number;

    [ModelField("a_health")]
    public byte healthA;
    [ModelField("b_health")]
    public byte healthB;

    private void Start()
    {
        
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);

    }
}
