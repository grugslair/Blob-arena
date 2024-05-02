using Dojo;
using Dojo.Starknet;
using Dojo.Torii;

public class LobbyPlayer : ModelInstance
{
    [ModelField("address")]
    public FieldElement id;

    [ModelField("lobby_id")]
    public FieldElement lobbyId;
    [ModelField("blobert_id")]
    public FieldElement blobertId;
    [ModelField("wins")]
    public FieldElement wins;
    [ModelField("joined")]
    public bool joined;

    // Start is called before the first frame update
    void Start()
    {

    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);
    }
}
