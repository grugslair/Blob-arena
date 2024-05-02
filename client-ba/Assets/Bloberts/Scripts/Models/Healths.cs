using Dojo;
using Dojo.Starknet;
using Dojo.Torii;
using System;
using UnityEngine;

public class Healths : ModelInstance
{
    [ModelField("combat_id")]
    public FieldElement combatId;

    [ModelField("a")]
    public byte a;
    [ModelField("b")]
    public byte b;

    private void Start()
    {
        DojoEntitiesStorage.healthsDict.Add(combatId.Hex(), this);
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

        //if (DojoEntitiesStorage.inLobbyRoundId != null)
        //{
        //    if (combatId.Hex() == DojoEntitiesStorage.inLobbyRoundId.Hex())
        //    {
        //        UiReferencesStatic.battlePageBehaviour.UpdateFrontEndData();
        //    }
        //}
   
        //if (DojoEntitiesStorage.inLobbyRoundId == null)
        //{
        //    return;
        //}

        //if (DojoEntitiesStorage.inLobbyRoundId.Hex() != combatId.Hex())
        //{
        //    return;
        //}

        //if (UiReferencesStatic.battlePageBehaviour != null)
        //{
        //    UiReferencesStatic.battlePageBehaviour.CallFromDataToUpdate();
        //}
    }

}
