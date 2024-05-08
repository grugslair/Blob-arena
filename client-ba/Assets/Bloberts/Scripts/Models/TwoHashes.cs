using Dojo;
using Dojo.Starknet;
using Dojo.Torii;
using System;

public class TwoHashes : ModelInstance
{

    #region ModelFields
    [ModelField("id")]
    public FieldElement combatId;

    [ModelField("a")]
    public FieldElement a;
    [ModelField("b")]
    public FieldElement b;
    #endregion



    private void Start()
    {
        if (DojoEntitiesStorage.currentCombatId != null)
        {
            if (DojoEntitiesStorage.currentCombatId.Hex() == combatId.Hex())
            {
                DojoEntitiesStorage.twoHashesCurrentGame = this;
            }
        }

        if (DojoEntitiesStorage.currentCombatId == null)
        {
            return;
        }

        if (DojoEntitiesStorage.currentCombatId.Hex() == combatId.Hex())
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

        if (DojoEntitiesStorage.currentCombatId.Hex() != combatId.Hex())
        {
            return;
        }

        if (UiReferencesStatic.battlePageBehaviour != null)
        {
            UiReferencesStatic.battlePageBehaviour.CallFromDataToUpdate();
        }
    }
}
