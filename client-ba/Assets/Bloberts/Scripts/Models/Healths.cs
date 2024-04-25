using Dojo;
using Dojo.Starknet;
using Dojo.Torii;
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
        DojoEntitiesStatic.healthsList.Add(this);
    }

    private void Update()
    {

    }

    public override void OnUpdate(Model model)
    {
        base.OnUpdate(model);

        if (DojoEntitiesStatic.currentRoundId != null)
        {
            if (combatId.Hex() == DojoEntitiesStatic.currentRoundId.Hex())
            {

                Debug.Log("Healths updated");
                Debug.Log("a value: " + a);
                Debug.Log("b value: " + b);

                UiReferencesStatic.battlePageBehaviour.UpdateData();
            }
        }
    }
}
