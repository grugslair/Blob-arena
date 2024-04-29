using Dojo;
using Dojo.Starknet;
using Dojo.Torii;
using UnityEngine;

public class Blobert : ModelInstance
{
    [ModelField("id")]
    public FieldElement blobertId;

    [ModelField("owner")]
    public FieldElement owner;

    [ModelField("stats")]
    public BlobertUtils.Stats stats;
    [ModelField("traits")]
    public BlobertUtils.Traits traits;

    private void Start()
    {
        if (owner.Hex() == DojoEntitiesStatic.currentAccount.Address.Hex())
        {
            DojoEntitiesStatic.userBlobertData = this;
        }

        DojoEntitiesStatic.allBlobertDict.Add(blobertId.Hex(), this);

        Debug.Log($"this is the id");
        Debug.Log($"");
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);

    }
}
