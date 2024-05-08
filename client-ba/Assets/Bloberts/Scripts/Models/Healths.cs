using Dojo;
using Dojo.Starknet;
using Dojo.Torii;
using System;
using UnityEngine;

public class Healths : ModelInstance
{
    #region GeneratedRegion 

    [ModelField("combat_id")]
    public FieldElement dojoCombatId;
    


    [ModelField("a")]
    public byte dojoA;
    


    [ModelField("b")]
    public byte dojoB;
    

    #endregion  

    private void Start()
    {
        DojoEntitiesStorage.healthsDict.Add(dojoCombatId.Hex(), this);
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);

        if (this == DojoEntitiesStorage.healthsCurrentGame)
        {
            if (UiReferencesStatic.battlePageBehaviour != null)
            {
                UiReferencesStatic.battlePageBehaviour.CallFromDataToUpdate();
            }
        }
    }
}
