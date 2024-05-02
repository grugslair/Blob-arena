using Dojo;
using Dojo.Starknet;
using Dojo.Torii;
using System;

public class TwoHashes : ModelInstance
{
    [ModelField("id")]
    public FieldElement roundId;

    [ModelField("a")]
    public FieldElement a;
    [ModelField("b")]
    public FieldElement b;

    private void Start()
    {
        if (DojoEntitiesStorage.currentCombatId != null)
        {
            if (DojoEntitiesStorage.currentCombatId.Hex() == roundId.Hex())
            {
                DojoEntitiesStorage.twoHashesCurrentGame = this;
            }
        }

        if (DojoEntitiesStorage.currentCombatId == null)
        {
            return;
        }

        if (DojoEntitiesStorage.currentCombatId.Hex() == roundId.Hex())
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

        if (DojoEntitiesStorage.currentCombatId.Hex() != roundId.Hex())
        {
            return;
        }

        if (UiReferencesStatic.battlePageBehaviour != null)
        {
            UiReferencesStatic.battlePageBehaviour.CallFromDataToUpdate();
        }
    }
}
