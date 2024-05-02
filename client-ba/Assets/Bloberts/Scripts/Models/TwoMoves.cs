using Dojo;
using Dojo.Starknet;
using Dojo.Torii;

public enum MoveN
{
    NONE,
    BEAT,
    COUNTER,
    RUSH
}

public class TwoMoves : ModelInstance
{
    [ModelField("id")]
    public FieldElement roundId;

    [ModelField("a")]
    public MoveN a;
    [ModelField("b")]
    public MoveN b;

    private void Start()
    {
        if (DojoEntitiesStorage.currentCombatId != null)
        {
            if (DojoEntitiesStorage.currentCombatId.Hex() == roundId.Hex())
            {
                DojoEntitiesStorage.twoMovesCurrentGame = this;
            }
        }

        if (DojoEntitiesStorage.currentCombatId == null)
        {
            return;
        }

        if (DojoEntitiesStorage.currentCombatId.Hex() == roundId.Hex())
        {
            DojoEntitiesStorage.twoMovesCurrentGame = this;

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
