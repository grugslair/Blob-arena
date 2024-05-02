using Dojo;
using Dojo.Starknet;
using Dojo.Torii;

public class Blobert : ModelInstance
{
    [ModelField("id")]
    public FieldElement dojoBlobertId;

    [ModelField("owner")]
    public FieldElement dojoOwner;

    [ModelField("stats")]
    public BlobertUtils.Stats dojoStats;
    [ModelField("traits")]
    public BlobertUtils.Traits dojoTraits;

    private FieldElement _savedOwner;

    private void Start()
    {
        if (dojoOwner.Hex() == DojoEntitiesStorage.currentAccount.Address.Hex())
        {
            DojoEntitiesStorage.userBloberts.Add(this);
        }

        DojoEntitiesStorage.allBlobertDict.Add(dojoBlobertId.Hex(), this);

        _savedOwner = dojoOwner;
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);

        if (_savedOwner == null)
        {
            return;
        }

        if (_savedOwner.Hex() != dojoOwner.Hex())
        {
            if (_savedOwner.Hex() == DojoEntitiesStorage.currentAccount.Address.Hex())
            {
                DojoEntitiesStorage.userBloberts.Remove(this);
            }
            else if (dojoOwner.Hex() == DojoEntitiesStorage.currentAccount.Address.Hex())
            {
                DojoEntitiesStorage.userBloberts.Add(this);
            }

            _savedOwner = dojoOwner;
        }
    }
}
