using Dojo;
using Dojo.Starknet;
using Dojo.Torii;

public class Stake : ModelInstance
{
    #region GeneratedRegion 

    [ModelField("combat_id")]
    public FieldElement dojoCombatId;
    


    [ModelField("amount")]
    public BlobertUtils.u256 dojoAmount;
    


    [ModelField("blobert")]
    public bool dojoBlobert;
    

    #endregion

    // Start is called before the first frame update
    void Start()
    {
        
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);
    }
}
