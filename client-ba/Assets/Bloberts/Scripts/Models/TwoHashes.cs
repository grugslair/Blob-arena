using Dojo;
using Dojo.Starknet;
using Dojo.Torii;
using System;

public class TwoHashes : ModelInstance
{
    #region GeneratedRegion 

    [ModelField("id")]
    public FieldElement dojoId;
    


    [ModelField("a")]
    public FieldElement dojoA;
    


    [ModelField("b")]
    public FieldElement dojoB;
    

    #endregion



    private void Start()
    {
        if (DojoEntitiesStorage.currentCombatId != null)
        {
            if (DojoEntitiesStorage.currentCombatId.Hex() == dojoId.Hex())
            {
                DojoEntitiesStorage.twoHashesCurrentGame = this;
            }
        }

        if (DojoEntitiesStorage.currentCombatId == null)
        {
            return;
        }

        if (DojoEntitiesStorage.currentCombatId.Hex() == dojoId.Hex())
        {
            DojoEntitiesStorage.twoHashesCurrentGame = this;

            if (UiReferencesStatic.battlePageBehaviour != null)
            {
                UiReferencesStatic.battlePageBehaviour.CallFromDataToUpdate();
            }
        }
    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);
         
        if (DojoEntitiesStorage.currentCombatId == null)
        {
            return;
        }

        if (DojoEntitiesStorage.currentCombatId.Hex() != dojoId.Hex())
        {
            return;
        }

        if (UiReferencesStatic.battlePageBehaviour != null)
        {
            UiReferencesStatic.battlePageBehaviour.CallFromDataToUpdate();
        }
    }
}
