using Dojo;
using Dojo.Starknet;
using Dojo.Torii;
using System;

public class Lobby : ModelInstance
{
    [ModelField("combat_id")]
    public FieldElement combatId;

    [ModelField("amount")]
    public BlobertUtils.U256 a;
    [ModelField("blobert")]
    public Boolean b;

    // Start is called before the first frame update
    void Start()
    {
        
    }
    

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);

    }
}
