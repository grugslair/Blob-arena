using Dojo;
using Dojo.Starknet;
using Dojo.Torii;

public class Blobert : ModelInstance
{
    #region GeneratedRegion 

    [ModelField("id")]
    public FieldElement dojoId;
    


    [ModelField("owner")]
    public FieldElement dojoOwner;
    


    [ModelField("traits")]
    public BlobertUtils.Traits dojoTraits;
    


    [ModelField("stats")]
    public BlobertUtils.Stats dojoStats;
    

    #endregion  

    private FieldElement _savedOwner;

    private void Start()
    {
        if (dojoOwner.Hex() == DojoEntitiesStorage.currentAccount.Address.Hex())
        {
            DojoEntitiesStorage.userBloberts.Add(this);
        }

        DojoEntitiesStorage.allBlobertDict.Add(dojoId.Hex(), this);

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
