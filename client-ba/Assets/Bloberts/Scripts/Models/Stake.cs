using Dojo;
using Dojo.Starknet;
using Dojo.Torii;

public class Stake : ModelInstance
{

    [ModelField("id")]
    public FieldElement id;

    [ModelField("owner")]
    public FieldElement owner;
    [ModelField("running")]
    public bool running;


    // Start is called before the first frame update
    void Start()
    {
        
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);
    }
}
